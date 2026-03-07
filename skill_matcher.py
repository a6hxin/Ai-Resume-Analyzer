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