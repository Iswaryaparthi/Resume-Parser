# 📄 Resume Parser Project

This project is a **Resume Parser** built with Python. It extracts structured information like name, contact details, skills, education, work experience, certifications, and projects from resume PDF files.

## 🧠 Approach

1. **Text Extraction**:  
   Used `pdfplumber` to extract raw text from the PDF.

2. **Section-wise Parsing**:  
   Applied keyword and regex-based logic to extract structured data for:
   - Name
   - Email
   - Phone
   - LinkedIn
   - Skills
   - Education
   - Work Experience
   - Certifications
   - Projects

3. **Confidence Scoring**:  
   Each field is wrapped with a manually set confidence score using a utility function for interpretability.

4. **JSON Output**:  
   Parsed data is saved into a structured JSON format (`output.json`) for further usage or downstream applications.

## 🛠️ Libraries/Tools Used

- `pdfplumber`: PDF text extraction
- `re`: Regular expressions for pattern matching
- `json`: To store and view structured output
- Python Standard Libraries (os, etc.)

## 🧾 File Structure

- `main.py`: Main execution file to load PDF and extract data.
- `utilities.py`: Helper functions to extract various sections.
- `output.json`: Generated output in JSON format after parsing.
- `README.md`: This file.

## 📍Assumptions and Limitations

- Assumes resume is in English and in standard formatting.
- Parsing logic is based on keyword presence and regex, so it might fail on heavily styled or unconventional resumes.
- Confidence scores are manually assigned and not learned or predicted.
- 
## 📌 How to Run

1. Place a resume PDF as `sample_resume.pdf` in the root directory.
2. Run the script:

```bash
python main.py



