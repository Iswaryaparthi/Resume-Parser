import pdfplumber
import json  

from utilities import (
    extract_name, extract_email, extract_phone, extract_linkedin, extract_skills,
    extract_education, extract_workexperience,extract_projects, extract_certifications,wrap_field
)

# Extract text from the PDF file
def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# Main function to process resume data
if __name__ == "__main__":
    resume_path = "sample_resume.pdf"  # Path to your resume PDF
    text = extract_text_from_pdf(resume_path)  # Extract text from the PDF

    # Creating resume data dictionary with confidence scores
    resume_data = {
        "name": wrap_field(extract_name(text), 0.95),
        "email": wrap_field(extract_email(text), 0.99),
        "phone": wrap_field(extract_phone(text), 0.99),
        "linkedin": wrap_field(extract_linkedin(text), 0.90),
        "skills": wrap_field(extract_skills(text), 0.85),
        "education": wrap_field(extract_education(text), 0.85),
        "experience": wrap_field(extract_workexperience(text), 0.80),
        "certifications": wrap_field(extract_certifications(text), 0.75),
        "projects": wrap_field(extract_projects(text), 0.75)
    }

    # Print the resume data as JSON
    print(json.dumps(resume_data, indent=2))
    
    # Save the resume data to a JSON file
    with open("output.json", "w") as f:
        json.dump(resume_data, f, indent=2)

    print(" Resume data saved to output.json")