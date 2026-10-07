"use strict";

const $ = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];

const state = {
  problems: [],
  topics: [],
  current: null,
  savedSql: "",
  saveTimer: null,
  solutionShown: false,
  autoStartTimer: false,
};

const VERDICTS = { PASS: "Accepted", FAIL: "Wrong Answer", ERROR: "Error", TODO: "Nothing to submit" };
const TARGET_MIN = { medium: 15, hard: 25 };

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

function esc(s) {
  return String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

function inline(s) {
  return esc(s).replace(/`([^`]+)`/g, "<code>$1</code>");
}

async function api(path, body) {
  const opts = body === undefined ? {} : {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  };
  const res = await fetch(path, opts);
  if (!res.ok) throw new Error((await res.json().catch(() => ({}))).error || res.statusText);
  return res.json();
}

function cell(v) {
  if (v === null || v === undefined) return '<td class="null">NULL</td>';
  if (typeof v === "number") return `<td class="num">${v}</td>`;
  if (typeof v === "object") return `<td>${esc(JSON.stringify(v))}</td>`;
  if (typeof v === "string" && /^-?\d+(\.\d+)?$/.test(v)) return `<td class="num">${v}</td>`;
  return `<td>${esc(v)}</td>`;
}

function grid(columns, rows, types) {
  const head = columns.map((c, i) =>
    `<th>${esc(c)}${types && types[i] ? `<small>${esc(types[i])}</small>` : ""}</th>`).join("");
  const body = rows.map((r, i) => `<tr><td class="idx">${i + 1}</td>${r.map(cell).join("")}</tr>`).join("");
  return `<div class="grid-wrap"><table class="grid"><thead><tr><th class="idx">#</th>${head}</tr></thead>` +
         `<tbody>${body}</tbody></table></div>`;
}

function selectTab(group, name) {
  $$(`[data-tabs="${group}"] .tab`).forEach(t => t.classList.toggle("active", t.dataset.tab === name));
  const names = $$(`[data-tabs="${group}"] .tab`).map(t => t.dataset.tab);
  names.forEach(n => $(`#tab-${n}`).classList.toggle("hidden", n !== name));
}

// ---------------------------------------------------------------------------
// Editor (CodeMirror when the CDN loads, plain textarea otherwise)
// ---------------------------------------------------------------------------

function textareaEditor(ta) {
  const handlers = [];
  ta.addEventListener("input", () => handlers.forEach(h => h()));
  ta.addEventListener("keydown", e => {
    if (e.key === "Tab") {
      e.preventDefault();
      ta.setRangeText("    ", ta.selectionStart, ta.selectionEnd, "end");
      handlers.forEach(h => h());
    }
  });
  ta.placeholder = "Write your SQL here";
  return {
    getValue: () => ta.value,
    setValue: v => { ta.value = v; },
    getSelection: () => ta.value.substring(ta.selectionStart, ta.selectionEnd),
    on: (_evt, fn) => handlers.push(fn),
    focus: () => ta.focus(),
    refresh() {},
    clearHistory() {},
    setOption() {},
  };
}

function createEditor() {
  const ta = $("#editor");
  if (!window.CodeMirror) return textareaEditor(ta);
  const keys = {
    "Cmd-Enter": () => runQuery(), "Ctrl-Enter": () => runQuery(),
    "Shift-Cmd-Enter": () => submit(), "Shift-Ctrl-Enter": () => submit(),
    "Cmd-S": () => saveNow(), "Ctrl-S": () => saveNow(),
    "Cmd-/": "toggleComment", "Ctrl-/": "toggleComment",
    "Ctrl-Space": "autocomplete",
    Tab: cm => cm.somethingSelected() ? cm.indentSelection("add") : cm.replaceSelection("    "),
  };
  const cm = CodeMirror.fromTextArea(ta, {
    mode: "text/x-pgsql",
    lineNumbers: true,
    indentUnit: 4,
    matchBrackets: true,
    autoCloseBrackets: true,
    styleActiveLine: true,
    extraKeys: keys,
    hintOptions: { completeSingle: false },
  });
  cm.on("inputRead", (_cm, change) => {
    if (change.text[0] === ".") cm.showHint({ completeSingle: false });
  });
  return cm;
}

const editor = createEditor();

// ---------------------------------------------------------------------------
// Sidebar
// ---------------------------------------------------------------------------

