# AWS Certified AI Practitioner Practice Test Summary

Use this as a fast review guide for the topics repeatedly tested across the practice tests. The exam questions are mostly scenario based, so focus on recognizing the keywords that point to each AWS service, ML concept, model technique, or metric.

## Quick Exam Strategy

- If the question says **least operational effort**, choose a managed AWS service instead of building, training, or coding a custom solution.
- If the question says **company data changes often**, choose **RAG / Amazon Bedrock Knowledge Bases**, not fine-tuning.
- If the question says **company tone, domain style, labeled examples, or specific output behavior**, choose **prompt engineering** first for low cost, or **fine-tuning** when examples must be learned into the model.
- If the question says **filter harmful content, PII, denied topics, or prompt injection with least effort**, choose **Amazon Bedrock Guardrails**.
- If the question says **bias, explainability, feature influence, or model predictions**, choose **Amazon SageMaker Clarify**.
- If the question says **document model purpose, intended use, training details, limitations, or audit record**, choose **SageMaker Model Cards**.
- If the question says **drift, quality degradation, production monitoring**, choose **SageMaker Model Monitor**.
- If the question says **vector search, embeddings, nearest neighbor, semantic search**, choose **Amazon OpenSearch Service** or **Aurora PostgreSQL with pgvector**.
- If the question says **private access without public internet**, choose **AWS PrivateLink / VPC endpoints**.
- If the question asks about **API access logs**, choose **AWS CloudTrail**.
- If the question asks for **AWS compliance reports**, choose **AWS Artifact**.

## Core AI, ML, and Generative AI Concepts

### AI vs ML vs Deep Learning

- **AI** is the broad field of machines performing intelligent tasks.
- **ML** is a subset of AI where systems learn patterns from data.
- **Deep learning** is a subset of ML that uses neural networks with many layers.
- **Foundation models (FMs)** are large pre-trained models that can be adapted to many tasks.
- **Generative AI** creates new content such as text, images, code, summaries, translations, audio, or video.
- **Discriminative models** classify or predict; **generative models** create new content.

### Common Model Types

- **Transformer models**: Best for text generation, summarization, code generation, question answering, and coherent language output. They use self-attention to understand context.
- **Diffusion models**: Best for image generation.
- **GANs**: Generate synthetic data based on existing data.
- **BERT-based models**: Good for understanding context and filling in missing words.
- **Decision trees**: Easy to explain and interpret.
- **Logistic regression**: Interpretable binary classification; weights can be viewed and adjusted.
- **K-nearest neighbors (k-NN)**: Supervised classification based on similar nearby examples.
- **K-means**: Unsupervised clustering, often for customer grouping.
- **Autoencoders**: Unsupervised anomaly detection, especially when labels are unavailable.
- **Regression**: Predicts numeric values.
- **Binary classification**: Two classes, such as fraud or not fraud.
- **Multi-class classification**: More than two classes.

### Learning Types

- **Supervised learning**: Uses labeled data with known outputs. Use for classification, regression, image labels, churn prediction, disease prediction, and fraud/non-fraud prediction.
- **Unsupervised learning**: Uses unlabeled data. Use for clustering, customer segmentation, dimensionality reduction, and finding groups.
- **Reinforcement learning**: Learns from interactions, rewards, and penalties.
- **RLHF**: Reinforcement learning from human feedback.
- **Transfer learning**: Reuses a pre-trained model for a related task.
- **Federated learning**: Trains across private/local datasets without moving raw data; useful for privacy and compliance.

## Generative AI Use Cases

Know these mappings:

