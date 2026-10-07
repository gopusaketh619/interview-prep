# AWS Certified AI Practitioner (AIF-C01) — Complete Study Guide

> **Goal:** Reading this guide alone should prepare you to score 100% on the exam.  
> **Last updated:** August 2026 (Exam Guide v1.1, April 30 2026)

---

## PART 0: Exam Logistics

| Detail | Value |
|--------|-------|
| Exam Code | AIF-C01 |
| Total Questions | 65 (50 scored + 15 unscored pilot questions) |
| Duration | 90 minutes (~80 seconds per question) |
| Passing Score | 700 / 1000 |
| Question Types | Multiple choice, Multiple response, Ordering, Matching |
| Penalty for guessing | **None** — always answer every question |
| Compensatory scoring | You do NOT need to pass each domain individually |

### Domain Weightings

| Domain | Weight | ~Scored Qs |
|--------|--------|-----------|
| 1. Fundamentals of AI and ML | 20% | 10 |
| 2. Fundamentals of Generative AI | 24% | 12 |
| 3. Applications of Foundation Models | **28%** | 14 |
| 4. Guidelines for Responsible AI | 14% | 7 |
| 5. Security, Compliance, and Governance | 14% | 7 |

> **Critical:** Domains 2 + 3 = **52%** of the exam. Master GenAI and Foundation Models first.

---

# PART 1: DOMAIN 1 — Fundamentals of AI and ML (20%)

## 1.1 Basic AI Concepts and Terminologies

### The AI Hierarchy

```
Artificial Intelligence (broadest umbrella)
└── Machine Learning (learns from data)
    └── Deep Learning (multi-layer neural networks)
        └── Foundation Models (pre-trained on massive data)
            └── Large Language Models (text-focused FMs)
                └── Generative AI (creates new content)
                    └── Agentic AI (autonomous planning + action)
```

**Key distinctions the exam tests:**
- **AI** = Any system that simulates intelligent behavior
- **ML** = Subset of AI; systems learn patterns from data without explicit programming
- **Deep Learning** = Subset of ML using neural networks with many hidden layers; "deep" = many layers, not philosophical depth
- **GenAI** = Creates NEW content (text, images, code, audio, video)
- **Agentic AI** = AI that autonomously plans, reasons, uses tools, and takes multi-step actions

### Core Terminology Deep Dive

| Term | Definition | Exam Context |
|------|-----------|--------------|
| **Algorithm** | Step-by-step computational procedure | The recipe; NOT the trained result |
| **Model** | Trained artifact that maps inputs to outputs | The result of running an algorithm on data |
| **Training** | Process of teaching a model from data | Adjusts model weights/parameters |
| **Inferencing** | Using a trained model to make predictions on new data | The production phase |
| **Bias** | Systematic error that unfairly favors certain outcomes | Can be in data OR model |
| **Fairness** | Equal treatment across demographic groups | Measured by metrics like Demographic Parity |
| **Overfitting** | Model memorizes training data; performs poorly on new data | High variance, low bias |
| **Underfitting** | Model too simple; misses important patterns | High bias, low variance |
| **Neural Network** | Computing system of interconnected nodes (neurons) in layers | Input → Hidden(s) → Output |
| **Computer Vision** | AI for interpreting visual information | AWS: Amazon Rekognition |
| **NLP** | AI for understanding/generating human language | AWS: Amazon Comprehend |
| **LLM** | Neural network trained on massive text to understand/generate language | GPT, Claude, Llama, Titan |
| **Agentic AI** | AI systems that plan, reason, and act autonomously | Bedrock Agents, Strands Agents |

### Neural Networks Explained

```
INPUT LAYER          HIDDEN LAYERS          OUTPUT LAYER
(receives data)      (learns patterns)      (produces result)

  [x1] ─────────┐
                 ├── [h1] ──┐
  [x2] ─────────┤           ├── [h3] ──── [y] (prediction)
                 ├── [h2] ──┘
  [x3] ─────────┘

Each connection has a WEIGHT that is adjusted during training.
Training uses BACKPROPAGATION to minimize prediction errors.
```

- **Input layer** — Receives raw data
- **Hidden layers** — Transform data through weighted connections (the "deep" in deep learning = many hidden layers)
- **Output layer** — Produces predictions (one neuron for regression, one per class for classification)
- **Activation functions** — Add non-linearity (ReLU, sigmoid, softmax)
- **Backpropagation** — Algorithm that adjusts weights to minimize errors

### Types of Inferencing

| Type | How It Works | Latency | Use Case | AWS Example |
|------|-------------|---------|----------|-------------|
| **Real-time** | Immediate response per request | Milliseconds | Chatbots, fraud detection, recommendations | SageMaker real-time endpoints, Bedrock InvokeModel |
| **Batch** | Process large dataset at once | Minutes-hours | Nightly scoring, bulk predictions, periodic reports | SageMaker Batch Transform, Bedrock batch inference |
| **Asynchronous** | Submit request, retrieve result later | Seconds-minutes | Video processing, large document analysis | SageMaker Async Inference |
| **Serverless** | Auto-scales, no infrastructure management | Variable (cold start possible) | Variable/unpredictable workloads | SageMaker Serverless Inference, Lambda |

### Types of Data in AI Models

| Data Type | Description | Example | ML Approach |
|-----------|-------------|---------|-------------|
| **Labeled** | Data with known outcomes/tags | Emails marked "spam"/"not spam" | Supervised learning |
| **Unlabeled** | Raw data without tags | Millions of web pages | Unsupervised or self-supervised |
| **Structured** | Organized in rows/columns with schema | Database tables, CSV files | Traditional ML, tabular models |
| **Unstructured** | No predefined format | Text, images, audio, video | Deep learning, FMs |
| **Semi-structured** | Some organization but flexible | JSON, XML, logs | Varies |
| **Tabular** | Rows and columns | Spreadsheets, SQL results | XGBoost, Random Forest |
| **Time-series** | Sequential data points over time | Stock prices, IoT sensor readings | Forecasting models |
| **Image** | Pixel-based visual data | Photos, X-rays, satellite images | CNNs, Vision models |
| **Text** | Natural language | Documents, emails, reviews | NLP, LLMs |

### Types of ML Learning (The Three Paradigms)

#### Supervised Learning
**Signal:** Labeled input-output pairs  
**Goal:** Learn to predict outputs for new inputs

| Task | Description | Algorithm Examples | AWS Service |
|------|-------------|-------------------|-------------|
| **Classification** | Predict category | Decision Trees, Random Forest, XGBoost, Neural Networks, SVM | SageMaker (built-in XGBoost) |
| **Regression** | Predict continuous value | Linear Regression, XGBoost, Neural Networks | SageMaker |

**Real examples:** Spam detection, image recognition, price prediction, churn prediction, fraud detection

#### Unsupervised Learning
**Signal:** Unlabeled data only  
**Goal:** Find hidden patterns/structure

| Task | Description | Algorithm Examples | Use Case |
|------|-------------|-------------------|----------|
| **Clustering** | Group similar items | K-Means, DBSCAN, Hierarchical | Customer segmentation |
| **Dimensionality Reduction** | Reduce features while preserving information | PCA, t-SNE | Data visualization, feature reduction |
| **Anomaly Detection** | Find outliers | Isolation Forest, Autoencoders | Fraud detection, system failures |
| **Association** | Find co-occurrence rules | Apriori | Market basket analysis |

#### Reinforcement Learning (RL)
**Signal:** Reward/punishment from environment  
**Goal:** Learn optimal action strategy (policy) to maximize cumulative reward

**Key concepts:**
- **Agent** — The learner/decision-maker
- **Environment** — What the agent interacts with
- **State** — Current situation
- **Action** — What the agent does
- **Reward** — Feedback signal (positive or negative)
- **Policy** — Strategy mapping states to actions

**Use cases:** Robotics, game playing, dynamic pricing, resource allocation  
**AWS Example:** AWS DeepRacer (autonomous racing)

#### Self-Supervised Learning (bonus — know this exists)
**Signal:** Training signal derived FROM the data itself (masking words, predicting next token)  
**Why it matters:** This is how LLMs and foundation models are pre-trained on massive unlabeled data  
**Example:** GPT predicts the next word; BERT fills in masked words

---

## 1.2 Practical Use Cases for AI

### When AI/ML Provides Value
- Automating repetitive tasks at scale
- Assisting (not replacing) human decision-making
- Processing volumes of data beyond human capacity
- Finding subtle patterns in complex data
- Personalizing experiences for millions of users simultaneously
- Making predictions from historical data

### When AI/ML is NOT Appropriate
- When a **deterministic outcome** is needed (not a probability)
- When **cost exceeds benefit** (small dataset, simple problem)
- When **insufficient or poor-quality data** exists
- When a **simple rule-based system** works just as well
- When **full explainability is legally required** and the model can't provide it
- When **ethical/legal risks** outweigh benefits

### ML Techniques Mapped to Use Cases

| Business Need | ML Technique | Type | Example |
|--------------|-------------|------|---------|
| "How much will X cost?" | **Regression** | Supervised | House price prediction |
| "Is this spam or not?" | **Classification** | Supervised | Email filtering |
| "Group similar customers" | **Clustering** | Unsupervised | Customer segments |
| "Is this transaction suspicious?" | **Anomaly Detection** | Unsupervised | Fraud detection |
| "What should we recommend?" | **Recommendation** | Various | Product suggestions |
| "What will demand be next month?" | **Forecasting** | Supervised (time-series) | Inventory planning |

### Real-World AI Applications → AWS Services

