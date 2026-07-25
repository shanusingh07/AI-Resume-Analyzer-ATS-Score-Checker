import spacy
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords", quiet=True)
nlp = spacy.load("en_core_web_sm")

STOP_WORDS = set(stopwords.words("english"))

def extract_keywords(text: str) -> set:
    """Extract meaningful keywords using spaCy NLP."""
    doc = nlp(text.lower())
    keywords = set()

    for token in doc:
        if (
            not token.is_stop
            and not token.is_punct
            and not token.is_space
            and len(token.text) > 2
            and token.pos_ in {"NOUN", "PROPN", "VERB", "ADJ"}
        ):
            keywords.add(token.lemma_)  # lemmatized form

    return keywords


def keyword_match_score(resume_keywords: set, jd_keywords: set) -> float:
    """Calculate keyword overlap score (0–100)."""
    if not jd_keywords:
        return 0.0
    matched = resume_keywords & jd_keywords
    return round((len(matched) / len(jd_keywords)) * 100, 2)


def get_missing_keywords(resume_keywords: set, jd_keywords: set) -> list:
    """Return keywords in JD but missing from resume."""
    return sorted(list(jd_keywords - resume_keywords))
