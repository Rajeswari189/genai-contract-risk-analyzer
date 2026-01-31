import re

def extract_clauses(text):
    clauses = re.split(r'\n\d+[\.\)]?\s', text)
    return [c.strip() for c in clauses if len(c.strip()) > 40]

def classify_contract(text):
    text = text.lower()

    if "employment" in text:
        return "Employment Agreement"
    elif "lease" in text:
        return "Lease Agreement"
    elif "vendor" in text:
        return "Vendor Contract"
    elif "partnership" in text:
        return "Partnership Deed"
    elif "service" in text:
        return "Service Agreement"
    else:
        return "General Contract"
