# Every target runs inside the repo-wide virtual environment at ../../.venv.
#   make setup          create it (if missing) and install requirements.txt
#   make app            browser UI on http://127.0.0.1:8765
#   make all            CLI progress board
#   make check N=24     check one problem
#   make test           pytest over your attempts
#   make solutions      verify every reference solution

VENV := ../../.venv
PY := $(VENV)/bin/python

.PHONY: setup app all check test solutions clean

setup: $(VENV)/.installed

$(VENV)/.installed: requirements.txt
	test -x $(PY) || python3 -m venv $(VENV)
	$(PY) -m pip install --upgrade pip
	$(PY) -m pip install -r requirements.txt
	touch $@

app: setup
	$(PY) app.py

all: setup
	$(PY) run.py --all

check: setup
	$(PY) run.py $(N)

test: setup
	$(PY) -m pytest -q

solutions: setup
	$(PY) run.py --solutions
	SQL_SOLUTIONS=1 $(PY) -m pytest -q

clean:
	rm -rf __pycache__ .pytest_cache
