Resume box
Job Description box
User Goal box
Run Agent button
def skill_gap_tool(resume):
    skills = [
        "Python",
        "SQL",
        "Machine Learning",
        "Statistics",
        "Excel",
        "Tableau",
        "Power BI",
        "Pandas",
        "Scikit-learn",
        "GitHub",
        "Generative AI"
    ]

    missing = []

    for skill in skills:
        if skill.lower() not in resume.lower():
            missing.append(skill)

    return missing
