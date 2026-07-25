# 🚀 AI Resume Analyzer & ATS Score Checker

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![spaCy](https://img.shields.io/badge/spaCy-NLP-09A3D5?style=for-the-badge&logo=spacy&logoColor=white)](https://spacy.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

An enterprise-grade, full-stack **AI Resume Analyzer & ATS Score Checker** built with **Flask, spaCy NLP, scikit-learn, and OpenAI GPT-4o**. Upload any resume (PDF or DOCX), compare it against target job descriptions, and instantly receive a multi-dimensional ATS score breakdown alongside actionable recruiter recommendations.

---

## ✨ Features

- **📄 Multi-Format Resume Parsing**: Fast text extraction from PDF (`pdfplumber`) and DOCX (`python-docx`) documents.
- **🔑 spaCy NLP Keyword Intelligence**: Extracts lemmatized nouns, verbs, adjectives, and domain skills; highlights matched vs. missing keywords.
- **📐 TF-IDF Cosine Similarity**: Measures deep semantic relevance between your resume content and the job description using `scikit-learn`.
- **📑 Structural Section Coverage**: Verifies presence of key resume sections (*Experience, Education, Skills, Projects, Summary, Certifications*).
- **🤖 GPT-4o Actionable AI Feedback**: Generates an executive summary, keyword placement strategies, formatting fixes, bullet rewrites, and top 3 quick wins.
- **💎 Modern Dark Glassmorphism UI**: 
  - Drag-and-drop file uploader with instant file preview.
  - Live job description word counter and 1-click **Sample JD Loader**.
  - Animated step-by-step progress indicator overlay.
  - Interactive SVG radial score gauge & sub-metric progress bars.
  - Keyword explorer with search, category tabs, and 1-click **Copy Missing Keywords**.
  - Formatted Markdown rendering for AI feedback with copy & print/PDF export features.

---

## 🛠️ Technology Stack

| Component | Technology / Library |
| :--- | :--- |
| **Backend Framework** | Python 3.9+, Flask, Werkzeug |
| **AI / LLM Engine** | OpenAI API (`gpt-4o`) |
| **Natural Language Processing** | spaCy (`en_core_web_sm`), NLTK (`stopwords`) |
| **Vector Similarity** | scikit-learn (`TfidfVectorizer`, Cosine Similarity) |
| **Document Parsers** | `pdfplumber`, `python-docx` |
| **Frontend UI** | HTML5, Modern Vanilla CSS3 (Glassmorphism System), Vanilla JS |
| **Icons & Renderers** | FontAwesome 6, Google Fonts (Plus Jakarta Sans & Inter), Marked.js |

---

## 📁 Project Architecture

```
AI-Resume-Analyzer-ATS-Score-Checker/
│
├── app.py                   # Flask server entry point & route definitions
├── analyzer/                # Core NLP & ATS Scoring Package
│   ├── __init__.py          # Package initialization
│   ├── parser.py            # Extracts raw text from PDF and DOCX files
│   ├── nlp_utils.py         # spaCy NLP keyword extraction & matching logic
│   ├── ats_scorer.py        # Composite ATS score algorithm (Keyword + TF-IDF + Section)
│   └── ai_feedback.py       # OpenAI GPT-4o integration for recruiter feedback
│
├── static/                  # Static web assets
│   └── style.css            # Dark Glassmorphism CSS design system & animations
│
├── templates/               # Jinja2 HTML templates
│   ├── index.html           # File upload & job description analysis form
│   └── result.html          # ATS score dashboard & AI feedback report
│
├── .env                     # Environment variables (OpenAI API key)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🧮 How the Composite ATS Score is Calculated

The total ATS score is computed using a weighted tri-factor formula:

$$ \text{ATS Score} = (\text{Keyword Overlap} \times 0.50) + (\text{TF-IDF Cosine Similarity} \times 0.30) + (\text{Section Coverage} \times 0.20) $$

1. **Keyword Overlap (50%)**: Percentage of job description keywords present in the resume.
2. **TF-IDF Semantic Similarity (30%)**: Cosine similarity between resume and job description TF-IDF word vectors.
3. **Section Coverage (20%)**: Structural audit of essential sections (*Experience, Education, Skills, Projects, Summary, Certifications*).

---

## ⚡ Quick Start & Installation

### Prerequisites
- Python **3.9** or higher installed.
- An **OpenAI API Key** (for GPT-4o recommendations).

### 1. Clone the Repository
```bash
git clone https://github.com/shanusingh07/AI-Resume-Analyzer-ATS-Score-Checker.git
cd AI-Resume-Analyzer-ATS-Score-Checker
```

### 2. Create and Activate Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies & Download NLP Models
```bash
pip install -r requirements.txt

# Download spaCy language model & NLTK data
python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run the Application
```bash
python app.py
```
Open your browser and navigate to: **`http://127.0.0.1:5000`**

---

## 🌐 Deployment Guide

### Deploying to Render / Railway
1. Add a `Procfile` to the root directory:
   ```web: gunicorn app:app```
2. Install `gunicorn`:
   ```bash
   pip install gunicorn
   ```
3. Set your Environment Variable `OPENAI_API_KEY` in the hosting provider's dashboard.
4. Set Build Command:
   ```bash
   pip install -r requirements.txt && python -m spacy download en_core_web_sm && python -c "import nltk; nltk.download('stopwords')"
   ```
5. Set Start Command: `gunicorn app:app`.

---

## 🔒 Privacy & Data Security

- **In-Memory Processing**: Uploaded resumes are temporarily processed to extract text and immediately deleted from the server disk.
- **No Data Retention**: Your resumes and job descriptions are never saved to databases or used to train public AI models.

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more details.
