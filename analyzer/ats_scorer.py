from .nlp_utils import extract_keywords, keyword_match_score, get_missing_keywords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_ats_score(resume_text: str, jd_text: str) -> dict:
    """
    Calculate a composite ATS score using:
    - Keyword match (50%)
    - TF-IDF cosine similarity (30%)
    - Section presence check (20%)
    """

    resume_kw = extract_keywords(resume_text)
    jd_kw     = extract_keywords(jd_text)

    # --- 1. Keyword Match Score (50%) ---
    kw_score = keyword_match_score(resume_kw, jd_kw)

    # --- 2. TF-IDF Cosine Similarity (30%) ---
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text, jd_text])
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    tfidf_score = round(cosine_sim * 100, 2)

    # --- 3. Section Presence Score (20%) ---
    required_sections = [
        "experience", "education", "skills",
        "projects", "summary", "certifications"
    ]
    resume_lower = resume_text.lower()
    found = sum(1 for s in required_sections if s in resume_lower)
    section_score = round((found / len(required_sections)) * 100, 2)

    # --- Composite ATS Score ---
    composite = round(
        (kw_score * 0.50) +
        (tfidf_score * 0.30) +
        (section_score * 0.20),
        2
    )

    return {
        "ats_score":       composite,
        "keyword_score":   kw_score,
        "tfidf_score":     tfidf_score,
        "section_score":   section_score,
        "matched_keywords": sorted(list(resume_kw & jd_kw)),
        "missing_keywords": get_missing_keywords(resume_kw, jd_kw),
        "sections_found":  [s for s in required_sections if s in resume_lower],
    }
