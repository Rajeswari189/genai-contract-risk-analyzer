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
    entities = []
    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "label": ent.label_
        })
    return entities
