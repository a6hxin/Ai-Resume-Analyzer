skills_db = [
    "python",
    "html",
    "css",
    "javascript",
    "react",
    "node",
    "sql",
    "git",
    "github"
]


def extract_skills(text):
    found = []

    for skill in skills_db:
        if skill in text:
            found.append(skill)

    return found


def calculate_score(skills):

    total = len(skills_db)
    score = int((len(skills) / total) * 100)

    missing = []

    for skill in skills_db:
        if skill not in skills:
            missing.append(skill)

    return score, missing

def job_match(resume_text, job_desc):

    resume_words = set(resume_text.split())
    job_words = set(job_desc.lower().split())

    matched = resume_words & job_words

    score = int(len(matched) / len(job_words) * 100)

    return score