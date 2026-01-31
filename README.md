# ⚖️ GenAI Contract Analysis & Risk Assessment Bot  
### AI-Powered Legal Assistant for Indian SMEs

## 🚀 Overview

The **GenAI Contract Analysis & Risk Assessment Bot** is a sophisticated AI-powered legal assistant designed to help Small and Medium Enterprises (SMEs) understand complex contracts, identify legal risks, and receive actionable advice in simple business language.

The system combines **NLP preprocessing (spaCy)** with **GPT-4o reasoning** to perform clause-level risk analysis, compliance detection, and generate structured legal summaries.

---

## 🎯 Problem Statement

Small businesses often sign contracts without fully understanding:

- Hidden liabilities
- Unfavorable clauses
- Indemnity risks
- Non-compete restrictions
- IP ownership transfers
- Arbitration & jurisdiction constraints

Our solution simplifies legal complexity into structured, understandable, and actionable insights.

---

## 🧠 Key Features

### 🔍 Core Legal NLP Tasks
- Contract Type Classification
- Clause & Sub-Clause Extraction
- Named Entity Recognition (Parties, Dates, Amounts, Jurisdiction)
- Obligation vs Right vs Prohibition Identification
- Risk & Compliance Detection
- Ambiguity Detection
- Clause Similarity Matching to Templates

---

### ⚠️ Risk Assessment Capabilities

- Clause-Level Risk Scoring (Low / Medium / High)
- Contract-Level Composite Risk Score
- Automatic Identification of:
  - Penalty Clauses
  - Indemnity Clauses
  - Unilateral Termination
  - Arbitration & Jurisdiction Terms
  - Auto-Renewal & Lock-in Periods
  - Non-compete Clauses
  - Intellectual Property Transfer Clauses

---

### 📊 User-Facing Outputs

- Simplified Contract Summary (Plain Business English)
- Clause-by-Clause Explanation
- Unfavorable Clause Highlighting
- Suggested Renegotiation Alternatives
- SME-Friendly Contract Templates
- Risk Distribution Dashboard
- Downloadable PDF Legal Report

---

### 🌐 Multilingual Support

- English & Hindi Contract Parsing
- Hindi → English internal normalization
- Simplified English output for SMEs

---

### 🔐 Confidentiality & Compliance

- No external legal database usage
- Local processing architecture
- JSON-based audit logging
- Secure API key handling

---

## 🏗️ System Architecture

User Upload (PDF / DOCX / TXT)
↓
Text Extraction (Parser Module)
↓
NLP Preprocessing (spaCy)
↓
Clause Extraction & Entity Recognition
↓
Rule-Based Risk Detection
↓
GPT-4o Legal Reasoning Engine
↓
Composite Risk Scoring
↓
PDF Report Generation + Audit Logging

## 🛠️ Tech Stack

- **LLM:** GPT-4o
- **NLP:** spaCy
- **Frontend UI:** Streamlit
- **Backend:** Python
- **Storage:** JSON-based audit logs
- **Visualization:** Matplotlib

---

## 📂 Supported Input Formats

- PDF (Text-based)
- DOC/DOCX
- Plain Text (.txt)

---

## 📈 Risk Scoring Logic

Each clause is assigned a numerical risk score based on:

- Presence of high-risk legal keywords
- Clause structure complexity
- Identified unfavorable terms

Composite contract risk is calculated as the average clause risk score.

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/contract-legal-ai.git

cd contract-legal-ai

2️⃣ Install Dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

3️⃣ Add OpenAI API Key

Create a .env file or update config.py:

OPENAI_API_KEY = "your-api-key-here"
MODEL_NAME = "gpt-4o"

4️⃣ Run the Application
python -m streamlit run app.py

📊 Example Output

Risk Distribution Dashboard

Clause-Level Risk Insights

Actionable Renegotiation Suggestions

Downloadable PDF Report

🏆 Innovation Highlights

Hybrid Architecture (Rule-Based + LLM)

SME-Focused Legal Simplification

Multilingual Contract Handling

Structured Risk Quantification

Audit-Ready Report Generation

🚧 Future Enhancements

Fine-tuned legal LLM integration

Private on-premise deployment

Automated compliance benchmarking

Industry-specific contract templates