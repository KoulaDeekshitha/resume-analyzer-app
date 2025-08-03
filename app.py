import streamlit as st
from resume_parser import extract_text_from_pdf, extract_keywords
from db_manager import create_db, insert_resume

def main():
    st.title("📄 Resume Analyzer App")

    # Create DB & table if not exists
    create_db()

    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    
    if uploaded_file is not None:
        # Extract text from PDF
        text = extract_text_from_pdf(uploaded_file)
        
        # Extract keywords
        keywords = extract_keywords(text)

        # Show extracted info
        st.subheader("Extracted Text")
        st.write(text[:1000])  # Show first 1000 chars

        st.subheader("Extracted Keywords")
        st.write(keywords)

        # Input for candidate name
        candidate_name = st.text_input("Enter Candidate Name")

        if st.button("Save Resume to Database"):
            if candidate_name.strip() == "":
                st.error("Please enter candidate name")
            else:
                insert_resume(candidate_name, text, keywords)
                st.success("Resume saved successfully!")

if __name__ == "__main__":
    main()
