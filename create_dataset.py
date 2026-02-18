import random
import pandas as pd

# Define roles and skills
roles = {
    "Data Scientist": [
        "Python", "Machine Learning", "Deep Learning", "Pandas", "NumPy",
        "Matplotlib", "Seaborn", "Statistics", "Data Visualization",
        "SQL", "Scikit-learn", "TensorFlow", "Power BI", "Excel"
    ],
    
    "Machine Learning Engineer": [
        "Python", "Machine Learning", "TensorFlow", "PyTorch",
        "Scikit-learn", "Model Deployment", "Docker", "Flask",
        "FastAPI", "Deep Learning", "NLP", "Computer Vision"
    ],
    
    "Data Analyst": [
        "Excel", "SQL", "Power BI", "Tableau", "Data Cleaning",
        "Data Visualization", "Statistics", "Python", "Pandas",
        "Business Intelligence"
    ],
    
    "Backend Developer": [
        "Python", "Django", "Flask", "API Development",
        "Database Management", "SQL", "Git", "Docker",
        "REST API", "Authentication"
    ],
    "AI Engineer": [
        "Python", "Machine Learning", "Deep Learning", "TensorFlow",
        "PyTorch", "Computer Vision", "NLP", "Model Deployment",
        "MLOps", "Docker", "Kubernetes", "Cloud Computing",
        "Data Engineering", "APIs"
    ],

    "DevOps Engineer": [
        "Linux", "Docker", "Kubernetes", "CI/CD", "Jenkins",
        "AWS", "Azure", "GCP", "Terraform", "Ansible",
        "Monitoring", "Shell Scripting", "Git", "Cloud Infrastructure"
    ],

    "Frontend Developer": [
        "HTML", "CSS", "JavaScript", "React", "Angular",
        "Vue.js", "Responsive Design", "Bootstrap",
        "Tailwind CSS", "UI/UX", "REST APIs",
        "Version Control", "Web Performance"
    ],

    "Full Stack Developer": [
        "HTML", "CSS", "JavaScript", "React",
        "Node.js", "Express", "MongoDB",
        "SQL", "REST APIs", "Authentication",
        "Git", "Docker", "Cloud Deployment"
    ],

    "Data Engineer": [
        "Python", "SQL", "ETL", "Data Pipelines",
        "Apache Spark", "Hadoop", "Airflow",
        "Big Data", "Data Warehousing",
        "AWS", "Azure", "GCP", "Docker"
    ],

    "Cloud Engineer": [
        "AWS", "Azure", "GCP",
        "Cloud Architecture", "Docker",
        "Kubernetes", "Networking",
        "Security", "Infrastructure as Code",
        "Terraform", "Linux"
    ],
    "Cybersecurity Analyst": [
        "Network Security", "Penetration Testing", "Ethical Hacking",
        "Firewalls", "SIEM", "Python", "Linux",
        "Security Auditing", "Cryptography", "Incident Response"
    ],

    "Mobile App Developer": [
        "Java", "Kotlin", "Swift", "Flutter",
        "React Native", "Android Studio",
        "iOS Development", "REST APIs",
        "Firebase", "UI Design"
    ],

    "QA Engineer": [
        "Manual Testing", "Automation Testing",
        "Selenium", "Test Cases",
        "Bug Tracking", "JUnit",
        "API Testing", "Performance Testing",
        "Python", "CI/CD"
    ],

    "Business Analyst": [
        "Requirement Gathering", "Stakeholder Management",
        "Data Analysis", "SQL", "Excel",
        "Power BI", "Process Modeling",
        "Documentation", "Agile Methodology"
    ]


}

data = []

for role, skills in roles.items():
    for _ in range(100):
        num_skills = min(len(skills), random.randint(8, 12))
        selected_skills = random.sample(skills, k=num_skills)
        resume_text = (
    "Results-driven professional with experience in "
    + ", ".join(selected_skills)
    + ". Strong problem-solving abilities and hands-on project experience."
)

        data.append([resume_text, role])

# Create dataframe
df = pd.DataFrame(data, columns=["Resume", "Role"])

# Save to CSV
df.to_csv("tech_resume_dataset.csv", index=False)

print("Dataset created successfully!")