| Application | Description | Primary AWS Service |
|------------|-------------|-------------------|
| Computer Vision | Analyze images/video | **Amazon Rekognition** |
| NLP / Text Analysis | Sentiment, entities, language | **Amazon Comprehend** |
| Speech-to-Text | Transcribe audio | **Amazon Transcribe** |
| Text-to-Speech | Generate spoken audio | **Amazon Polly** |
| Language Translation | Translate between languages | **Amazon Translate** |
| Conversational AI / Chatbots | Natural language dialog | **Amazon Lex** |
| Document Processing / OCR | Extract text from documents | **Amazon Textract** |
| Personalization | Real-time recommendations | **Amazon Personalize** |
| Enterprise Search | Intelligent document search | **Amazon Kendra** |
| Forecasting | Time-series prediction | **Amazon SageMaker** (Canvas/AutoML) |
| GenAI Applications | Text/code/image generation | **Amazon Bedrock** |
| Knowledge-based Q&A | RAG over proprietary data | **Bedrock Knowledge Bases** |
| Agentic Workflows | Autonomous multi-step tasks | **Bedrock Agents, Strands Agents** |
| AI Code Assistant | Code generation/explanation | **Amazon Q Developer** |

### Traditional ML vs Foundation Models — When to Choose

| Factor | Choose Traditional ML | Choose Foundation Models |
|--------|----------------------|------------------------|
| **Data type** | Structured/tabular data | Unstructured (text, images, audio) |
| **Explainability** | Need full model interpretability | Can accept less transparency |
| **Regulatory** | Strict audit requirements | Flexible requirements |
| **Task** | Specific, well-defined (predict churn) | Open-ended, flexible (summarize, generate) |
| **Data available** | Good labeled dataset for your task | Limited task-specific data |
| **Latency** | Need sub-ms predictions | Can accept ~100ms-seconds |
| **Cost** | Predictable, lower per-prediction | Token-based, can be higher |

---

## 1.3 The AI/ML Development Lifecycle

### ML Pipeline Components

```
┌─────────────┐   ┌──────────────┐   ┌─────────────────┐   ┌──────────────┐
│ 1. Data      │──▶│ 2. Data      │──▶│ 3. Feature      │──▶│ 4. Model     │
│ Collection   │   │ Preparation  │   │ Engineering     │   │ Training     │
└─────────────┘   └──────────────┘   └─────────────────┘   └──────────────┘
                                                                    │
┌─────────────┐   ┌──────────────┐   ┌─────────────────┐          ▼
│ 7. Model     │◀──│ 6. Model     │◀──│ 5. Model        │◀─────────┘
│ Monitoring   │   │ Deployment   │   │ Evaluation      │
└─────────────┘   └──────────────┘   └─────────────────┘
        │
        ▼
┌─────────────┐
│ 8. Retrain  │ (Loop back to step 1 or 4)
└─────────────┘
```

### AWS Services for Each Pipeline Stage

| Stage | Purpose | AWS Services |
|-------|---------|-------------|
| Data Collection & Storage | Gather and store raw data | **S3**, Glue, Lake Formation, Data Exchange |
| Data Preparation | Clean, transform, label | **SageMaker Data Wrangler**, Glue DataBrew |
| Feature Engineering | Create useful input features | **SageMaker Feature Store** |
| Model Training | Train/fine-tune models | **SageMaker AI**, Bedrock (fine-tuning) |
| Model Evaluation | Assess performance and bias | **SageMaker Clarify**, Bedrock Model Evaluation |
| Model Deployment | Serve predictions | **SageMaker Endpoints**, Bedrock API |
| Monitoring | Watch for degradation | **SageMaker Model Monitor**, CloudWatch |
| Orchestration/MLOps | Automate pipelines | **SageMaker Pipelines**, Amazon Q, Kiro |

### Sources of Foundation Models
- **Open-source pre-trained models** — Llama, Mistral (available via SageMaker JumpStart)
- **Commercial FM providers** — Anthropic Claude, Cohere (available via Amazon Bedrock)
- **AWS-built models** — Amazon Titan, Amazon Nova (native to Bedrock)
- **Training custom models** — From scratch using SageMaker AI (expensive, requires massive data)

### Methods to Use Models in Production
- **Managed API service** — Amazon Bedrock (serverless, no infrastructure)
- **Self-hosted API** — SageMaker Endpoints (more control, more responsibility)
- **Embedded in application** — Lambda + Bedrock API calls

### MLOps Fundamentals

| Concept | Description | Why It Matters |
|---------|-------------|---------------|
| **Experimentation** | Track parameters, metrics, artifacts across experiments | Reproduce and compare results |
| **Repeatable Processes** | Automated, version-controlled pipelines | Eliminate manual errors |
| **Scalable Systems** | Infrastructure that grows with demand | Handle production load |
| **Technical Debt** | Accumulated maintenance burden | ML systems degrade silently |
| **Production Readiness** | Testing, validation, canary deployments | Prevent bad model releases |
| **Model Monitoring** | Continuous performance tracking | Detect drift before users notice |
| **Model Re-training** | Update models with fresh data | Keep predictions accurate over time |

### Performance Metrics

#### Model Metrics

| Metric | Formula | Best For | Remember |
|--------|---------|----------|----------|
| **Accuracy** | Correct / Total | Balanced classes | Misleading with imbalanced data |
| **Precision** | TP / (TP + FP) | "How many predicted positives are correct?" | Minimize false positives |
| **Recall (Sensitivity)** | TP / (TP + FN) | "How many actual positives were found?" | Minimize false negatives |
| **F1 Score** | 2 × (P × R) / (P + R) | Balance precision and recall | Harmonic mean |
| **AUC-ROC** | Area under ROC curve | Model's overall discriminative ability | 1.0 = perfect, 0.5 = random |