- **Summarization**: Legal documents, medication reviews, policy documents, customer complaints, chat transcripts.
- **Text generation**: Product descriptions, code from comments, human-like chatbot responses.
- **Translation**: Manuals, articles, subtitles in other languages.
- **Image generation**: Illustrations, marketing images, story images.
- **Video generation**: Amazon Nova Reel for generated video.
- **Code generation and developer help**: Amazon Q Developer.
- **Conversational assistant over company data**: Amazon Q Business or Bedrock with RAG/Knowledge Bases.
- **Personalized recommendations**: Amazon Personalize.
- **Computer vision**: Image classification, object detection, product defect detection.
- **Speech-to-text**: Amazon Transcribe, or AWS HealthScribe for clinical notes.
- **Text-to-speech**: Amazon Polly.
- **Document text extraction**: Amazon Textract.
- **NLP entity/sentiment/toxicity**: Amazon Comprehend or Amazon Comprehend Medical for medical text.

## Amazon Bedrock

Amazon Bedrock is the central AWS service for building and scaling generative AI applications using foundation models without managing infrastructure.

### Bedrock Features

- **Foundation models**: Use for text, image, multimodal, and other generative tasks.
- **Knowledge Bases for Amazon Bedrock**: Use RAG to connect FMs to private or current data.
- **Agents for Amazon Bedrock**: Use when the assistant must take actions, call APIs, use tools, query systems, orchestrate workflows, or complete multi-step tasks.
- **Guardrails for Amazon Bedrock**: Use to filter unsafe inputs/outputs, denied topics, harmful content, PII, prompt injection risks, child-safe content, hate, violence, and responsible AI controls.
- **Model invocation logging**: Use to log Bedrock model inputs and outputs.
- **Model evaluation**: Use to compare model output quality with automatic evaluation or human workforce evaluation.
- **Provisioned Throughput**: Use for customized Bedrock models or predictable steady traffic.
- **On-Demand Throughput**: Use for low, unpredictable, experimental, or budget-sensitive usage.
- **PartyRock**: Low-cost experimental environment for learning generative AI applications.

### Bedrock Security and Privacy

- Bedrock does **not share user inputs or outputs with third-party model providers**.
- Use **IAM policies** to restrict access to specific Bedrock models.
- Use **least privilege IAM roles and policies** for secure Bedrock applications.
- Use **custom service roles** when teams should access only their own S3/customer data.
- Use **AWS PrivateLink** when Bedrock API traffic must stay off the public internet.
- Use **AWS KMS** for customer-managed encryption keys for model artifacts or data encryption.
- Use **CloudTrail** to track API calls and unauthorized access attempts.
- Use **S3 Intelligent-Tiering** for long-term log retention at lower cost when access patterns are uncertain.

### Bedrock Model Selection

- **Amazon Nova Lite**: Cost-effective multimodal and multilingual model.
- **Nova Canvas**: Image generation.
- **Nova Reel**: Video generation.
- **Nova Pro**: More capable general multimodal use, but not always most cost-effective.
- **Stable Diffusion**: Text-to-image generation.
- Choose model by **modality** when output/input types matter: text, image, video, audio, multimodal.
- Choose model by **context window** when the question asks how much information fits into one prompt.
- Choose model by **inference speed** when real-time user responses are required.

## RAG, Embeddings, and Vector Databases

### Retrieval Augmented Generation

Use **RAG** when the model needs accurate, current, private, or domain-specific data at query time.

Choose RAG for:

- Product manuals stored as PDFs.
- HR or company policies updated frequently.
- Customer support knowledge bases.
- Current inventory data.
- Research papers or internal documents.
- Chatbots that need source-grounded answers.
- Cost-effective improvement without retraining.

RAG is usually better than fine-tuning when facts change often.

### RAG Pipeline Concepts

- **Chunking** splits long documents into smaller meaningful sections so retrieval can return only relevant context.
- **Content embeddings** convert documents/chunks into vectors.
- **Search index creation** stores vectors for retrieval.
- **Query embeddings** are generated at request time for user questions.
- **Retrieval** finds relevant chunks.
- **Generation** uses retrieved context to produce the final answer.
- For near real-time RAG, run content embedding and index creation offline or in batches; query embedding, retrieval, and generation happen online.

### Embeddings and Vector Search

