import PyPDF2
import spacy

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# Function to extract raw text from a PDF
def extract_text_from_pdf(uploaded_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to extract keywords from resume text
def extract_keywords(text):
    doc = nlp(text)
    keywords = []

    for token in doc:
        if not token.is_stop and not token.is_punct and token.pos_ in ["NOUN", "PROPN"]:
            keywords.append(token.text.lower())

    return list(set(keywords))  # Remove duplicates
