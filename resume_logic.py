import fitz  # PyMuPDF


# ----------------------------
# PDF TEXT EXTRACTION
# ----------------------------
def extract_text_from_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.lower()


# ----------------------------
# ROLE DEFINITIONS (10 ROLES)
# ----------------------------
ROLES = {

    "Data Scientist": [
        "python", "pandas", "numpy", "statistics", "machine learning",
        "data visualization", "sql", "deep learning",
        "feature engineering", "model evaluation"
    ],

    "AI Engineer": [
        "python", "machine learning", "deep learning",
        "nlp", "computer vision", "tensorflow",
        "pytorch", "model deployment",
        "data preprocessing", "neural networks"
    ],

    "Machine Learning Engineer": [
        "python", "scikit-learn", "machine learning",
        "model optimization", "feature engineering",
        "data pipelines", "docker", "mlops",
        "tensorflow", "pytorch"
    ],

    "Data Analyst": [
        "excel", "sql", "power bi",
        "tableau", "data cleaning",
        "statistics", "python",
        "data visualization", "reporting"
    ],

    "Backend Developer": [
        "python", "flask", "django",
        "api development", "sql",
        "database design", "authentication",
        "rest api", "docker"
    ],

    "Frontend Developer": [
        "html", "css", "javascript",
        "react", "responsive design",
        "ui ux", "bootstrap",
        "typescript", "web performance"
    ],

    "Full Stack Developer": [
        "html", "css", "javascript",
        "react", "node.js",
        "mongodb", "sql",
        "api integration", "authentication",
        "deployment"
    ],

    "DevOps Engineer": [
        "docker", "kubernetes",
        "aws", "ci cd",
        "linux", "terraform",
        "cloud computing", "monitoring",
        "git", "automation"
    ],

    "Cloud Engineer": [
        "aws", "azure", "gcp",
        "cloud security", "virtual machines",
        "networking", "linux",
        "terraform", "docker"
    ],

    "Cyber Security Analyst": [
        "network security", "ethical hacking",
        "penetration testing", "cryptography",
        "firewalls", "incident response",
        "risk assessment", "siem",
        "vulnerability assessment"
    ]
}


# ----------------------------
# YOUTUBE RESOURCE MAPPING
# ----------------------------
YOUTUBE_RESOURCES = {
    "python": "Krish Naik",
    "machine learning": "StatQuest",
    "deep learning": "DeepLearning.AI",
    "nlp": "Krish Naik",
    "computer vision": "Murtaza's Workshop",
    "tensorflow": "freeCodeCamp.org",
    "pytorch": "Aladdin Persson",
    "statistics": "StatQuest",
    "pandas": "Codebasics",
    "numpy": "Codebasics",
    "sql": "freeCodeCamp.org",
    "excel": "Leila Gharani",
    "power bi": "Guy in a Cube",
    "tableau": "Tableau Tim",
    "flask": "Tech With Tim",
    "django": "Corey Schafer",
    "react": "Traversy Media",
    "javascript": "The Net Ninja",
    "docker": "TechWorld with Nana",
    "kubernetes": "TechWorld with Nana",
    "aws": "Stephane Maarek",
    "azure": "Adam Marczak",
    "gcp": "Google Cloud Tech",
    "ethical hacking": "The Cyber Mentor",
    "penetration testing": "HackerSploit",
    "linux": "NetworkChuck",
    "terraform": "TechWorld with Nana",
    "node.js": "Traversy Media",
    "mongodb": "Web Dev Simplified",
    "api integration": "Programming with Mosh",
    "deployment": "Codevolution",
    "authentication": "The Net Ninja",
    "api development": "Tech With Tim",

}


# ----------------------------
# MAIN ANALYSIS FUNCTION
# ----------------------------
def analyze_resume(pdf_path):

    text = extract_text_from_pdf(pdf_path)

    role_scores = {}

    # Evaluate each role
    for role, skills in ROLES.items():

        matched_skills = [skill for skill in skills if skill in text]
        match_count = len(matched_skills)

        percentage = (match_count / len(skills)) * 100

        role_scores[role] = {
            "percentage": round(percentage, 2),
            "matched": matched_skills,
            "missing": [skill for skill in skills if skill not in text]
        }

    # Sort roles by highest match
    sorted_roles = sorted(
        role_scores.items(),
        key=lambda x: x[1]["percentage"],
        reverse=True
    )

    # Best matched role
    main_role = sorted_roles[0][0]
    main_data = sorted_roles[0][1]

    # Other suggested roles (top 3)
    related_roles = [
        {"role": r[0], "percentage": r[1]["percentage"]}
        for r in sorted_roles[1:4]
    ]

    youtube_suggestions = []

    for skill in main_data["missing"]:
        if skill in YOUTUBE_RESOURCES:
            youtube_suggestions.append({
                "skill": skill,
                "channel": YOUTUBE_RESOURCES[skill]
            })
    if not youtube_suggestions:
     youtube_suggestions.append({
        "skill": "General Learning",
        "channel": "freeCodeCamp.org"
    })



    # Motivation message
    percentage = main_data["percentage"]

    if percentage >= 85:
        motivation = "Outstanding profile! You're highly aligned with this role. Start applying to top companies with confidence."
    elif percentage >= 60:
        motivation = "You're on a strong path. Strengthen the remaining core skills and you'll be industry-ready soon."
    elif percentage >= 40:
        motivation = "Good foundation! Focus on the missing technical skills to significantly boost your career prospects."
    else:
        motivation = "Every expert was once a beginner. Start building these core skills step by step — your journey begins now."

    return {
        "predicted_role": main_role,
        "match_percentage": main_data["percentage"],
        "matched_skills": main_data["matched"],
        "required_skills": main_data["missing"],
        "related_roles": related_roles,
        "youtube_channels": youtube_suggestions,
        "motivation": motivation
    }