- **Tokens** are units of input/output text processed by a model.
- **Tokenization** breaks text into smaller units.
- **Embeddings** are dense numerical vectors representing words, text, images, or concepts.
- Embeddings enable semantic similarity, recommendations, search, clustering, and RAG.
- **Latent space** represents a model's internal organization of relationships and semantic similarity.
- **Vector databases** store embeddings and support nearest neighbor / similarity search.

AWS services to know:

- **Amazon OpenSearch Service**: Vector database, k-NN, nearest neighbor search, semantic search, RAG support.
- **Amazon Aurora PostgreSQL with pgvector**: Store embeddings with structured relational data and query by vector similarity using SQL.
- **Amazon Kendra**: Enterprise search with natural language understanding and semantic search.

## Prompt Engineering

Prompt engineering is the process of crafting input instructions to guide model output.

### Prompt Techniques

- **Zero-shot prompting**: Give instructions but no examples.
- **One-shot prompting**: Give one example.
- **Few-shot prompting**: Give several examples. Use for intent detection, product descriptions, expected format, and style matching.
- **Chain-of-thought prompting**: Ask for step-by-step reasoning. Use for complex reasoning and numerical problems.
- **Prompt chaining**: Break a complex task into smaller sequential prompts.
- **ReAct prompting**: Combine reasoning with actions/API calls. Use when a chatbot must check real-time inventory or external systems.
- **Negative prompts**: Tell an image model what not to include.
- **Adversarial prompting**: Used to test or defend against prompt injection.
- **Prompt templates**: Standardized reusable prompt structure.
- **Role prompting**: Add a role/persona or audience description, such as explaining based on a user's age range.

### Prompt Design Rules

- Give clear context and instructions.
- Include desired format, tone, language, and length.
- Include examples when helpful.
- Avoid vague prompts.
- Use prompt engineering first when you need low-cost improvement in accuracy, style, tone, or output format.
- Prompt engineering helps but does not guarantee deterministic, always-correct, or fully secure output.

### Prompt Risks

- **Prompt injection**: User manipulates the model's instructions or behavior.
- **Jailbreak**: Attempt to bypass model safety features.
- **Extracting prompt template**: Attack that exposes hidden system instructions.
- **Prompted persona switch**: Attack that changes the assistant's role or behavior.
- Use Bedrock Guardrails, prompt templates, input validation, least privilege, and monitoring to reduce risk.

## Inference Parameters

- **Temperature** controls randomness.
  - Lower temperature = more deterministic, stable, consistent, fewer hallucinations.
  - Temperature 0 = most deterministic.
  - Higher temperature = more creative and diverse.
- **Top K** limits generation to the K most likely next tokens.
- **Top P / nucleus sampling** selects from tokens whose cumulative probability adds up to P.
- **Maximum tokens / generation length** controls output length.
- **Context window** controls how much input can fit in the prompt.
- **Generation steps** affect image detail/refinement. More steps generally means more detailed images.
- **Classifier-free guidance (CFG) scale** controls how closely image generation follows the prompt. Higher CFG means more prompt adherence.
- **Prompt strength** influences how much the prompt guides certain image generation workflows.

## Fine-Tuning, Customization, and Pre-Training

### Choose Fine-Tuning When

- You have labeled examples.
- You need domain terminology or industry-specific behavior.
- You need company tone or style learned from example conversations.
- You need instruction-response behavior, such as question-answer pairs.
- You need to adapt a model to a specific task.

Training data patterns:

- For Bedrock fine-tuning, provide **prompt/completion** or **input/output** pairs.
- For instruction tuning, provide **question/answer** or **instruction/response** pairs.
- For tone/style refinement, provide paired messages and desired outputs.
- Remove PII or confidential data before fine-tuning. If confidential data was used, retrain without it.

### Choose Continued Pre-Training When

- You want an FM to learn broad internal company documents or recent domain data.
- You need to keep the model more current over time.
- The question mentions ongoing pre-training or regular updates to the base model.

### Choose Prompt Engineering When

- You need low-cost, fast improvement.
- You need format, tone, language, length, or examples in output.
- You do not need to change model weights.