function renderList() {
  const q = $("#search").value.trim().toLowerCase();
  const level = $("#filter-difficulty").value;
  const status = $("#filter-status").value;
  const match = p =>
    (!q || p.title.toLowerCase().includes(q) || String(p.id) === q || p.key === q) &&
    (!level || p.difficulty === level) &&
    (!status || (status === "unsolved" ? p.status !== "PASS" : p.status === status));

  const html = state.topics.map(topic => {
    const items = state.problems.filter(p => p.topic === topic && match(p));
    if (!items.length) return "";
    return `<div class="topic-head">${esc(topic)}</div>` + items.map(p => `
      <a class="problem-link ${state.current && state.current.id === p.id ? "active" : ""}" href="#/${p.id}" data-id="${p.id}">
        <span class="dot ${p.status}" title="${p.status}"></span>
        <span class="num">${p.key}</span>
        <span class="name" title="${esc(p.title)}">${esc(p.title)}</span>
        <span class="diff-tag ${p.difficulty}">${p.difficulty === "hard" ? "H" : "M"}</span>
      </a>`).join("");
  }).join("");
  $("#problem-list").innerHTML = html || '<p class="muted" style="padding:12px">No problems match.</p>';

  const solved = state.problems.filter(p => p.status === "PASS").length;
  $("#progress-text").textContent = `${solved} / ${state.problems.length} solved`;
  $("#progress-fill").style.width = `${(100 * solved) / (state.problems.length || 1)}%`;
}

function setStatus(id, status) {
  const p = state.problems.find(x => x.id === id);
  if (p) p.status = status;
  if (state.current && state.current.id === id) state.current.status = status;
  renderList();
}

// ---------------------------------------------------------------------------
// Problem panes
// ---------------------------------------------------------------------------

function renderPrompt(lines) {
  const out = [];
  let para = [], list = null, pre = null;
  const flushPara = () => { if (para.length) out.push(`<p>${inline(para.join(" "))}</p>`); para = []; };
  const flushList = () => { if (list) out.push(`<ul>${list.map(li => `<li>${inline(li)}</li>`).join("")}</ul>`); list = null; };
  const flushPre = () => { if (pre) out.push(`<pre>${esc(pre.join("\n"))}</pre>`); pre = null; };
  const flushAll = () => { flushPara(); flushList(); flushPre(); };

  for (const line of lines) {
    if (!line.trim()) { flushAll(); continue; }
    if (/^\s*\* /.test(line)) {
      flushPara(); flushPre();
      (list = list || []).push(line.replace(/^\s*\* /, ""));
    } else if (list && /^\s{3,}\S/.test(line)) {
      list[list.length - 1] += " " + line.trim();
    } else if (/^\s{2,}\S/.test(line)) {
      flushPara(); flushList();
      (pre = pre || []).push(line.replace(/^ {2}/, ""));
    } else if (/^[A-Z][\w()/-]*(?: [\w()/-]+){0,2}:$/.test(line.trim())) {
      flushAll();
      out.push(`<h4>${esc(line.trim().slice(0, -1))}</h4>`);
    } else {
      flushList(); flushPre();
      para.push(line.trim());
    }
  }
  flushAll();
  return out.join("");
}

function renderDescription(p) {
  const tables = p.tables.map(t => `<span class="col-chip table-link" data-table="${esc(t)}">${esc(t)}</span>`).join("");
  const cols = p.output_columns.split(",").map(c => `<span class="col-chip">${esc(c.trim())}</span>`).join("");
  $("#tab-description").innerHTML = `
    <h1 class="problem-title">${p.key}. ${esc(p.title)}</h1>
    <div class="meta">
      <span class="pill ${p.difficulty}">${p.difficulty === "hard" ? "Hard" : "Medium"}</span>
      <span class="pill">${esc(p.topic)}</span>
      ${p.status === "PASS" ? '<span class="pill PASS">Solved</span>' : ""}
    </div>
    ${p.inspired_by ? `<p class="inspired">Inspired by ${esc(p.inspired_by)}</p>` : ""}
    <div class="prompt">${renderPrompt(p.description)}</div>
    <dl class="spec">
      <dt>Tables</dt><dd>${tables}</dd>
      <dt>Output columns</dt><dd>${cols}</dd>
      <dt>Row order</dt><dd>${inline(p.row_order)}${p.ordered ? " <span class=\"muted\">(checked)</span>" : ""}</dd>
    </dl>`;
  $$(".table-link", $("#tab-description")).forEach(el => el.addEventListener("click", () => {
    selectTab("left", "schema");
    const target = document.getElementById(`schema-${el.dataset.table}`);
    if (target) target.scrollIntoView({ block: "start" });
  }));
}

