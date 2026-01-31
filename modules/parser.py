from PyPDF2 import PdfReader
import docx

def extract_text(file):
    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        return "".join([page.extract_text() for page in reader.pages])

    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join([para.text for para in doc.paragraphs])

    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    return ""
