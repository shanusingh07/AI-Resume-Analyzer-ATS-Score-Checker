import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ai_feedback(resume_text: str, jd_text: str, ats_data: dict) -> str:
    """Generate targeted feedback using GPT-4o."""

    prompt = f"""
You are an expert ATS resume coach and technical recruiter.

**Job Description:**
{jd_text[:1500]}

**Resume Content:**
{resume_text[:2000]}

**ATS Analysis Results:**
- Overall ATS Score     : {ats_data['ats_score']} / 100
- Keyword Match Score   : {ats_data['keyword_score']} / 100
- Semantic Similarity   : {ats_data['tfidf_score']} / 100
- Section Coverage Score: {ats_data['section_score']} / 100
- Missing Keywords      : {', '.join(ats_data['missing_keywords'][:20])}
- Sections Found        : {', '.join(ats_data['sections_found'])}

Provide a structured, actionable resume improvement report with:

1. **Executive Summary** — Overall assessment in 2-3 sentences.
2. **Keyword Optimization** — Exact keywords to add and where to place them.
3. **Layout & Structure Fixes** — Section ordering, formatting, and ATS-friendliness.
4. **Content Enhancement** — Bullet point rewrites, quantification suggestions.
5. **Quick Wins** — Top 3 changes for immediate score improvement.

Be specific, concise, and use bullet points.
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a professional ATS resume optimization expert."},
            {"role": "user",   "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1200
    )

    return response.choices[0].message.content
