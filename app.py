import streamlit as st
import google.generativeai as genai

st.title("AI Career Agent P3")

st.write("AI Career Agent with Custom MCP Tool")

resume = st.text_area("Paste Resume Here")

job_description = st.text_area("Paste Job Description Here")

user_goal = st.text_input(
    "Career Goal",
    "Help me get this internship"
)

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

    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

    model = genai.GenerativeModel("gemini-2.5-flash-lite")

    prompt = f"""
You are an AI Career Agent.

User Goal:
{user_goal}

Resume:
{resume}

Job Description:
{job_description}

Tool Output:
Missing Skills: {missing_skills}

Your task:

1. Decide what the user needs most.
2. Explain your decision.
3. Give recommendations.
4. Suggest next steps.

Format:

Decision:
Reason:
Recommendations:
Next Steps:
"""

    response = model.generate_content(prompt)

    st.subheader("Agent Recommendation")
    st.write(response.text)