function schemaBlock(t) {
  const cols = t.columns.map(c => `<span><b>${esc(c.name)}</b> ${esc(c.type)}</span>`).join("");
  return `
    <div class="schema-table" id="schema-${esc(t.name)}">
      <div class="schema-head">
        <h3>${esc(t.name)}</h3><span class="count">${t.count} rows</span>
        <button class="btn ghost" data-preview="${esc(t.name)}">Query all rows</button>
      </div>
      <div class="schema-cols">${cols}</div>
      ${grid(t.columns.map(c => c.name), t.sample)}
      ${t.count > t.sample.length ? `<p class="note">Showing ${t.sample.length} of ${t.count} rows.</p>` : ""}
    </div>`;
}

function renderSchema(p) {
  const primary = p.schema.filter(t => p.tables.includes(t.name));
  const others = p.schema.filter(t => !p.tables.includes(t.name));
  $("#tab-schema").innerHTML = `
    <p class="note">Every Run and Submit starts from a fresh in-memory copy of the
      <code>${p.datasets.join("</code>, <code>")}</code> dataset, so INSERT, UPDATE, and CREATE TABLE are safe to try.</p>
    ${primary.map(schemaBlock).join("")}
    ${others.length ? `<details class="other-tables"><summary>Other tables loaded for this problem (${others.length})</summary>
      ${others.map(schemaBlock).join("")}</details>` : ""}`;
  $$("[data-preview]", $("#tab-schema")).forEach(btn => btn.addEventListener("click", () =>
    runQuery(`SELECT * FROM "${btn.dataset.preview}"`, `Preview of ${btn.dataset.preview}`)));

  const tables = {};
  p.schema.forEach(t => { tables[t.name] = t.columns.map(c => c.name); });
  editor.setOption("hintOptions", { tables, completeSingle: false });
}

function renderSolutionLocked(p) {
  state.solutionShown = false;
  if (p.status === "PASS") return showSolution();
  $("#tab-solution").innerHTML = `
    <div class="locked">
      <p>The reference solution explains the approach and the trap the data is built to catch.</p>
      <p>Give it an honest attempt first: about ${TARGET_MIN[p.difficulty]} minutes for a ${p.difficulty} problem.</p>
      <button class="btn" id="reveal-btn">Reveal solution</button>
    </div>`;
  $("#reveal-btn").addEventListener("click", () => {
    if (confirm("Reveal the reference solution for this problem?")) showSolution();
  });
}

async function showSolution() {
  const p = state.current;
  const { sql } = await api(`/api/problems/${p.id}/solution`);
  if (state.current !== p) return;
  state.solutionShown = true;
  $("#tab-solution").innerHTML = `
    <div style="display:flex;gap:8px;margin-bottom:10px">
      <button class="btn" id="run-ref-btn">Run reference solution</button>
    </div>
    <div id="solution-view" class="solution-code"></div>`;
  const view = $("#solution-view");
  if (window.CodeMirror) {
    const cm = CodeMirror(view, { value: sql.trim(), mode: "text/x-pgsql", readOnly: true, lineNumbers: true });
    cm.setSize(null, "auto");
  } else {
    view.innerHTML = `<pre>${esc(sql)}</pre>`;
  }
  $("#run-ref-btn").addEventListener("click", () => runQuery(sql, "Reference solution output"));
}

// ---------------------------------------------------------------------------
// Saving
// ---------------------------------------------------------------------------

function setSaveState(text) { $("#save-state").textContent = text; }

async function saveNow() {
  clearTimeout(state.saveTimer);
  state.saveTimer = null;
  const p = state.current;
  if (!p) return;
  const sql = editor.getValue();
  if (sql === state.savedSql) return;
  try {
    await api(`/api/problems/${p.id}/save`, { sql });
    if (state.current === p) {
      state.savedSql = sql;
      setSaveState(`Saved to problems/${p.filename}`);
    }
  } catch (err) {
    setSaveState(`Save failed: ${err.message}`);
  }
}

