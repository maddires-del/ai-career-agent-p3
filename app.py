import streamlit as st

st.title("AI Career Agent P3")

st.write("AI Career Agent with Custom MCP Tool")

resume = st.text_area("Paste Resume Here")

job_description = st.text_area("Paste Job Description Here")

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

if st.button("Run Agent"):

    missing_skills = skill_gap_tool(resume)

    st.subheader("Custom MCP Tool Output")

    st.write("Missing Skills:")

    st.write(missing_skills)