### Choose RAG When

- Facts change frequently.
- The model must use private documents.
- You need citations or source-grounded answers.
- You want to avoid fine-tuning cost.

## SageMaker

Amazon SageMaker supports the full ML lifecycle: data preparation, training, tuning, deployment, monitoring, and MLOps.

### Key SageMaker Features

- **SageMaker Canvas**: No-code ML for users with minimal ML/coding knowledge.
- **SageMaker Data Wrangler**: Data preparation and transformation.
- **SageMaker Feature Store**: Central repository to share and reuse ML features/variables across teams.
- **SageMaker Clarify**: Bias detection, explainability, feature influence, SHAP/Shapley values.
- **SageMaker Model Monitor**: Production monitoring for data drift, model drift, quality degradation, and alerts.
- **SageMaker Model Cards**: Standardized documentation of model purpose, intended use, training details, metrics, limitations, and audit records.
- **SageMaker Model Registry**: Store, manage, version, and approve models.
- **SageMaker JumpStart**: Pre-trained models, FMs, built-in algorithms, and quick-start ML solutions.
- **SageMaker Ground Truth**: Data labeling workflows.
- **SageMaker Ground Truth Plus**: Managed labeling workforce and human feedback without managing labelers.
- **SageMaker Autopilot / automatic tuning**: Automated model building or hyperparameter optimization.
- **SageMaker network isolation**: Run training/inference without internet access.

### SageMaker Inference Options

- **Real-time inference**: Low-latency individual predictions, APIs, chatbots, small inputs.
- **Batch transform / batch inference**: Large datasets, scheduled jobs, no immediate response needed, most cost-effective for offline processing.
- **Asynchronous inference**: Large payloads or long processing time, near real-time but not blocking.
- **Serverless inference**: Host predictions without managing infrastructure, good for variable traffic and serverless deployment.

Recognition examples:

- Large monthly data report = **batch transform**.
- Weekend gigabytes of text processing = **batch transform**.
- Chatbot intent detection with minimal latency = **real-time inference**.
- Large input up to 1 GB and processing up to 1 hour with near real-time = **asynchronous inference**.
- Deploy model without managing infrastructure = **SageMaker Serverless Inference** or **SageMaker endpoint**, depending on wording.

## AWS AI Services

Know what each managed AI service does:

- **Amazon Bedrock**: Build generative AI apps with FMs.
- **Amazon Q Developer**: Coding assistant, code snippets, test cases, documentation, AWS service help.
- **Amazon Q Business**: Enterprise AI assistant over internal company data.
- **Amazon Q in QuickSight**: Natural language BI, dashboards, graphs, and visual analytics.
- **Amazon Comprehend**: NLP, sentiment analysis, entities, key phrases, toxicity detection.
- **Amazon Comprehend Medical**: Medical entity and relationship extraction.
- **Amazon Textract**: Extract text and structure from PDFs/scanned documents/forms.
- **Amazon Transcribe**: Speech to text, subtitles.
- **AWS HealthScribe**: Clinical speech-to-text and clinical note generation.
- **Amazon Translate**: Text translation between languages.
- **Amazon Polly**: Text to speech and voice-overs.
- **Amazon Rekognition**: Image/video analysis, object detection, moderation, custom labels.
- **Amazon Personalize**: Personalized recommendations.
- **Amazon Lex**: Conversational interfaces/chatbots.
- **Amazon Kendra**: Enterprise search.
- **Amazon Macie**: Sensitive data discovery in S3 and alerts.
- **Amazon Augmented AI (A2I)**: Human review workflows and confidence thresholds.

## Responsible AI

Repeated responsible AI topics:

- **Fairness**: Avoid biased outcomes across demographics.
- **Transparency**: Make model behavior and decisions understandable.
- **Explainability / interpretability**: Show why the model made a prediction.
- **Privacy and security**: Protect sensitive data and access.
- **Governance**: Policies, standards, accountability, compliance, documentation.
- **Human-centered design**: Make AI understandable and useful for people affected by decisions.

