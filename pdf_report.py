from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(name, question, answer, feedback, score):
    styles = getSampleStyleSheet()
    pdf = SimpleDocTemplate("report.pdf")

    content = []
    content.append(Paragraph(f"Name: {name}", styles['Normal']))
    content.append(Paragraph(f"Question: {question}", styles['Normal']))
    content.append(Paragraph(f"Answer: {answer}", styles['Normal']))
    content.append(Paragraph(f"Feedback: {feedback}", styles['Normal']))
    content.append(Paragraph(f"Score: {score}/10", styles['Normal']))

    pdf.build(content)
