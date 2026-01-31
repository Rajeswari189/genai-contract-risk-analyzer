import spacy
from langdetect import detect

nlp = spacy.load("en_core_web_sm")

def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"

def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]