### Bias and Fairness

- **Sampling bias**: Training data is not representative of the population.
- **Class imbalance**: Some classes/demographics have more examples than others.
- Reduce bias by using diverse, representative datasets.
- Detect imbalances or disparities in data.
- Include fairness metrics in evaluation.
- Modify training data to mitigate bias.
- Use human-in-the-loop review for high-risk or postprocessing checks.
- For biased fine-tuned LLMs, add more diverse training data and fine-tune again.

### Explainability

Use these when asked to explain decisions:

- **SageMaker Clarify**: Bias/explainability reports and feature influence.
- **SHAP/Shapley values**: Explain feature contributions.
- **Partial dependence plots (PDPs)**: Show relationship between features and predictions.
- **Decision trees/logistic regression**: More interpretable model choices.
- **Model complexity** affects explainability: simpler models are easier to explain.
- **Citations/source links** improve user confidence in AI agent responses.

### Risks and Limitations

- **Hallucination**: Plausible but incorrect/fabricated output.
- **Nondeterminism**: Same prompt may produce different outputs due to randomness.
- **Toxicity**: Harmful or offensive output.
- **Plagiarism**: Copying AI-generated content without attribution or originality.
- **Data leakage**: Sensitive data exposed in outputs or training.
- **Overfitting**: Performs well on training data but poorly on new/evaluation data.
- **Underfitting**: Model is too simple and performs poorly even on training data.

Ways to reduce risks:

- Lower temperature for consistency and fewer hallucinations.
- Use RAG to ground answers in current sources.
- Use Bedrock Guardrails for content filtering.
- Remove PII/confidential data before training or fine-tuning.
- Use benchmark datasets and human evaluation.
- Use Model Monitor after deployment.
- Use human review for sensitive predictions.

## Security, Governance, and Compliance

### AWS Security Services

- **IAM**: Least privilege access, restrict model access, team-specific roles.
- **AWS KMS**: Encryption keys for data/model artifacts.
- **AWS PrivateLink**: Private API connectivity without public internet.
- **AWS CloudTrail**: API activity logging and unauthorized access tracking.
- **Amazon CloudWatch**: Metrics, alarms, monitoring, notifications.
- **AWS Config**: Resource configuration tracking and compliance checks.
- **AWS Audit Manager**: Continuous audit evidence collection and compliance assessment.
- **AWS Artifact**: Download AWS compliance reports and certifications.
- **Amazon Macie**: Sensitive data discovery in S3.
- **AWS Secrets Manager**: Secret storage, not model artifact encryption.
- **Amazon Inspector**: Vulnerability management, not AI explainability.

### Governance Concepts

- **Data residency**: Data must stay in a specific country/region.
- **Data retention**: Rules for how long data is stored and when it is deleted.
- **Data quality**: Accuracy, completeness, consistency, reliability.
- **Data diversity**: Representation across demographics and use cases.
- **Data labeling**: Assign labels/categories to records.
- **Data de-identification**: Remove or mask identifiers.
- **Algorithm accountability laws**: Review when automated decisions affect people, such as credit scores.
- **ISO accreditation for AI risk**: Reflects certified organizational framework/processes, not individual employees or every AI system.
- **Shared responsibility model**: AWS secures the cloud; customers secure their data, access, configurations, and application use.

## Model Evaluation Metrics

### Classification Metrics

- **Accuracy**: Correct predictions / total predictions. Use when asking how many items were classified correctly.
- **Precision**: Of items flagged positive, how many are actually positive. Use when false positives are costly, such as reducing employee review of non-fraud cases.
- **Recall**: Of actual positives, how many were found. Use when missing positives is costly.
- **F1 score**: Harmonic mean of precision and recall. Use for binary classification, imbalanced classes, churn prediction, and balancing detection with correct labeling.
- **Confusion matrix**: Shows true positives, false positives, true negatives, false negatives.
- **AUC / ROC AUC**: Measures ability to distinguish between classes.