editor.on("change", () => {
  if (!state.current || editor.getValue() === state.savedSql) return;
  if (state.autoStartTimer) { state.autoStartTimer = false; timer.start(); }
  setSaveState("Unsaved changes");
  clearTimeout(state.saveTimer);
  state.saveTimer = setTimeout(saveNow, 800);
});

window.addEventListener("beforeunload", () => {
  if (state.current && state.saveTimer) {
    navigator.sendBeacon(`/api/problems/${state.current.id}/save`, JSON.stringify({ sql: editor.getValue() }));
  }
});

// ---------------------------------------------------------------------------
// Run and submit
// ---------------------------------------------------------------------------

function busy(on) {
  ["#run-btn", "#submit-btn", "#reset-btn"].forEach(s => { $(s).disabled = on; });
}

async function runQuery(sqlOverride, label) {
  const p = state.current;
  if (!p) return;
  const selection = editor.getSelection();
  const sql = sqlOverride || selection || editor.getValue();
  selectTab("right", "result");
  $("#tab-result").innerHTML = '<p class="muted">Running...</p>';
  busy(true);
  try {
    const r = await api(`/api/problems/${p.id}/run`, { sql });
    if (state.current !== p) return;
    if (r.error) {
      $("#tab-result").innerHTML = `<div class="error-box">${esc(r.error)}</div>`;
      return;
    }
    const title = label || (selection && !sqlOverride ? "Selection" : "Your query");
    $("#tab-result").innerHTML = `
      <div class="result-meta"><span>${esc(title)}</span><span>${r.total} rows</span><span>${r.ms} ms</span>
        ${r.truncated ? `<span>showing first ${r.rows.length}</span>` : ""}</div>
      ${r.columns.length ? grid(r.columns, r.rows, r.types) : '<p class="muted">Statement ran. No result set.</p>'}`;
  } catch (err) {
    $("#tab-result").innerHTML = `<div class="error-box">${esc(err.message)}</div>`;
  } finally {
    busy(false);
  }
}

function historyKey(id) { return `sqlp-history-${id}`; }

function readHistory(id) {
  try { return JSON.parse(localStorage.getItem(historyKey(id))) || []; } catch { return []; }
}

function pushHistory(id, status, ms) {
  const items = [{ t: Date.now(), status, ms, elapsed: timer.elapsed() }, ...readHistory(id)].slice(0, 10);
  localStorage.setItem(historyKey(id), JSON.stringify(items));
}

function renderHistory(id) {
  const items = readHistory(id);
  if (!items.length) return "";
  const fmt = ms => `${Math.floor(ms / 60000)}m ${Math.floor((ms % 60000) / 1000)}s`;
  return `<div class="history">Recent submissions<ol>${items.map(h =>
    `<li><span class="${h.status}">${VERDICTS[h.status]}</span> &middot; ${new Date(h.t).toLocaleString()}` +
    `${h.elapsed ? ` &middot; timer ${fmt(h.elapsed)}` : ""}</li>`).join("")}</ol></div>`;
}

function renderSubmission(p, r) {
  let sub = "", body = "";
  if (r.status === "PASS") {
    sub = `${r.total} rows matched in ${r.ms} ms. Open the Solution tab to compare approaches and see the trap this data is built to catch.`;
  } else if (r.status === "ERROR" || r.status === "TODO") {
    body = `<div class="error-box">${esc(r.message)}</div>`;
  } else if (r.reason === "rows") {
    sub = `Expected ${r.expected_count} rows, got ${r.total}.`;
    if (r.missing.length) {
      body += `<div class="diff-section"><h4 class="missing">Missing rows: expected but not returned (${r.missing.length})</h4>
        ${grid(r.expected_columns, r.missing)}</div>`;
    }
    if (r.extra.length) {
      body += `<div class="diff-section"><h4 class="extra">Extra rows: returned but not expected (${r.extra.length})</h4>
        ${grid(r.expected_columns, r.extra)}</div>`;
    }
    body += `<p class="note" style="margin-top:12px">Numbers are compared rounded to 2 decimals and dates as ISO strings.</p>`;
  } else {
    sub = r.message;
  }
  if (r.columns && r.columns.length && r.status !== "PASS") {
    body += `<details style="margin-top:12px"><summary class="muted" style="cursor:pointer">Your output (${r.total} rows)</summary>
      <div style="margin-top:8px">${grid(r.columns, r.rows, r.types)}</div></details>`;
  }
  $("#tab-submission").innerHTML = `
    <p class="verdict ${r.status}">${VERDICTS[r.status]}</p>
    ${sub ? `<p class="verdict-sub">${esc(sub)}</p>` : ""}
    ${body}
    ${renderHistory(p.id)}`;
}

