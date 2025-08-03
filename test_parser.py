from resume_parser import extract_text_from_pdf, extract_keywords
from db_manager import create_db, insert_resume

# Step 1: Extract text from PDF
with open("sample_resumes/sample1.pdf", "rb") as f:
    text = extract_text_from_pdf(f)
    print("Extracted text:")
    print(text[:500])  # print first 500 chars for brevity

# Step 2: Extract keywords from text
keywords = extract_keywords(text)
print("\nExtracted keywords:")
print(keywords)

# Step 3: Create database and table (if not already created)
create_db()
print("\nDatabase and table ensured.")

# Step 4: Insert resume into database
candidate_name = "John Doe"  # You can change this or make it dynamic
insert_resume(candidate_name, text, keywords)
print("Resume inserted into database successfully!")