### Regression Metrics

- **RMSE / MSE**: Numeric prediction error.
- **R-squared**: Regression fit, not classification.

### Generative AI Metrics

- **BLEU**: Machine translation quality; compares n-gram overlap with reference translations.
- **ROUGE**: Summarization quality; compares overlap with reference summaries.
- **BERTScore**: Semantic similarity for generated text, summarization, and translation using contextual embeddings.
- **F1 for summarization**: Often ROUGE-F1 style overlap measure.
- **Human evaluation**: Use when style preference, subjective quality, domain experts, or custom prompt datasets matter.
- **Benchmark datasets**: Least administrative effort for standard bias/fairness/toxicity evaluation.

### Operational and Business Metrics

- **Average response time / latency**: Runtime efficiency.
- **Time to first token**: Generation responsiveness.
- **Conversion rate after AI assistant interaction**: Sales impact.
- **Cost per conversation**: Financial impact of chatbot operations.
- **Average call duration / average handle time**: Contact center efficiency.
- **Customer satisfaction score (CSAT)**: User/business satisfaction.
- **ROI**: Financial return.
- **Time-to-value**: Business value speed.
- **Impact on business processes**: Business effectiveness.

## ML Lifecycle and MLOps

### Typical ML Lifecycle

1. Define business goal and frame the ML problem.
2. Collect data.
3. Explore data with EDA.
4. Prepare and preprocess data.
5. Engineer features.
6. Train the model.
7. Tune hyperparameters.
8. Evaluate the model.
9. Deploy the model.
10. Monitor the model.

### Foundation Model Lifecycle

- Data selection.
- Pre-training.
- Fine-tuning/customization.
- Evaluation.
- Deployment.
- Monitoring and governance.

### EDA and Data Prep

- **Exploratory data analysis (EDA)**: Statistics, visualization, correlation matrix, understanding data characteristics.
- **Feature engineering**: Create or transform features to improve performance.
- **Data labeling**: Add categories/target labels to records.
- **Data balancing**: Address class imbalance.
- **Data augmentation**: Add/transform examples to improve representation or reduce bias.

### MLOps

- **MLOps** means Machine Learning Operations.
- Important practices: model versioning, reproducibility, automated testing, validation, deployment automation, monitoring.
- **Infrastructure as code (IaC)** helps deploy scalable, consistent, repeatable ML workloads.
- **Model Registry** stores and versions models.
- **Model Cards** document models.
- **Model Monitor** watches deployed models.

## Data Types and Matching Tasks

- **Text data**: NLP, sentiment, summarization, classification, translation.
- **Image data**: Computer vision, object detection, image classification, image generation.
- **Audio data**: Transcription, subtitles, speech recognition.
- **Time series data**: Forecasting demand, sales, internet speed variation, disease trends over time.
- **Tabular data**: Structured rows/columns, credit scoring, churn prediction, customer records.
- **Multimodal data**: Text plus images, image questions with text answers, multimodal search.

## Common Scenario-to-Answer Patterns

### If You See This, Think This