async function submit() {
  const p = state.current;
  if (!p) return;
  clearTimeout(state.saveTimer);
  state.saveTimer = null;
  const sql = editor.getValue();
  selectTab("right", "submission");
  $("#tab-submission").innerHTML = '<p class="muted">Checking...</p>';
  busy(true);
  try {
    const r = await api(`/api/problems/${p.id}/submit`, { sql });
    state.savedSql = sql;
    setSaveState(`Saved to problems/${p.filename}`);
    if (r.status !== "TODO") pushHistory(p.id, r.status, r.ms);
    if (state.current !== p) return;
    const wasSolved = p.status === "PASS";
    setStatus(p.id, r.status);
    renderSubmission(p, r);
    if (r.status === "PASS") {
      timer.pause();
      if (!wasSolved) renderDescription(p);
      if (!state.solutionShown) showSolution();
    }
  } catch (err) {
    $("#tab-submission").innerHTML = `<div class="error-box">${esc(err.message)}</div>`;
  } finally {
    busy(false);
  }
}

async function resetAnswer() {
  const p = state.current;
  if (!p || !confirm(`Clear your answer for problem ${p.key}? This empties problems/${p.filename} below the marker.`)) return;
  clearTimeout(state.saveTimer);
  state.saveTimer = null;
  await api(`/api/problems/${p.id}/reset`, {});
  state.savedSql = "";
  editor.setValue("");
  setSaveState("Answer cleared");
  state.autoStartTimer = true;
  setStatus(p.id, "TODO");
  renderDescription(state.current);
  renderSolutionLocked(state.current);
  $("#tab-submission").innerHTML = `<p class="muted">Submit to check your answer against the expected output.</p>${renderHistory(p.id)}`;
}

// ---------------------------------------------------------------------------
// Timer
// ---------------------------------------------------------------------------

const timer = (() => {
  let base = 0, startedAt = null, target = 0, tick = null;
  const elapsed = () => base + (startedAt ? Date.now() - startedAt : 0);
  const fmt = ms => {
    const s = Math.floor(ms / 1000);
    return `${String(Math.floor(s / 60)).padStart(2, "0")}:${String(s % 60).padStart(2, "0")}`;
  };
  const paint = () => {
    const ms = elapsed();
    $("#timer-text").textContent = fmt(ms);
    $("#timer-target").textContent = `/ ${fmt(target)}`;
    const el = $("#timer");
    el.classList.toggle("running", !!startedAt);
    el.classList.toggle("warn", ms >= target * 0.8 && ms < target);
    el.classList.toggle("over", ms >= target);
  };
  return {
    elapsed,
    start() { if (!startedAt) { startedAt = Date.now(); tick = setInterval(paint, 1000); paint(); } },
    pause() { if (startedAt) { base = elapsed(); startedAt = null; clearInterval(tick); paint(); } },
    toggle() { startedAt ? this.pause() : this.start(); },
    reset(minutes) { this.pause(); base = 0; if (minutes) target = minutes * 60000; paint(); },
  };
})();

// ---------------------------------------------------------------------------
// Routing
// ---------------------------------------------------------------------------

async function openProblem(id) {
  if (state.saveTimer) await saveNow();
  let p;
  try {
    p = await api(`/api/problems/${id}`);
  } catch (err) {
    $("#tab-description").innerHTML = `<div class="error-box">${esc(err.message)}</div>`;
    return;
  }
  state.current = p;
  state.savedSql = p.sql;
  editor.setValue(p.sql);
  editor.clearHistory();
  setSaveState(p.sql ? `Loaded from problems/${p.filename}` : "");
  document.title = `${p.key}. ${p.title} - SQL Practice`;

  renderDescription(p);
  renderSchema(p);
  renderSolutionLocked(p);
  selectTab("left", "description");
  selectTab("right", "result");
  $("#tab-result").innerHTML = '<p class="muted">Run a query to see its output here. With text selected, Run executes only the selection.</p>';
  $("#tab-submission").innerHTML = `<p class="muted">Submit to check your answer against the expected output.</p>${renderHistory(p.id)}`;
  setStatus(p.id, p.status);
  timer.reset(TARGET_MIN[p.difficulty]);
  state.autoStartTimer = p.status !== "PASS";
  editor.refresh();
  editor.focus();
  const link = $(`.problem-link[data-id="${p.id}"]`);
  if (link) link.scrollIntoView({ block: "nearest" });
}