**Exam scenario tip:**
- High **Precision** needed → Minimize false alarms (spam filter: don't block legit emails)
- High **Recall** needed → Don't miss positives (cancer detection: catch every case)
- **F1** → When both matter equally

#### Business Metrics
- Cost per user / Cost per prediction
- Development costs and time-to-market
- Customer feedback and satisfaction scores
- Return on Investment (ROI)
- Revenue impact / conversion rate

---

# PART 2: DOMAIN 2 — Fundamentals of Generative AI (24%)

## 2.1 Basic GenAI Concepts

### Essential GenAI Vocabulary

| Term | Definition | Why It Matters |
|------|-----------|---------------|
| **Token** | Smallest unit of text processed by an LLM (word, subword, or character) | Billing, context limits, and performance all measured in tokens |
| **Tokenization** | Process of splitting text into tokens | "unhappiness" → ["un", "happiness"] |
| **Context Window** | Maximum number of tokens a model can process at once | Determines how much info model can "see" |
| **Chunking** | Breaking large documents into smaller pieces for processing | Critical for RAG systems |
| **Embedding** | Dense numerical vector that captures semantic meaning | "king" and "queen" have similar embeddings |
| **Vector** | Array of numbers representing data in multi-dimensional space | The mathematical form of embeddings |
| **Vector Store/Database** | Specialized DB for storing and searching embeddings efficiently | Core of RAG architecture |
| **Prompt** | Text input given to a model | Your instruction + context |
| **Completion** | Model's generated output response | What the model returns |
| **Hallucination** | Model generates plausible but factually incorrect information | Major risk of GenAI |
| **Temperature** | Parameter controlling output randomness | 0 = deterministic, 1 = creative |
| **Top-p** | Nucleus sampling; controls diversity of word choices | Lower = more focused |
| **RLHF** | Reinforcement Learning from Human Feedback | Aligns model outputs with human preferences |
| **Foundation Model (FM)** | Large model pre-trained on broad data, adaptable to many tasks | Base that you customize |
| **Multi-modal Model** | Processes multiple data types (text + image + audio + video) | Amazon Nova, GPT-4o |
| **Diffusion Model** | Generates images by learning to reverse a noise process | Stable Diffusion, DALL-E |

### How Transformers Work (the architecture behind LLMs)

```
INPUT TEXT: "The cat sat on the"
      │
      ▼
┌─────────────────────────────┐
│  1. TOKENIZATION            │  "The" "cat" "sat" "on" "the"
└─────────────────────────────┘
      │
      ▼
┌─────────────────────────────┐
│  2. TOKEN EMBEDDINGS        │  Each token → dense vector (e.g., 768 dimensions)
└─────────────────────────────┘
      │
      ▼
┌─────────────────────────────┐
│  3. POSITIONAL ENCODING     │  Add position info (token 1, token 2, etc.)
└─────────────────────────────┘  (Transformers have no inherent sequence awareness)
      │
      ▼
┌─────────────────────────────────────────────────────────────┐
│  4. SELF-ATTENTION (Multi-Head)                              │
│                                                              │
│  For each token, compute:                                    │
│  • Query (Q): "What am I looking for?"                       │
│  • Key (K): "What do I contain?"                             │
│  • Value (V): "What information do I provide?"               │
│                                                              │
│  Attention = softmax(Q·K^T / √d) × V                        │
│                                                              │
│  Multiple "heads" capture different relationship types       │
│  (syntax, semantics, long-range dependencies)                │
└─────────────────────────────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────┐
│  5. FEED-FORWARD NETWORK    │  Further transform each token's representation
└─────────────────────────────┘
      │
      ▼
┌─────────────────────────────┐
│  6. OUTPUT / NEXT TOKEN     │  Predict probability distribution over vocabulary
└─────────────────────────────┘  → "mat" (highest probability) → output "mat"
```

**Key insight for exam:** Self-attention lets each token "attend to" every other token, capturing context regardless of distance. This is what makes transformers superior to older architectures (RNNs) for language tasks.

### Embeddings Explained

Embeddings convert discrete items (words, sentences, documents) into continuous vectors where **semantic similarity = geometric proximity**.

```
Vector Space Visualization:

    "king" ──── [0.9, 0.1, 0.8, ...]
    "queen" ─── [0.85, 0.15, 0.82, ...]   (close to king!)
    "apple" ─── [0.1, 0.9, 0.2, ...]      (far from king)

Famous relationship: king - man + woman ≈ queen
```

**Why embeddings matter for the exam:**
- RAG systems use embeddings to find semantically similar documents
- Vector databases store and search embeddings efficiently
- The quality of embeddings affects RAG retrieval quality
- AWS services for embedding: Amazon Titan Embeddings, Amazon Bedrock

### GenAI Use Cases

| Category | Examples |
|----------|---------|
| Text Generation | Summarization, content creation, email drafting |
| Code Generation | Write, debug, explain, translate code |
| Image Generation | Create images from text descriptions |
| Video Generation | Generate video clips from prompts |
| Audio Generation | Text-to-speech, music creation |
| AI Assistants | Customer service, internal knowledge Q&A |
| Translation | Real-time multilingual communication |
| Search | Semantic search over documents |
| Recommendation | Personalized content suggestions |

### Foundation Model Lifecycle

```
Data Selection → Model Architecture → Pre-training → Fine-tuning → Evaluation → Deployment → Feedback
```

1. **Data Selection** — Choose massive, diverse, high-quality training corpus
2. **Model Architecture** — Transformer, size (parameters), modalities
3. **Pre-training** — Self-supervised learning on massive data (predict next token)
4. **Fine-tuning** — Adapt to specific tasks with smaller labeled datasets
5. **Evaluation** — Benchmark tests, human evaluation, safety testing
6. **Deployment** — Serve via API endpoints
7. **Feedback** — RLHF, user feedback, continuous improvement

### Token-Based Pricing Model

| Factor | Impact on Cost |
|--------|---------------|
| **Input tokens** (your prompt) | Billed per 1K or 1M tokens |
| **Output tokens** (model response) | Usually more expensive than input |
| **Model size/capability** | Larger/newer models cost more per token |
| **On-demand vs Provisioned** | Provisioned = committed throughput at discount |

**Exam tip:** Longer prompts = more input tokens = higher cost. Longer responses = more output tokens = higher cost. Choosing a smaller model that's "good enough" saves money.

**Approximate token counts:** 1 token ≈ 4 characters ≈ 0.75 words in English

### Context Engineering

Context engineering is the discipline of selecting, structuring, and managing the information provided to a model to maximize output quality while respecting context window limits.

**Strategies:**
- Summarize long documents before including
- Use chunking to break documents into relevant pieces
- RAG to dynamically retrieve only relevant context
- Memory management in multi-turn conversations
- System prompts for persistent instructions

### Agentic AI Concepts (NEW in exam v1.1 — important!)

| Concept | Definition | Exam Context |
|---------|-----------|--------------|
| **AI Agent** | System that autonomously plans, reasons, and executes tasks | Bedrock Agents, Strands Agents |
| **Multi-Agent System** | Multiple agents collaborating on complex tasks | Supervisor-worker, peer-to-peer patterns |
| **Model Context Protocol (MCP)** | Open standard for connecting agents to external tools/data | Typed, schema-validated tool interfaces |
| **Agent-to-Agent (A2A)** | Protocol for agent discovery and collaboration | Agents publish "agent cards" describing capabilities |
| **Memory Management** | How agents maintain state across interactions | Short-term (conversation) and long-term (persistent) |
| **Tool Usage** | Agents calling external APIs, DBs, or services | Extends agent capabilities beyond text generation |
| **Workflow Orchestration** | Coordinating multi-step agent processes | Pipeline, supervisor-worker, swarm patterns |

**Multi-Agent Patterns:**
- **Supervisor-Worker:** One agent delegates subtasks to specialized agents
- **Peer-to-Peer:** Agents collaborate as equals
- **Pipeline:** Sequential hand-off between agents
- **Swarm:** Dynamic collaboration based on need

**AWS Services for Agentic AI:**
- **Amazon Bedrock Agents** — Managed agent service with action groups and knowledge bases
- **Strands Agents** — Open-source SDK for building agents (Python & TypeScript)
- **Amazon Bedrock AgentCore** — Production infrastructure for deploying agents (memory, identity, observability)
- **Kiro** — AI-powered development environment

---

## 2.2 Capabilities and Limitations of GenAI

### Advantages of GenAI

| Advantage | Description |
|-----------|-------------|
| **Adaptability** | Single model handles many tasks without retraining |
| **Responsiveness** | Interactive, conversational interactions |
| **Conversational** | Natural language interface — no coding needed |
| **Content Generation** | Creates text, code, images, audio at scale |
| **Efficiency** | Automates tasks that took humans hours |
| **Accessibility** | Lowers barrier to AI capabilities |

### Limitations/Disadvantages of GenAI

| Limitation | Description | Mitigation |
|-----------|-------------|-----------|
| **Hallucinations** | Generates confident but false information | RAG grounding, Guardrails, citations |
| **Nondeterminism** | Same input → different outputs each time | Lower temperature, set seed |
| **Inaccuracy** | May produce factually wrong content | Validation, human review |
| **Interpretability** | Can't fully explain reasoning | Chain-of-thought prompting |
| **Bias** | Reflects biases in training data | SageMaker Clarify, diverse data |
| **Knowledge Cutoff** | Training data has a fixed date | RAG for current information |
| **Context Limits** | Can't process unlimited text | Chunking, summarization |
| **Cost** | Token-based pricing can escalate | Prompt optimization, caching |

### Factors for Selecting GenAI Models

| Factor | Considerations |
|--------|---------------|
| Model type | Text-only, multi-modal, code-specialized |
| Performance | Speed vs quality tradeoff |
| Capabilities | Task-specific strengths |
| Constraints | Context window, language support |
| Compliance | Data residency, industry regulations |
| Cost | Token pricing, volume discounts |
| Latency | Response time requirements |
| Model complexity | Larger ≠ always better for your task |

### Business Value Metrics for GenAI

| Metric | What It Measures |
|--------|-----------------|
| Cross-domain performance | How well model adapts across different use cases |
| ROI | Revenue generated vs cost of AI system |
| Efficiency gains | Time saved vs previous process |
| Conversion rate | Sales/signups improvement |
| Average revenue per user | Revenue impact of personalization |
| Accuracy | Correctness of generated outputs |
| Customer lifetime value | Long-term customer relationship impact |

---

## 2.3 AWS Infrastructure for GenAI

### AWS GenAI Services Tier Model

```
┌──────────────────────────────────────────────────────────────────────┐
│ TIER 1: PRE-TRAINED AI APIs (no ML expertise needed)                 │
│ Rekognition | Textract | Comprehend | Polly | Transcribe |           │
│ Translate | Lex | Personalize | Kendra                               │
├──────────────────────────────────────────────────────────────────────┤
│ TIER 2: FOUNDATION MODEL PLATFORMS (customize without training)      │
│ Amazon Bedrock | Amazon Q | Amazon Nova | Kiro | Strands Agents      │
├──────────────────────────────────────────────────────────────────────┤
│ TIER 3: CUSTOM ML INFRASTRUCTURE (full control)                      │
│ Amazon SageMaker AI | SageMaker JumpStart                            │
└──────────────────────────────────────────────────────────────────────┘
```

### Amazon Bedrock — Complete Feature Breakdown

| Feature | Purpose | Exam Relevance |
|---------|---------|---------------|
| **Model Access** | Single API to access FMs from multiple providers | Choose models without lock-in |
| **Knowledge Bases** | Managed RAG workflow (ingest, chunk, embed, retrieve) | RAG questions point here |
| **Agents** | Multi-step task orchestration with tools | Agentic AI questions |
| **Guardrails** | Safety policies (content filters, PII, hallucination) | Security + Responsible AI |
| **Fine-tuning** | Customize model weights with labeled data | When RAG isn't enough |
| **Continued Pre-training** | Adapt model with unlabeled domain data | Deep domain knowledge |
| **Model Evaluation** | Compare and assess model performance | Choosing the right model |
| **Prompt Management** | Version, manage, and test prompts | Prompt engineering at scale |
| **Custom Model Import** | Bring your own models into Bedrock | Flexibility |
| **Model Distillation** | Create smaller, faster models from larger ones | Cost optimization |
| **AgentCore** | Production infrastructure for agents | Enterprise agent deployment |

**Models available in Bedrock:** Anthropic Claude, Meta Llama, Mistral, Cohere, AI21, Stability AI, Amazon Titan, Amazon Nova

### Amazon SageMaker AI — Complete Feature Breakdown

| Feature | Purpose |
|---------|---------|
| **SageMaker Studio** | Integrated development environment for ML |
| **SageMaker JumpStart** | Pre-built models and solutions hub |
| **Data Wrangler** | Visual data preparation and transformation |
| **Feature Store** | Centralized feature repository |
| **Training** | Managed training jobs (GPU/CPU clusters) |
| **Autopilot** | AutoML — automatically builds models |
| **Clarify** | Bias detection + SHAP explainability |
| **Model Monitor** | Drift detection in production |
| **Model Cards** | Documentation of model details |
| **Endpoints** | Managed model serving infrastructure |
| **Pipelines** | CI/CD for ML workflows |
| **Canvas** | No-code ML for business users |

### Advantages of AWS GenAI Services

| Advantage | Description |
|-----------|-------------|
| Accessibility | API-based, no infrastructure to manage |
| Lower barrier to entry | No ML expertise needed for Bedrock |
| Efficiency | Pre-built capabilities save development time |
| Cost-effectiveness | Pay-per-use, no upfront infrastructure |
| Speed to market | Build GenAI apps in hours/days |
| Security | IAM, encryption, VPC, compliance built-in |
| Compliance | Region-based, meets regulatory standards |

### Cost Tradeoffs of AWS GenAI Services

| Factor | Tradeoff |
|--------|---------|
| On-demand vs Provisioned Throughput | Flexibility vs cost savings |
| Token-based vs committed pricing | Variable vs predictable costs |
| Smaller vs larger models | Cost vs capability |
| Regional availability | Not all models in all regions |
| Custom models | Higher cost but better task performance |
| Prompt caching | Save cost on repeated context |

---

# PART 3: DOMAIN 3 — Applications of Foundation Models (28%)

> This is the LARGEST domain. Master this thoroughly.

## 3.1 Design Considerations for FM Applications

### FM Selection Criteria

| Criterion | What to Consider |
|-----------|-----------------|
| **Cost** | Token pricing, provisioned throughput discounts |
| **Modality** | Text-only vs multi-modal (text + image + audio) |
| **Latency** | Response time requirements for your use case |
| **Multi-lingual** | Number of languages supported |
| **Model Size** | Larger = more capable but slower and costlier |
| **Model Complexity** | More parameters ≠ always better for your task |
| **Customization** | Fine-tuning availability, RAG support |
| **Input/Output Length** | Context window limits |
| **Prompt Caching** | Save cost for repeated context/system prompts |

### Inference Parameters (CRITICAL for exam!)

| Parameter | What It Controls | Low Value | High Value |
|-----------|-----------------|-----------|------------|
| **Temperature** | Randomness of output | Deterministic, focused, repetitive | Creative, diverse, unpredictable |
| **Top-p (Nucleus Sampling)** | Diversity of word choices | Considers fewer word options | Considers more word options |
| **Max Tokens** | Maximum response length | Short responses | Long responses |
| **Top-k** | Number of top candidates considered | More focused | More diverse |
| **Stop Sequences** | When to stop generating | N/A | N/A |

**The critical rule to memorize:**
- **Low temperature + Low top-p** = Deterministic, factual, consistent output (use for: code, data extraction, factual Q&A)
- **High temperature + High top-p** = Creative, varied output (use for: creative writing, brainstorming)

**Common exam scenario:** "A company needs consistent, factual responses from their customer service bot" → Set LOW temperature

### Retrieval Augmented Generation (RAG) — Deep Dive

```
┌──────────────┐         ┌──────────────────────┐
│  USER QUERY  │────────▶│ 1. EMBED QUERY       │
└──────────────┘         │    (convert to vector)│
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ 2. VECTOR SEARCH      │
                         │    (find similar docs)│
                         │    in Vector Database │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ 3. AUGMENT PROMPT     │
                         │    (add retrieved     │
                         │     context to prompt)│
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ 4. GENERATE RESPONSE  │
                         │    (FM generates      │
                         │     grounded answer)  │
                         └──────────────────────┘
```

**RAG Benefits:**
- Reduces hallucinations (grounded in real data)
- No model retraining needed
- Uses up-to-date information
- Provides source citations
- Cost-effective (vs fine-tuning)
- Fast to deploy

**RAG Limitations:**
- Adds latency (retrieval step)
- Quality depends on chunking strategy and embedding quality
- Doesn't work well for full-document summarization
- Can't change model's writing style or behavior

**AWS Service:** Amazon Bedrock Knowledge Bases (fully managed RAG)

### Vector Databases on AWS

| Service | Type | Best For |
|---------|------|----------|
| **Amazon OpenSearch Service** | Search engine + vector | Full-text + semantic search combined |
| **Amazon Aurora (PostgreSQL + pgvector)** | Relational + vector | When you already use Aurora |
| **Amazon Neptune** | Graph + vector | Knowledge graphs with semantic search |
| **Amazon RDS for PostgreSQL** | Relational + vector | Simple vector storage with pgvector |

### FM Customization Approaches — Complete Comparison

| Approach | What Changes | Cost | Speed | Data Needed | Best For | AWS Service |
|----------|-------------|------|-------|-------------|----------|-------------|
| **In-context Learning** | Nothing (prompt only) | Lowest | Instant | None | Simple task adaptation | Bedrock (prompts) |
| **RAG** | Nothing (retrieves external data) | Low | Fast to set up | Documents | Current/dynamic knowledge | Bedrock Knowledge Bases |
| **Model Distillation** | Creates smaller model | Medium | Hours | Large model's outputs | Smaller, faster model | Bedrock Distillation |
| **Fine-tuning** | Model weights (small subset) | High | Hours-days | Labeled Q&A pairs | Task-specific behavior, style | Bedrock Fine-tuning |
| **Continued Pre-training** | Model weights (deeper) | Very High | Days | Unlabeled domain text | Deep domain knowledge | Bedrock Continued Pre-training |
| **Pre-training from scratch** | Everything | Extreme | Weeks-months | Massive corpus | Entirely new model | SageMaker AI |

**The Decision Framework (memorize this!):**

```
Need current/dynamic information? → RAG
Need consistent style/format/tone? → Fine-tuning
Need deep domain vocabulary? → Continued Pre-training
Need smaller/faster model? → Distillation
Need quick experiment? → In-context learning (prompt engineering)
Need maximum quality + current data? → Fine-tuning + RAG (hybrid)
```

**Key analogy:**
- **RAG** = Giving an employee a reference manual (external knowledge)
- **Fine-tuning** = Sending an employee to a training course (changes behavior)
- **Continued Pre-training** = Employee gets a PhD in the domain (deep knowledge)

### Role of AI Agents

**What agents do:**
- Break complex tasks into subtasks
- Plan execution steps
- Use tools (APIs, databases, search engines)
- Remember context across interactions
- Make decisions autonomously

**Business applications:**
- Customer service automation (lookup orders, process refunds)
- Research and analysis (multi-source synthesis)
- Workflow automation (booking, scheduling, approvals)
- Code development (plan, write, test, deploy)

**AWS Services:** Amazon Bedrock Agents, Strands Agents, Bedrock AgentCore

---

## 3.2 Prompt Engineering Techniques

### Prompt Anatomy

```
┌─────────────────────────────────────────────────────────┐
│ SYSTEM PROMPT (role, behavior, constraints)              │
│ "You are a helpful medical assistant. Never give         │
│  diagnoses. Always recommend consulting a doctor."       │
├─────────────────────────────────────────────────────────┤
│ CONTEXT (background information)                         │
│ "Patient medical history: [retrieved documents]"         │
├─────────────────────────────────────────────────────────┤
│ INSTRUCTION (what to do)                                 │
│ "Summarize the key findings in 3 bullet points."        │
├─────────────────────────────────────────────────────────┤
│ INPUT (data to process)                                  │
│ "Lab report: Cholesterol 240, HDL 35, LDL 180..."       │
├─────────────────────────────────────────────────────────┤
│ OUTPUT FORMAT (how to structure response)                 │
│ "Format as: Finding | Significance | Recommendation"    │
├─────────────────────────────────────────────────────────┤
│ NEGATIVE PROMPTS (what to avoid)                         │
│ "Do NOT provide specific drug recommendations."         │
└─────────────────────────────────────────────────────────┘
```

### Prompting Techniques — Detailed

#### Zero-Shot Prompting
No examples provided. Relies entirely on model's pre-training.

```
Prompt: "Classify the sentiment of this review as positive, negative, or neutral:
'The product arrived late but the quality was excellent.'"

Output: "Mixed/Neutral"
```

**When to use:** Simple, well-defined tasks the model already knows how to do.

#### One-Shot (Single-Shot) Prompting
One example provided to demonstrate expected behavior.

```
Prompt: "Classify sentiment:
Review: 'Amazing product, fast shipping!' → Positive
Review: 'The product arrived late but quality was excellent.' → "

Output: "Positive"
```

#### Few-Shot Prompting
Multiple examples (typically 3-5) to establish a pattern.

```
Prompt: "Classify sentiment:
'Love it!' → Positive
'Terrible experience' → Negative  
'It was okay' → Neutral
'The product arrived late but quality was excellent.' → "

Output: "Positive"
```

**When to use:** Need consistent formatting, domain-specific tasks, model making errors with zero-shot.  
**Tradeoff:** More tokens = higher cost and latency.

#### Chain-of-Thought (CoT) Prompting
Instruct model to explain reasoning step by step.

```
Prompt: "A store has 50 books. They sell 15 and receive 7 more. How many do they have?
Think step by step."

Output: "Start: 50 books. Sold 15: 50 - 15 = 35. Received 7: 35 + 7 = 42. Answer: 42"
```

**When to use:** Math, logic, multi-step reasoning problems.  
**Key phrase:** "Think step by step" or "Let's work through this..."

#### Prompt Templates
Reusable structures with placeholders for variable content.

```
Template: "You are a {ROLE}. Given the following {CONTEXT}, 
please {TASK}. Format your response as {FORMAT}."
```

**AWS Service:** Amazon Bedrock Prompt Management (version, test, and deploy templates)

### Best Practices for Prompt Engineering
1. **Be specific and concise** — Precise instructions get better results
2. **Provide clear instructions** — Don't assume the model knows what you want
3. **Use examples** when output format matters
4. **Experiment and iterate** — Test multiple approaches
5. **Set guardrails in prompts** — "Only answer based on the provided context"
6. **Use delimiters** — XML tags or markers to separate sections
7. **Specify output format** — JSON, bullet points, table, etc.
8. **Include negative prompts** — "Do NOT include..." or "Never..."

### Prompt Engineering Risks and Limitations

| Risk | Description | Mitigation |
|------|-------------|-----------|
| **Prompt Injection** | Malicious input overrides system instructions ("Ignore all previous instructions...") | Input validation, Bedrock Guardrails, XML delimiters |
| **Prompt Leakage (Exposure)** | Model reveals hidden system prompts or instructions | Don't put secrets in prompts; use Guardrails |
| **Prompt Poisoning** | Malicious data in retrieval sources causes harmful outputs | Validate retrieved content, content filtering |
| **Prompt Hijacking** | Redirecting model to unintended tasks | Strict role definitions, Guardrails |
| **Jailbreaking** | Bypassing safety guardrails | Multiple layers of defense, Bedrock Guardrails |
| **Data Exposure** | Extracting sensitive training data from model | Guardrails, access controls |

### Amazon Bedrock Prompt Management
- **Version control** — Track changes to prompts over time
- **A/B testing** — Compare different prompt versions
- **Centralized storage** — Single source of truth for all prompts
- **Performance tracking** — Monitor which prompts perform best
- **Collaboration** — Teams can share and iterate on prompts

---

## 3.3 Training and Fine-tuning Foundation Models

### Training Methods Compared

| Method | What Happens | Data Type | Cost | Duration | Result |
|--------|-------------|-----------|------|----------|--------|
| **Pre-training** | Train model from scratch | Massive unlabeled corpus | $Millions | Weeks-months | Base FM |
| **Continued Pre-training** | Extend existing model's knowledge | Unlabeled domain text | $Thousands | Days | Domain-adapted FM |
| **Fine-tuning** | Adjust weights for specific task | Labeled input-output pairs | $Hundreds-Thousands | Hours-days | Task-specific FM |
| **Instruction Tuning** | Teach model to follow instructions | Instruction-response pairs | $Hundreds | Hours | Better instruction-following |
| **RLHF** | Align with human preferences | Human preference rankings | $Thousands | Days | Aligned FM |
| **Distillation** | Train small model to mimic large | Large model's outputs | $Hundreds | Hours | Smaller, faster FM |
| **Transfer Learning** | Apply learned knowledge to new task | Small task-specific dataset | Low | Hours | Adapted model |

### Data Preparation for Fine-tuning

| Requirement | Description |
|-------------|-------------|
| **Data curation** | Clean, relevant, high-quality examples |
| **Governance** | Compliance with data policies, privacy regulations |
| **Size** | Enough examples (typically hundreds to thousands) |
| **Labeling** | Accurate input-output pairs |
| **Representativeness** | Cover the diversity of expected inputs |
| **Format** | JSON lines with prompt-completion pairs (Bedrock format) |
| **Balance** | Avoid over-representing one class/type |
| **RLHF** | Optional human preference data for alignment |

### Fine-tuning on Amazon Bedrock

**Available for:** Amazon Titan, Amazon Nova, Llama, Cohere Command  
**Process:**
1. Prepare labeled data in JSONL format in S3
2. Choose base model
3. Configure hyperparameters (epochs, learning rate, batch size)
4. Bedrock creates a PRIVATE copy of the model
5. Your data is NOT used to train the base model
6. Fine-tuned model accessible only to your account

---

## 3.4 Evaluating FM Performance

### Evaluation Approaches

| Approach | Description | When to Use |
|----------|-------------|-------------|
| **Automatic Evaluation** | Computed metrics (ROUGE, BLEU, etc.) | Quick comparison, quantitative benchmarks |
| **Human-in-the-Loop** | Human reviewers assess quality | Subjective quality, safety, brand voice |
| **Benchmark Datasets** | Standardized test sets | Compare against published results |
| **LLM-as-a-Judge** | Another model evaluates outputs | Scale evaluation without humans |
| **Amazon Bedrock Model Evaluation** | AWS managed evaluation service | Compare models for your use case |

### Key Evaluation Metrics — MUST KNOW

#### ROUGE (Recall-Oriented Understudy for Gisting Evaluation)
**Best for:** Summarization  
**Measures:** How much of the reference summary is captured in the generated summary (RECALL-focused)

| Variant | What It Compares |
|---------|-----------------|
| ROUGE-1 | Unigram (individual word) overlap |
| ROUGE-2 | Bigram (two-word phrase) overlap |
| ROUGE-L | Longest Common Subsequence |

**Example:**
- Reference: "The cat sat on the mat"
- Generated: "The cat is on the mat"  
- ROUGE-1 = 5/6 = 0.83 (5 of 6 reference words appear)

#### BLEU (Bilingual Evaluation Understudy)
**Best for:** Machine Translation  
**Measures:** How many n-grams in the generated text appear in the reference (PRECISION-focused)

**Example:**
- Reference: "The cat is on the mat"
- Generated: "There is a cat on the mat"
- BLEU measures what fraction of generated n-grams match reference

#### BERTScore
**Best for:** Any text comparison where paraphrasing is valid  
**Measures:** Semantic similarity using contextual embeddings (captures MEANING, not just words)

**Key advantage:** "The feline rested on the rug" would score HIGH against "The cat sat on the mat" because embeddings capture semantic similarity, unlike ROUGE/BLEU which only match exact words.

#### LLM-as-a-Judge
**Best for:** Open-ended generation, style, helpfulness, safety  
**How it works:** A capable LLM (e.g., Claude) evaluates another model's output against criteria

**Advantages:** Scales better than human evaluation, captures nuance  
**Risks:** Position bias, verbosity bias, self-preference bias

#### Perplexity
**Best for:** Comparing language model quality (internal metric)  
**Measures:** How "surprised" the model is by the next token  
**Lower = better** (model is less surprised = better predictions)

### Summary: Which Metric for Which Task

| Task | Primary Metric | Secondary |
|------|---------------|-----------|
| **Summarization** | ROUGE-1, ROUGE-2, ROUGE-L | BERTScore |
| **Translation** | BLEU | BERTScore |
| **Text Generation (general)** | BERTScore | LLM-as-a-Judge |
| **Open-ended Q&A** | LLM-as-a-Judge | Human eval |
| **Chatbot quality** | LLM-as-a-Judge | Human eval |
| **Model comparison** | Perplexity | Benchmark scores |
| **RAG accuracy** | Faithfulness (grounding) | Relevance |

### Business Alignment Metrics

| Metric | What It Measures |
|--------|-----------------|
| Task completion rate | % of tasks successfully completed by AI |
| User satisfaction | User ratings/feedback on AI responses |
| Cost per interaction | Total cost divided by number of interactions |
| Productivity improvement | Time saved vs manual process |
| User engagement | Frequency and depth of AI usage |

### Evaluating RAG, Agents, and Workflows
- **RAG evaluation:** Faithfulness (is answer grounded?), Relevance (is retrieved context useful?), Answer correctness
- **Agent evaluation:** Task completion rate, tool usage accuracy, number of steps taken
- **Workflow evaluation:** End-to-end success rate, latency, cost per completion

---

# PART 4: DOMAIN 4 — Guidelines for Responsible AI (14%)

## 4.1 Developing Responsible AI Systems

### Six Pillars of Responsible AI

| Pillar | Definition | Example |
|--------|-----------|---------|
| **Bias** | Systematic unfairness in predictions | Model denies loans more to certain demographics |
| **Fairness** | Equal treatment across all groups | Equal approval rates across genders |
| **Inclusivity** | Representing diverse perspectives | Training data includes all languages/cultures |
| **Robustness** | Reliable under various conditions | Model handles adversarial inputs gracefully |
| **Safety** | Preventing harmful outputs/actions | Model refuses to generate dangerous content |
| **Veracity** | Truthfulness and factual accuracy | Model doesn't hallucinate |

### Legal Risks of GenAI

| Risk | Description | Example |
|------|-------------|---------|
| **IP Infringement** | Generated content may reproduce copyrighted material | Model outputs verbatim book passages |
| **Biased Outputs** | Model discriminates against protected groups | Hiring tool favors one gender |
| **Loss of Trust** | Customers lose confidence in AI-powered services | Chatbot gives wrong medical info |
| **End User Risk** | Harm to users from incorrect/harmful outputs | Financial advice causes losses |
| **Hallucinations** | Plausible but false information presented as fact | Citing non-existent legal cases |

### Responsible Model Selection Practices
- **Environmental considerations** — Larger models = more energy = higher carbon footprint
- **Sustainability** — Choose smallest model that meets quality requirements
- **Appropriateness** — Don't use FM when simple ML suffices
- **Licensing** — Understand model license terms (commercial use, attribution)

### Dataset Characteristics for Responsible AI

| Characteristic | What It Means | Why It Matters |
|---------------|--------------|---------------|
| **Inclusivity** | Represents diverse populations | Prevents bias against underrepresented groups |
| **Diversity** | Covers various scenarios, edge cases | Model handles real-world variety |
| **Curated Sources** | High-quality, verified data | Reduces noise and misinformation |
| **Balanced** | No over/under-representation | Prevents skewed predictions |

### Bias and Variance — Effects

| Issue | Technical Meaning | Real-World Impact |
|-------|------------------|-------------------|
| **High Bias (Underfitting)** | Model too simple, misses patterns | Wrong predictions for everyone |
| **High Variance (Overfitting)** | Model memorizes training data | Great on training data, terrible on new data |
| **Demographic Bias** | Different performance across groups | Discrimination, legal liability |
| **Selection Bias** | Training data not representative | Model only works for some populations |
| **Measurement Bias** | Flawed data collection methods | Systematically wrong predictions |

### AWS Tools for Detecting and Monitoring Bias

#### Amazon SageMaker Clarify
**Purpose:** Bias detection + Model explainability  
**When to use:** BEFORE and AFTER training

| Capability | What It Does |
|-----------|-------------|
| **Pre-training bias detection** | Analyzes dataset for imbalances BEFORE training |
| **Post-training bias detection** | Measures if trained model discriminates |
| **SHAP values** | Shows which features most influenced each prediction |
| **Feature importance** | Ranks which inputs matter most |
| **Bias metrics** | Class Imbalance (CI), Difference in Proportions of Labels (DPL), Demographic Parity |

**Exam tip:** If the question mentions "detect bias" or "explain predictions" → SageMaker Clarify

#### Amazon SageMaker Model Monitor
**Purpose:** Continuous production monitoring for drift  
**When to use:** AFTER deployment, ongoing

| Monitor Type | What It Detects |
|-------------|----------------|
| **Data Quality Drift** | Are inputs changing from training distribution? |
| **Model Quality Drift** | Are predictions getting worse? |
| **Bias Drift** | Is fairness degrading over time? |
| **Feature Attribution Drift** | Are important features changing? |

**Exam tip:** If the question mentions "model degrading over time" or "drift" → SageMaker Model Monitor

#### Amazon Augmented AI (Amazon A2I)
**Purpose:** Human review of low-confidence ML predictions  
**When to use:** When human oversight is needed for edge cases

**How it works:**
1. ML model makes prediction
2. If confidence < threshold, routes to human reviewer
3. Human confirms, corrects, or overrides
4. Results feed back for model improvement

**Exam tip:** If the question mentions "human review" or "human-in-the-loop" → Amazon A2I

#### Amazon Bedrock Guardrails
**Purpose:** Content safety, PII protection, hallucination detection for GenAI  
**When to use:** Any GenAI application

**Six safeguard policies:**
1. **Content Filters** — Block hate, insults, sexual, violence, misconduct content
2. **Denied Topics** — Block specific subjects (e.g., "no investment advice")
3. **Word Filters** — Block specific words/phrases
4. **Sensitive Information (PII)** — Detect and mask/block PII (SSN, email, phone)
5. **Contextual Grounding** — Detect hallucinations by checking against source
6. **Automated Reasoning** — Mathematical/logical verification of accuracy

**Exam tip:** If the question mentions "filter harmful content in GenAI" or "PII redaction" → Bedrock Guardrails

---

## 4.2 Transparent and Explainable Models

### Transparent vs Non-Transparent Models

| Aspect | Transparent/Explainable | Non-Transparent (Black Box) |
|--------|------------------------|----------------------------|
| **Decision process** | Can be understood and audited | Cannot easily explain decisions |
| **Examples** | Linear regression, Decision trees, Rule-based | Deep neural networks, LLMs |
| **Auditability** | Easy to audit for compliance | Requires additional tooling |
| **Trust level** | Higher inherent trust | Requires trust-building measures |
| **Performance** | Often lower (simpler models) | Often higher (complex models) |
| **Regulatory fit** | Meets explainability requirements | May need supplementary explanations |

### Tools for Transparency and Explainability

| Tool | What It Provides |
|------|-----------------|
| **SageMaker Model Cards** | Structured documentation: model purpose, limitations, performance, intended use, ethical considerations |
| **SageMaker Clarify** | SHAP values for feature importance; explains WHY a prediction was made |
| **Bedrock Model Evaluations** | Assessment of model quality, safety, and behavior across scenarios |
| **Open Source Models** | Inspectable architecture, weights, and training data |
| **Model Licensing** | Understanding terms of use and limitations |

### Tradeoffs: Safety vs Transparency

| Tradeoff | Description |
|---------|-------------|
| Interpretability vs Performance | More interpretable models (linear regression) often less performant than black-box models (deep learning) |
| Safety vs Capability | Adding safety constraints may reduce model's creative/helpful output |
| Complexity vs Auditability | Simpler models easier to audit but may not handle complex tasks |
| Regulation vs Innovation | Strict explainability requirements may limit use of best-performing models |

### Human-Centered Design for Explainable AI

| Principle | Implementation |
|-----------|---------------|
| **User feedback mechanisms** | Thumbs up/down, detailed feedback forms, report incorrect answers |
| **AI decision transparency** | Show confidence scores, explain reasoning, cite sources |
| **Clear limitation communication** | "I'm an AI and may be wrong" disclaimers |
| **Human override capabilities** | Allow users to correct or override AI decisions |
| **Gradual trust building** | Start with low-risk tasks, prove reliability before high-stakes |
| **Appropriate calibration** | Don't express certainty when uncertain |

---

# PART 5: DOMAIN 5 — Security, Compliance, and Governance (14%)

## 5.1 Securing AI Systems

### AWS Security Services for AI — Complete Reference

| Service | Purpose | AI-Specific Use |
|---------|---------|----------------|
| **IAM** | Identity and access management | Control who can invoke models, access training data, deploy endpoints |
| **AWS KMS** | Key Management Service — encryption keys | Encrypt model artifacts, training data, inference data at rest |
| **Amazon Macie** | Discover and protect sensitive data | Find PII in S3 buckets used for training |
| **AWS PrivateLink** | Private connectivity without internet | Access Bedrock/SageMaker without exposing to public internet |
| **Amazon Bedrock Guardrails** | Content filtering + PII redaction | Protect GenAI inputs/outputs |
| **Bedrock AgentCore Identity** | Identity for AI agents | Agents authenticate to external services securely |
| **AWS Secrets Manager** | Secure credential storage | Store API keys agents need |
| **Amazon VPC** | Virtual Private Cloud isolation | Isolate AI workloads from public internet |

### AWS Shared Responsibility Model for AI

```
┌────────────────────────────────────────────────────────┐
│  CUSTOMER RESPONSIBILITY (Security IN the Cloud)        │
│                                                         │
│  • Data classification and protection                   │
│  • IAM policies and access controls                     │
│  • Model input/output filtering                         │
│  • Application-level security                           │
│  • Prompt engineering security                          │
│  • Training data quality and privacy                    │
│  • Compliance with regulations                          │
│  • Monitoring and logging                               │
├────────────────────────────────────────────────────────┤
│  AWS RESPONSIBILITY (Security OF the Cloud)             │
│                                                         │
│  • Physical infrastructure security                     │
│  • Network infrastructure                               │
│  • Hypervisor and host OS                               │
│  • Service availability                                 │
│  • Hardware and compute isolation                       │
│  • Encryption in transit between AWS services           │
└────────────────────────────────────────────────────────┘
```

### Source Citation and Data Lineage

| Concept | Description | AWS Tool |
|---------|-------------|----------|
| **Data Lineage** | Track data from origin through all transformations | AWS Glue Data Catalog, Lake Formation |
| **Data Cataloging** | Maintain inventory of all data assets | AWS Glue Data Catalog |
| **Model Provenance** | Document where a model came from and how it was trained | SageMaker Model Cards |
| **Source Citation** | AI responses reference their information sources | Bedrock Knowledge Bases (built-in citations) |

### Secure Data Engineering Best Practices

| Practice | Description |
|----------|-------------|
| **Assess data quality** | Validate completeness, accuracy, consistency before training |
| **Privacy-enhancing technologies** | Anonymization, pseudonymization, differential privacy |
| **Data access control** | Least privilege — minimum access needed for each role |
| **Data integrity** | Checksums, versioning, immutable audit logs |
| **Encryption at rest** | KMS encryption for S3, EBS, databases |
| **Encryption in transit** | TLS/SSL for all data movement |
| **Data classification** | Label data by sensitivity (public, internal, confidential, restricted) |

### Security and Privacy Threats for AI Systems

| Threat | Description | Mitigation |
|--------|-------------|-----------|
| **Prompt Injection** | Malicious input overrides system instructions | Input validation, Bedrock Guardrails, XML delimiters, separate user/system inputs |
| **Data Leakage** | Sensitive training data exposed through outputs | Access controls, output filtering, PII masking |
| **Model Theft** | Unauthorized access to model weights/parameters | IAM policies, VPC isolation, encryption |
| **Adversarial Attacks** | Inputs designed to fool the model | Input validation, robustness testing |
| **Toxicity** | Model generates harmful/offensive content | Content filters, Bedrock Guardrails |
| **Output Manipulation** | Crafted inputs produce dangerous outputs | Output validation, confidence scoring |
| **Infrastructure Attacks** | Targeting the compute/network layer | VPC, Security Groups, WAF |
| **Supply Chain Attacks** | Compromised pre-trained models or datasets | Verify sources, scan for backdoors |

**Exam-specific security considerations:**
- **Audit trail and logging** — CloudTrail for API calls, Bedrock invocation logging
- **Data leakage prevention** — Macie for PII, Guardrails for output filtering
- **Output filtering and validation** — Guardrails content filters + contextual grounding
- **Encryption at rest** — KMS managed keys
- **Encryption in transit** — TLS 1.2+ for all API calls

### Hallucination Detection and Grounding Techniques

| Technique | How It Works | AWS Implementation |
|-----------|-------------|-------------------|
| **RAG Grounding** | Anchor responses to retrieved factual documents | Bedrock Knowledge Bases |
| **Contextual Grounding Check** | Verify response is supported by provided context | Bedrock Guardrails |
| **Automated Reasoning** | Mathematical/logical rules validate accuracy | Bedrock Guardrails (99% accuracy) |
| **Output Validation** | Check outputs against known facts or rules | Custom validation logic |
| **Confidence Scoring** | Measure model's certainty in its response | Model-specific APIs |
| **Source Citation** | Require model to cite sources for claims | Bedrock Knowledge Bases |

---

## 5.2 Governance and Compliance

### AWS Governance and Compliance Services

| Service | Purpose | AI Use Case |
|---------|---------|-------------|
| **AWS CloudTrail** | Log ALL API activity | Track who invoked which model, when, with what data |
| **Amazon CloudWatch** | Metrics, logs, alarms | Monitor model latency, error rates, token usage |
| **AWS Config** | Track resource configurations + compliance rules | Ensure AI resources meet compliance standards |
| **Amazon Inspector** | Automated vulnerability scanning | Scan containers/EC2 running ML workloads |
| **AWS Audit Manager** | Continuous audit evidence collection | Generate compliance reports automatically |
| **AWS Artifact** | Access AWS compliance reports (SOC, ISO, etc.) | Prove AWS infrastructure is compliant |
| **AWS Trusted Advisor** | Best practice recommendations | Security, cost, performance checks |

### Regulatory Compliance Standards

| Standard | Description | Relevance to AI |
|----------|-------------|----------------|
| **ISO 27001** | Information security management | Securing AI data and systems |
| **SOC 1** | Financial reporting controls | AI in financial processes |
| **SOC 2** | Security, availability, processing integrity | AI system trustworthiness |
| **SOC 3** | Public-facing SOC 2 summary | Customer-facing AI compliance |
| **GDPR** | EU data protection regulation | Personal data in AI training/inference |
| **HIPAA** | US healthcare data protection | AI processing health information |
| **Algorithm accountability laws** | Regulations requiring AI transparency | Explainability of AI decisions |

### Data Governance Strategies

| Strategy | Description | Implementation |
|----------|-------------|---------------|
| **Data Lifecycle** | Policies for creation, use, storage, archival, deletion | Define retention periods, deletion rules |
| **Logging** | Record all data access, modifications, and usage | CloudTrail, CloudWatch Logs |
| **Data Residency** | Keep data in required geographic regions | Region-specific S3 buckets, regional services |
| **Monitoring** | Continuous oversight of data usage | CloudWatch dashboards, alerts |
| **Observation** | Track data flow through systems | Data lineage tools, Glue Catalog |
| **Retention** | Rules for how long data is kept | S3 lifecycle policies, Glacier |

### Governance Processes

| Process | Description |
|---------|-------------|
| **Policies** | Written rules for AI development and use |
| **Review Cadence** | Regular scheduled reviews of AI systems |
| **Review Strategies** | How to assess AI system behavior and compliance |
| **Governance Frameworks** | Structured approach (e.g., Generative AI Security Scoping Matrix) |
| **Transparency Standards** | Requirements for documenting AI capabilities and limitations |
| **Team Training** | Ensuring staff understand responsible AI practices |

### Bedrock Model Invocation Logging
- Captures full prompt and response payloads
- Logs to CloudWatch Logs or S3
- Enables audit trail for all AI interactions
- Essential for compliance and debugging

---

# PART 6: In-Scope AWS Services — Complete Reference

## Machine Learning Services (Primary Focus)

### Amazon Bedrock
**What:** Fully managed service for accessing foundation models via API  
**Key features:** Model access, Knowledge Bases (RAG), Agents, Guardrails, Fine-tuning, Evaluation, Prompt Management  
**When to choose:** Building GenAI applications without managing infrastructure  
**Pricing:** Per-token (on-demand) or Provisioned Throughput

### Amazon SageMaker AI
**What:** End-to-end platform for building, training, deploying custom ML models  
**Key features:** Studio, Data Wrangler, Feature Store, Training, Autopilot, Clarify, Model Monitor, Model Cards, Endpoints, Pipelines  
**When to choose:** Custom models, full control over ML lifecycle  
**Pricing:** Per instance-hour for training and inference

### Amazon SageMaker JumpStart
**What:** Hub of pre-built models and solutions  
**When to choose:** Quick start with open-source models (Llama, Mistral) on your own infrastructure

### Amazon Comprehend
**What:** NLP service for text analysis  
**Capabilities:** Sentiment analysis, entity extraction, key phrases, language detection, PII detection, custom classification, topic modeling  
**When to choose:** Need to analyze text without building models

### Amazon Rekognition
**What:** Computer vision service  
**Capabilities:** Face detection/analysis, object detection, text in images, content moderation, celebrity recognition, custom labels  
**When to choose:** Image/video analysis without building CV models

### Amazon Textract
**What:** Document processing / intelligent OCR  
**Capabilities:** Extract text, tables, forms from scanned documents; handle handwriting  
**When to choose:** Invoice processing, ID verification, form digitization

### Amazon Transcribe
**What:** Speech-to-text  
**Capabilities:** Real-time and batch transcription, speaker diarization, custom vocabulary, medical transcription, call analytics  
**When to choose:** Converting audio/video to text

### Amazon Polly
**What:** Text-to-speech  
**Capabilities:** 60+ lifelike voices, Neural TTS, SSML support, custom lexicons  
**When to choose:** Voice interfaces, accessibility, content narration

### Amazon Translate
**What:** Neural machine translation  
**Capabilities:** 75+ languages, real-time and batch, custom terminology  
**When to choose:** Multilingual content, localization

### Amazon Lex
**What:** Conversational AI / chatbot builder  
**Capabilities:** Natural language understanding (NLU), automatic speech recognition (ASR), multi-turn dialog  
**When to choose:** Building chatbots, IVR systems, voice interfaces

### Amazon Personalize
**What:** Real-time recommendations  
**Capabilities:** Product recommendations, content personalization, user segmentation, search re-ranking  
**When to choose:** E-commerce, content platforms, personalized experiences

### Amazon Kendra
**What:** Intelligent enterprise search  
**Capabilities:** Natural language queries over documents, FAQ extraction, ML-powered ranking  
**When to choose:** Internal document search, knowledge management

### Amazon Augmented AI (A2I)
**What:** Human review workflows for ML predictions  
**When to choose:** Need human oversight for low-confidence predictions

### Amazon Nova
**What:** Amazon's own family of foundation models  
**Variants:** Nova Micro (text-only, fastest), Nova Lite (multimodal, cost-effective), Nova Pro (multimodal, balanced), Nova Premier (most capable)

### Amazon Bedrock AgentCore
**What:** Production infrastructure for AI agents  
**Capabilities:** Memory management, identity, observability, gateway for tool integration  
**When to choose:** Deploying production-grade agents at scale

## Developer Tools

### Amazon Q
**What:** AI-powered assistant for business and development  
**Variants:** Q Developer (coding), Q Business (enterprise knowledge)

### Kiro
**What:** AI-powered development environment  
**When to choose:** AI-assisted software development

### Strands Agents
**What:** Open-source SDK for building AI agents (Python & TypeScript)  
**When to choose:** Building custom multi-agent systems with MCP support

## Analytics Services

| Service | Purpose |
|---------|---------|
| **AWS Glue** | ETL (Extract, Transform, Load) and Data Catalog |
| **AWS Glue DataBrew** | Visual data preparation |
| **AWS Lake Formation** | Data lake creation and governance |
| **Amazon OpenSearch Service** | Search + vector database |
| **Amazon Redshift** | Data warehouse |
| **Amazon EMR** | Big data processing (Spark, Hadoop) |
| **AWS Data Exchange** | Find and subscribe to third-party data |
| **Amazon Quick** | Business intelligence with AI |

## Database Services (Vector Storage)

| Service | Vector Capability |
|---------|------------------|
| **Amazon Aurora** | pgvector extension for PostgreSQL |
| **Amazon Neptune** | Graph + vector search |
| **Amazon RDS** | pgvector with PostgreSQL |
| **Amazon DynamoDB** | Key-value store (not vector-native, but used for agent memory) |
| **Amazon DocumentDB** | MongoDB-compatible |
| **Amazon ElastiCache** | In-memory caching |

## Security Services

| Service | Purpose |
|---------|---------|
| **AWS IAM** | Access control (roles, policies, permissions) |
| **AWS KMS** | Encryption key management |
| **Amazon Macie** | PII discovery in S3 |
| **AWS Secrets Manager** | Secure credential storage |
| **Amazon Inspector** | Vulnerability scanning |
| **AWS Audit Manager** | Compliance evidence collection |
| **AWS Artifact** | AWS compliance reports |

## Management & Governance

| Service | Purpose |
|---------|---------|
| **AWS CloudTrail** | API activity logging |
| **Amazon CloudWatch** | Metrics, logs, alarms |
| **AWS Config** | Configuration compliance |
| **AWS Trusted Advisor** | Best practice checks |
| **AWS Well-Architected Tool** | Architecture review |

## Compute & Infrastructure

| Service | Purpose |
|---------|---------|
| **Amazon EC2** | Virtual servers (for self-managed ML) |
| **AWS Lambda** | Serverless compute |
| **Amazon ECS** | Container orchestration |
| **Amazon EKS** | Kubernetes |
| **Amazon S3** | Object storage (training data, model artifacts) |
| **Amazon S3 Glacier** | Archive storage |
| **Amazon CloudFront** | CDN |
| **Amazon VPC** | Network isolation |

---

# PART 7: Key Decision Frameworks (Exam Scenarios)

## Framework 1: Choosing Between Services

| Scenario | Answer |
|----------|--------|
| "Build GenAI app without managing infrastructure" | **Amazon Bedrock** |
| "Need full control over ML model training" | **Amazon SageMaker AI** |
| "Quick access to open-source models" | **SageMaker JumpStart** |
| "Analyze text sentiment" | **Amazon Comprehend** |
| "Analyze images/video" | **Amazon Rekognition** |
| "Extract text from documents" | **Amazon Textract** |
| "Convert speech to text" | **Amazon Transcribe** |
| "Convert text to speech" | **Amazon Polly** |
| "Translate languages" | **Amazon Translate** |
| "Build chatbot" | **Amazon Lex** |
| "Product recommendations" | **Amazon Personalize** |
| "Enterprise document search" | **Amazon Kendra** |
| "Human review of ML predictions" | **Amazon A2I** |
| "Detect bias in model" | **SageMaker Clarify** |
| "Monitor model drift" | **SageMaker Model Monitor** |
| "Filter harmful GenAI content" | **Bedrock Guardrails** |
| "Build AI agents" | **Bedrock Agents or Strands Agents** |
| "Manage production agents" | **Bedrock AgentCore** |

## Framework 2: Choosing Customization Approach

| Scenario | Answer |
|----------|--------|
| "Need answers from company documents" | **RAG (Bedrock Knowledge Bases)** |
| "Model uses wrong terminology for our industry" | **Fine-tuning** |
| "Need deep medical/legal domain knowledge" | **Continued Pre-training** |
| "Quick experiment, no infrastructure changes" | **Prompt engineering (in-context learning)** |
| "Need faster, cheaper version of large model" | **Model Distillation** |
| "Data changes frequently" | **RAG** (no retraining needed) |
| "Need consistent response format" | **Fine-tuning** |
| "Want to combine style + current data" | **Fine-tuning + RAG (hybrid)** |

## Framework 3: Choosing Evaluation Metric

| Task | Metric |
|------|--------|
| "Evaluate summary quality" | **ROUGE** |
| "Evaluate translation quality" | **BLEU** |
| "Evaluate semantic similarity" | **BERTScore** |
| "Evaluate open-ended generation" | **LLM-as-a-Judge** |
| "Evaluate classification" | **Accuracy, Precision, Recall, F1** |
| "Compare model versions internally" | **Perplexity** |

## Framework 4: Security and Compliance

| Scenario | Answer |
|----------|--------|
| "Track who invoked AI models" | **CloudTrail** |
| "Monitor AI system performance" | **CloudWatch** |
| "Ensure AI resources meet compliance rules" | **AWS Config** |
| "Get AWS compliance certificates" | **AWS Artifact** |
| "Automate audit evidence" | **Audit Manager** |
| "Protect PII in AI data" | **Macie** (discovery) + **Guardrails** (runtime) |
| "Encrypt training data" | **KMS** |
| "Private access to Bedrock" | **PrivateLink** |
| "Detect vulnerabilities in ML infrastructure" | **Inspector** |

---

# PART 8: Glossary of Must-Know Terms

| Term | Definition |
|------|-----------|
| **Accuracy** | Ratio of correct predictions to total predictions |
| **Agent** | AI system that autonomously plans and executes tasks |
| **Algorithm** | Step-by-step procedure for computation |
| **Attention Mechanism** | Allows model to focus on relevant parts of input |
| **AUC-ROC** | Area Under ROC Curve; overall model discrimination ability |
| **Backpropagation** | Algorithm to train neural networks by adjusting weights |
| **Batch Inference** | Processing many inputs at once |
| **BERTScore** | Semantic similarity metric using contextual embeddings |
| **Bias (ML)** | Systematic error in predictions |
| **Bias (Statistical)** | Model's tendency to underfit |
| **BLEU** | Bilingual Evaluation Understudy — translation metric |
| **Chain-of-Thought** | Prompting technique for step-by-step reasoning |
| **Chunking** | Splitting large text into smaller pieces |
| **Classification** | Predicting categories |
| **Clustering** | Grouping similar items (unsupervised) |
| **CNN** | Convolutional Neural Network — for images |
| **Context Window** | Max tokens a model can process |
| **Continuous Pre-training** | Extend model knowledge with domain data |
| **Data Drift** | When production data differs from training data |
| **Deep Learning** | ML using multi-layer neural networks |
| **Diffusion Model** | Generates images by reversing noise |
| **Dimensionality Reduction** | Reducing features while preserving info |
| **Distillation** | Training smaller model to mimic larger one |
| **Embedding** | Dense vector capturing semantic meaning |
| **Epoch** | One complete pass through training data |
| **F1 Score** | Harmonic mean of precision and recall |
| **Feature** | Input variable to a model |
| **Few-Shot** | Prompting with multiple examples |
| **Fine-tuning** | Adapting pre-trained model weights |
| **Foundation Model** | Large model pre-trained on broad data |
| **GAN** | Generative Adversarial Network |
| **Gradient Descent** | Optimization algorithm for training |
| **Guardrails** | Safety policies for AI systems |
| **Hallucination** | Model generates plausible but false information |
| **Hyperparameter** | Setting configured before training (learning rate, epochs) |
| **In-context Learning** | Teaching model via the prompt (no weight changes) |
| **Inference** | Using trained model for predictions |
| **Instruction Tuning** | Fine-tuning with instruction-response pairs |
| **LLM** | Large Language Model |
| **LLM-as-a-Judge** | Using one LLM to evaluate another's output |
| **LoRA** | Low-Rank Adaptation — efficient fine-tuning method |
| **MCP** | Model Context Protocol — standard for agent-tool connection |
| **MLOps** | DevOps practices for ML systems |
| **Model Drift** | Degradation of model performance over time |
| **Multi-modal** | Processing multiple data types |
| **Neural Network** | Computing system of interconnected nodes |
| **NLP** | Natural Language Processing |
| **Overfitting** | Model memorizes training data |
| **Parameter** | Learned value in model (weights) |
| **Perplexity** | How well model predicts next token (lower = better) |
| **PII** | Personally Identifiable Information |
| **Positional Encoding** | Information about token position in sequence |
| **Precision** | TP / (TP + FP) |
| **Pre-training** | Initial training on massive data |
| **Prompt** | Input text given to a model |
| **Prompt Engineering** | Crafting inputs for optimal outputs |
| **Prompt Injection** | Malicious input overriding instructions |
| **RAG** | Retrieval Augmented Generation |
| **Recall** | TP / (TP + FN) |
| **Regression** | Predicting continuous values |
| **Reinforcement Learning** | Learning through reward/punishment |
| **RLHF** | Reinforcement Learning from Human Feedback |
| **RNN** | Recurrent Neural Network — for sequences |
| **ROUGE** | Recall-oriented summarization metric |
| **Self-attention** | Each token attends to all others |
| **Self-supervised** | Training signal from data itself |
| **SHAP** | SHapley Additive exPlanations — feature importance |
| **Supervised Learning** | Learning from labeled data |
| **Temperature** | Controls output randomness |
| **Token** | Smallest unit processed by LLM |
| **Top-p** | Nucleus sampling parameter |
| **Transfer Learning** | Applying learned knowledge to new task |
| **Transformer** | Architecture using self-attention (basis of LLMs) |
| **Underfitting** | Model too simple, misses patterns |
| **Unsupervised Learning** | Learning from unlabeled data |
| **Variance** | Model's sensitivity to training data |
| **Vector** | Array of numbers in multi-dimensional space |
| **Vector Database** | DB optimized for similarity search on vectors |
| **Zero-Shot** | Prompting with no examples |

---

# PART 9: Study Resources & Exam Strategy

## Recommended Study Plan (4 weeks, ~8 hrs/week)

| Week | Focus | Activities |
|------|-------|-----------|
| **1** | Domain 1 + Start Domain 2 | Vocabulary, ML types, AI services overview |
| **2** | Domain 2 + Start Domain 3 | GenAI concepts, Bedrock deep dive, RAG vs fine-tuning |
| **3** | Domain 3 + Domain 4 | Prompt engineering, evaluation metrics, responsible AI |
| **4** | Domain 5 + Full review + Practice exams | Security, governance, timed practice, review weak areas |

## Free Resources
- [AWS Skill Builder Exam Prep Standard Course](https://explore.skillbuilder.aws/) (~14 hours)
- [Official Practice Question Set](https://explore.skillbuilder.aws/) — 20 free questions
- [AWS Exam Guide PDF](https://d1.awsstatic.com/training-and-certification/docs-ai-practitioner/AWS-Certified-AI-Practitioner_Exam-Guide.pdf)
- YouTube: Stéphane Maarek, Andrew Brown — full free courses
- [Amazon Bedrock Workshops](https://workshops.aws)
- [AWS Well-Architected ML Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html)

## Paid Resources
- Stéphane Maarek AIF-C01 (Udemy, ~$15)
- Tutorials Dojo Practice Tests
- AWS Skill Builder Subscription ($29/month) — Enhanced Exam Prep

## Exam Day Strategy

1. **First pass (60 min):** Answer everything you know confidently (~60 seconds each)
2. **Flag uncertain questions** — Come back to them
3. **Second pass (30 min):** Review flagged questions carefully
4. **Always answer everything** — Zero penalty for guessing
5. **Elimination technique** — Remove 2 obviously wrong answers, choose from remaining
6. **Watch for absolutes** — "Always" and "never" are usually wrong
7. **AWS-native answers win** — When in doubt, choose the AWS managed service
8. **"Least operational overhead"** = managed/serverless service
9. **"Most cost-effective"** = right-sized or serverless option
10. **Read all options** — The "best" answer may not be the "only correct" one

## Common Exam Traps

| Trap | How to Avoid |
|------|-------------|
| Confusing SageMaker Clarify (bias) with Model Monitor (drift) | Clarify = analysis; Monitor = ongoing surveillance |
| Confusing RAG with Fine-tuning | RAG = current data, no retraining; Fine-tuning = changes weights |
| Temperature confusion | LOW = deterministic; HIGH = creative |
| ROUGE vs BLEU | ROUGE = summarization (recall); BLEU = translation (precision) |
| Bedrock vs SageMaker | Bedrock = use FMs; SageMaker = build your own |
| Guardrails vs Clarify | Guardrails = GenAI safety; Clarify = ML bias/explainability |
| Comprehend vs Textract | Comprehend = understand text; Textract = extract from images/docs |
| Transcribe vs Translate | Transcribe = speech→text; Translate = language→language |
| A2I vs Guardrails | A2I = human review of predictions; Guardrails = automated content safety |

---

*This guide covers every topic, task statement, and objective in the official AWS Certified AI Practitioner (AIF-C01) Exam Guide v1.1 (April 2026). Good luck!*
