import re

SKILLS = [
    "python",
    "sql",
    "excel",
    "power bi",
    "tableau",
    "machine learning",
    "pandas",
    "numpy",
    "scikit-learn",
    "data analysis",
    "statistics",
    "communication",
    "problem solving",
    "html",
    "css",
    "javascript",
    "java",
    "c++",
    "flask",
    "streamlit",
    "nlp",
    "tensorflow",
    "pytorch",
    "git",
    "data visualization"
]


def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS:
        pattern = (
            r"(?<![a-z0-9+#])"
            + re.escape(skill)
            + r"(?![a-z0-9+#])"
        )

        if re.search(pattern, text):
            found_skills.append(skill)

    return sorted(set(found_skills))