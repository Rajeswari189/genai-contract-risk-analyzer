from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(filename, summary):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Contract Risk Report", styles["Title"]))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(summary, styles["BodyText"]))

    doc.build(elements)