- "No code ML" -> **SageMaker Canvas**.
- "Data labeling with humans" -> **SageMaker Ground Truth**.
- "Managed labeling workforce" -> **SageMaker Ground Truth Plus**.
- "Human review with confidence thresholds" -> **Amazon A2I**.
- "Share/manage features across teams" -> **SageMaker Feature Store**.
- "Detect bias and explain predictions" -> **SageMaker Clarify**.
- "Production drift" -> **SageMaker Model Monitor**.
- "Document model purpose and limitations" -> **SageMaker Model Cards**.
- "Store/manage/version models" -> **SageMaker Model Registry**.
- "Pre-trained models and quick deployment" -> **SageMaker JumpStart**.
- "Private API access" -> **PrivateLink**.
- "API logging" -> **CloudTrail**.
- "Performance metrics and alarms" -> **CloudWatch**.
- "Compliance reports" -> **Artifact**.
- "Compliance assessment/evidence" -> **Audit Manager**.
- "Configuration compliance" -> **Config**.
- "Sensitive data in S3" -> **Macie**.
- "Personalized recommendations" -> **Personalize**.
- "Enterprise search" -> **Kendra**.
- "Vector search" -> **OpenSearch Service** or **Aurora pgvector**.
- "PDF text extraction" -> **Textract**.
- "Audio to text" -> **Transcribe**.
- "Clinical notes" -> **HealthScribe**.
- "Text to speech" -> **Polly**.
- "Translate text" -> **Translate**.
- "Sentiment/toxicity/entities" -> **Comprehend**.
- "Medical entity extraction" -> **Comprehend Medical**.
- "Build generative AI app" -> **Bedrock**.
- "Developer productivity/code/test docs" -> **Amazon Q Developer**.
- "Employee assistant over internal data" -> **Amazon Q Business**.
- "Graphs from natural language BI" -> **Amazon Q in QuickSight**.

## High-Yield Comparisons

### RAG vs Fine-Tuning vs Prompt Engineering

- **Prompt engineering**: Cheapest/fastest way to improve format, tone, style, length, and accuracy.
- **RAG**: Best for current/private factual knowledge and changing documents.
- **Fine-tuning**: Best when the model must learn a specific style, domain behavior, or task from examples.
- **Continued pre-training**: Best for broad domain adaptation using large internal/recent corpora.
- **Training from scratch**: Most control, most cost, most security responsibility.

### Guardrails vs Clarify vs Model Cards vs Model Monitor

- **Guardrails**: Runtime safety filters and policy controls for Bedrock inputs/outputs.
- **Clarify**: Bias detection and explainability for ML models.
- **Model Cards**: Documentation and audit metadata.
- **Model Monitor**: Drift and quality monitoring in production.

### Bedrock Agents vs Knowledge Bases

- **Knowledge Bases**: Retrieve relevant information from documents/data sources.
- **Agents**: Plan and perform actions, call APIs/tools, query data sources, orchestrate workflows.
- Many real applications use both: an Agent can use a Knowledge Base.

### CloudTrail vs CloudWatch

- **CloudTrail**: Who called which AWS API and when.
- **CloudWatch**: Metrics, logs, alarms, performance monitoring, notifications.

### Batch vs Real-Time vs Async vs Serverless Inference

- **Batch**: Large offline jobs; no immediate answer; lowest cost for scheduled processing.
- **Real-time**: Immediate low-latency response.
- **Async**: Large inputs or long-running inference with near-real-time needs.
- **Serverless**: No infrastructure management and variable traffic.

## Final Cram List

Read these topics first if you have very little time:

1. Amazon Bedrock: Guardrails, Knowledge Bases, Agents, model evaluation, logging, pricing/throughput.
2. Prompt engineering: zero-shot, one-shot, few-shot, chain-of-thought, prompt chaining, ReAct, negative prompts, prompt injection.
3. RAG: chunking, embeddings, vector search, OpenSearch, Aurora pgvector, Kendra.
4. SageMaker: Canvas, Clarify, Model Monitor, Model Cards, Feature Store, Ground Truth, JumpStart, Model Registry.
5. Model metrics: accuracy, precision, recall, F1, AUC, RMSE/MSE, BLEU, ROUGE, BERTScore.
6. Responsible AI: fairness, bias, transparency, explainability, governance, privacy/security.
7. Security/compliance: IAM, KMS, PrivateLink, CloudTrail, CloudWatch, Config, Audit Manager, Artifact, Macie.
8. Inference choices: batch, real-time, asynchronous, serverless, provisioned vs on-demand Bedrock throughput.
9. AWS AI services: Comprehend, Textract, Transcribe, Translate, Polly, Rekognition, Personalize, Lex, Q Developer, Q Business.
10. ML basics: supervised vs unsupervised vs reinforcement learning, overfitting, feature engineering, EDA, data labeling, model drift.
