import re
import spacy

def extract_name(text):
    lines = text.strip().split('\n')
    ignore_keywords = ['resume', 'cv', 'curriculum vitae', 'data scientist', 'software engineer']

    for line in lines[:10]:
        line_clean = line.strip().lower()

        # Skip unwanted lines
        if not line.strip() or any(word in line_clean for word in ignore_keywords):
            continue

        # If line contains only alphabets and no numbers or symbols
        if line.strip().isalpha():
            if len(line.strip().split()) <= 3:
                return line.strip()

        # Fallback for multi-word names
        words = line.strip().split()
        if 1 < len(words) <= 3 and sum(word[0].isupper() for word in words) >= 2:
            if not any(char.isdigit() for char in line):
                return line.strip()

    return None

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group() if match else None

def extract_phone(text):
    match = re.search(r'(\+?\d{1,3}[\s.-]?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}', text)
    return match.group() if match else None

def extract_linkedin(text):
    match = re.search(r'(https?://)?(www\.)?linkedin\.com/in/[A-Za-z0-9_-]+', text)
    return match.group() if match else None

def extract_skills(text):
    # Example skill set to match — you can expand this!
    skill_keywords = [
        'Python', 'SQL', 'Excel', 'Pandas', 'NumPy', 'Java', 'Power BI', 'Data Visualization',
        'Tableau', 'Data Analysis', 'Machine Learning', 'Deep Learning', 'SPSS', 'MongoDB',
        'XGBoost', 'Scikit-learn', 'NLP', 'TensorFlow', 'Keras', 'AWS', 'GitHub'
    ]

    found_skills = []
    for skill in skill_keywords:
        pattern = re.compile(r'\b' + re.escape(skill) + r'\b', re.IGNORECASE)
        if re.search(pattern, text):
            found_skills.append(skill)
    
    return list(set(found_skills))  # remove duplicates

def extract_education(text):
    education_keywords = ['Bachelor', 'Master','MPhil', 'B.Tech', 'M.Tech', 'B.E', 'M.E', 'B.Sc', 'M.Sc', 'MBA', 'PhD', 'Diploma']
    lines = text.split('\n')
    education_list = []

    for line in lines:
        for keyword in education_keywords:
            if keyword.lower() in line.lower():
                degree_match = keyword
                institution_match = line
                year_match = re.search(r'(20\d{2}|19\d{2})', line)
                education_list.append({
                    'degree': degree_match,
                    'institution': institution_match.strip(),
                    'year': year_match.group() if year_match else None
                })
                break  

    return education_list if education_list else None

def extract_workexperience(text):
    experience_entries = []
    
    # Split by lines and strip
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    exp_pattern = re.compile(r'^(.*?),\s*(.*?)\s+((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4})\s*[–-]\s*((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}|Present)$', re.IGNORECASE)

    for line in lines:
        match = exp_pattern.match(line)
        if match:
            title = match.group(1).strip()
            company = match.group(2).strip()
            duration = f"{match.group(3)} – {match.group(4)}"
            experience_entries.append({
                "title": title,
                "company": company,
                "duration": duration
            })
    
    return experience_entries if experience_entries else None

def extract_projects(text):
    projects = []
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    project_title = None
    for i, line in enumerate(lines):
        if "Objective" in line:
            project_title = lines[i - 1] if i > 0 else None
            objective = line.replace("Objective:", "").strip()
            if project_title:
                projects.append({
                    "title": project_title,
                    "objective": objective
                })
    return projects if projects else None

def extract_certifications(text):
    certifications = []
    education_keywords = ['bachelor', 'master', 'phd', 'mca', 'mba', 'b.sc', 'm.sc', 'mtech', 'btech', 'mphil', 'university', 'college']

    # Clean and split into lines
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    for line in lines:
        line_lower = line.lower()

        # Skip if the line looks like an education entry
        if any(kw in line_lower for kw in education_keywords):
            continue

        # Try matching a cert-like pattern: Name - Org - Year
        match = re.match(r'^(.*?)[\-,]\s*(.*?)[\-,]\s*(\d{4})$', line)
        if match:
            name = match.group(1).strip()
            org = match.group(2).strip()
            year = match.group(3).strip()
            certifications.append({
                "name": name,
                "organization": org,
                "year": year
            })

    return certifications if certifications else None

def wrap_field(value, confidence):
    return {"value": value if value else None, "confidence": confidence if value else 0.0}