function route() {
  const m = location.hash.match(/^#\/(\d+)/);
  if (m) return openProblem(Number(m[1]));
  const next = state.problems.find(p => p.status !== "PASS") || state.problems[0];
  location.replace(`#/${next.id}`);
}

function randomProblem() {
  const level = $("#random-level").value;
  const pool = state.problems.filter(p =>
    p.status !== "PASS" && (level === "any" || p.difficulty === level) && (!state.current || p.id !== state.current.id));
  if (!pool.length) return alert("Every problem in that pool is solved.");
  const pick = pool[Math.floor(Math.random() * pool.length)];
  location.hash = `#/${pick.id}`;
  setTimeout(() => timer.start(), 300);
}

// ---------------------------------------------------------------------------
// Resizable panes
// ---------------------------------------------------------------------------

function draggable(gutter, onMove) {
  gutter.addEventListener("mousedown", e => {
    e.preventDefault();
    gutter.classList.add("dragging");
    const move = ev => onMove(ev);
    const up = () => {
      gutter.classList.remove("dragging");
      document.removeEventListener("mousemove", move);
      document.removeEventListener("mouseup", up);
      editor.refresh();
    };
    document.addEventListener("mousemove", move);
    document.addEventListener("mouseup", up);
  });
}

function setupResize() {
  const root = document.documentElement.style;
  const saved = JSON.parse(localStorage.getItem("sqlp-layout") || "{}");
  if (saved.left) { root.setProperty("--left-w", saved.left); root.setProperty("--right-w", "1fr"); }
  if (saved.editor) root.setProperty("--editor-h", saved.editor);
  const persist = (k, v) => { saved[k] = v; localStorage.setItem("sqlp-layout", JSON.stringify(saved)); };

  draggable($("#gutter-col"), e => {
    const sidebar = $("#sidebar").getBoundingClientRect();
    const layout = $("#layout").getBoundingClientRect();
    const w = Math.max(280, Math.min(e.clientX - sidebar.right, layout.right - 380 - sidebar.right));
    root.setProperty("--left-w", `${w}px`);
    root.setProperty("--right-w", "1fr");
    persist("left", `${w}px`);
  });
  draggable($("#gutter-row"), e => {
    const ws = $("#workspace").getBoundingClientRect();
    const top = $("#editor-wrap").getBoundingClientRect().top;
    const h = Math.max(80, Math.min(e.clientY - top, ws.bottom - top - 120));
    root.setProperty("--editor-h", `${h}px`);
    persist("editor", `${h}px`);
    editor.refresh();
  });
}

// ---------------------------------------------------------------------------
// Boot
// ---------------------------------------------------------------------------

async function init() {
  const data = await api("/api/problems");
  state.problems = data.problems;
  state.topics = data.topics;
  renderList();

  ["#search", "#filter-difficulty", "#filter-status"].forEach(s => $(s).addEventListener("input", renderList));
  $$(".tab").forEach(t => t.addEventListener("click", () => selectTab(t.closest(".tabs").dataset.tabs, t.dataset.tab)));
  $("#run-btn").addEventListener("click", () => runQuery());
  $("#submit-btn").addEventListener("click", submit);
  $("#reset-btn").addEventListener("click", resetAnswer);
  $("#random-btn").addEventListener("click", randomProblem);
  $("#timer").addEventListener("click", () => timer.toggle());
  $("#timer").addEventListener("dblclick", () => timer.reset());
  document.addEventListener("keydown", e => {
    const mod = e.metaKey || e.ctrlKey;
    if (!mod || (e.target.closest && e.target.closest(".CodeMirror"))) return;
    if (e.key === "Enter") { e.preventDefault(); e.shiftKey ? submit() : runQuery(); }
    if (e.key.toLowerCase() === "s") { e.preventDefault(); saveNow(); }
  });
  window.addEventListener("hashchange", route);
  setupResize();
  route();
}

init().catch(err => {
  document.body.innerHTML = `<div class="error-box" style="margin:40px">Could not reach the server: ${esc(err.message)}.
    Start it with <code>python3 app.py</code> from data_engineering/sql_practice.</div>`;
});
