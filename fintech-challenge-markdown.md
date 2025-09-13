# Deeptech GigaHack 2025
## FinTech Challenge 
### FinTech PrivacyGuard 
*by fineguide.ai*

## Challenge Overview
Your mission is to develop a modular, locally adapted mini-LLM that can detect and anonymize personal data according to Moldovan regulatory standards. The solution should balance compliance with data utility, enabling innovation without compromising citizens' privacy.

## Key Requirements

1. **Language Adaptation**: Ensure the model processes Romanian-language inputs with high accuracy.

2. **Sensitive Data Recognition**: Detect and classify identifiers such as IDNP/IDNO (national identification numbers), local address formats, and other regulated personal data fields.

3. **Anonymization**: Implement methods that securely anonymize data while maintaining its usefulness for analytics, financial modeling, and research.

4. **Compliance First**: The solution must meet Moldovan and EU-aligned data protection standards.

5. **Cross-Sector Utility**: Enable repurposing of anonymized datasets for applications in open banking, civic tech, and academic research.

6. **Scalability**: Design a modular, lightweight architecture that can be integrated into real-world fintech and government systems.

## Impact Goal
By building a privacy-first AI model, teams will contribute to Moldova's digital transformation agenda, helping fintechs, banks, and civic tech actors leverage data responsibly while protecting citizens' rights.

## Deliverables
- A working prototype of the mini-LLM with anonymization capability
- A demonstration showing successful anonymization of Romanian-language datasets containing personal identifiers
- A short integration roadmap outlining how the solution can be adopted by financial institutions, startups, and public services

## Minimum Requirements for the MVP
To qualify, teams must deliver at least:

1. **Core Data Detection** – Ability to correctly identify Moldovan-specific personal identifiers (IDNP, INDO, local address formats, phone numbers, etc.) in Romanian-language datasets.

2. **Anonymization Engine** – Working method (masking, pseudonymization, redaction, or tokenization) that removes or replaces sensitive data while preserving dataset structure.

3. **Accuracy Benchmark** – Demonstration on a sample dataset showing at least 70% correct detection and anonymization.

4. **Utility Preservation** – Evidence that the anonymized dataset can still be used for basic analytics or pattern recognition (not just "blanked out").

5. **Modularity & Scalability** – MVP should be packaged as a modular tool (script, API, or microservice) that can be realistically scaled or integrated into fintech or civic tech systems.

6. **Documentation & Demo** – Clear explanation of how it works + live demo during final pitch.

## Dataset Description
Romanian text samples specifically tailored for Moldova, containing realistic PII entities across multiple domains including healthcare, finance, education, legal, and technology sectors. The output format is compatible with the RONEC dataset structure using BIO2 tagging.

**Dataset Characteristics here**

**Data sets for FinTech challenge**

## How-to and Hints

### Architecture:
- You are free to use whatever approach you consider fit, but we recommend using pretrained multilingual LLMs such as BERT and XML-R or other models you find fit
- Free to use additional techniques to improve the accuracy scores, be creative

### Training data split:
- We recommend splitting training data 80/10/10 (training, eval, test)

### Accuracy metrics:
- **F1 Score** (will be used for judging criteria)
- Other metrics at your desire, optional, can include:
  - **Precision** – How many of the predicted entities are correct (avoids false alarms)
  - **Recall** – How many of the actual entities the model successfully found (avoids misses)
  - **Per-class scores** – Precision/recall/F1 for each entity type (e.g., PERSON, ORG, IBAN)
  - **Confusion Matrix** – Shows which entity types are being confused with each other

### Where to train:
- Use your own hardware as a start, start with small samples, make the code work, evaluate the initial accuracy
- We can provide a machine with a GPU on Linux
- Or we can provide access to huggingface spaces

### Deliverables and evaluation:
- We will provide an evaluation script and you will deliver the code to be compatible and run within that script to evaluate your implementation
- We will evaluate the algorithm on the out of sample data
- The evaluation script, templates, and examples can be found here:
  
  **[https://github.com/cmaftuleac/fintech_challenge_evaluator](https://github.com/cmaftuleac/fintech_challenge_evaluator)**

- `evaluator.py` will be used to evaluate your model
- Make sure the code is compatible with it
- There are some examples:
  - `anonymizer_mock.py` - a fake anonymizer example, it uses train data to output 95% accuracy
  - `anonymizer_ronec.py` - uses original ronec pretrained model (but different labels)
  - `anonymizer_template.py` - use is a template for your code

## Judging Criteria
Each team will be evaluated on:

### Technical Accuracy (30%)
- Precision in detecting sensitive data
- Reliability of anonymization methods

### Compliance & Standards (20%)
- Alignment with Moldovan data protection rules
- Consideration of GDPR/EU-level best practices

### Data Utility & Innovation (20%)
- Usefulness of anonymized datasets for fintech, banking, or research
- Creativity in how anonymization is balanced with data utility

### Scalability & Integration (15%)
- How well the solution can integrate into real-world fintech or civic tech systems
- Modularity, documentation, and deployment readiness

### Presentation & Clarity (15%)
- Quality of demo and clarity of technical explanation
- Feasibility of proposed roadmap for adoption

## Bonus Points
- **Creativity**: Enhance the accuracy with other methods that come with original algorithms
- **Multilingual Capability**: The LLM can also process inputs in Russian, English, or other languages common in Moldova and the region
- **Cross-Border Adaptability**: Ability to detect and anonymize identifiers from other countries/regions (e.g., EU address formats, international IDs, banking fields)
- **Performance & Efficiency**: Running effectively on resource-constrained environments (local servers, edge devices)