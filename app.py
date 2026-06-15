import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Career Agent P3")

st.title("AI Career Agent P3")

st.write("AI Career Agent with Custom MCP Tools")

resume = st.text_area(
    "Paste Resume Here",
    height=200
)

job_description = st.text_area(
    "Paste Job Description Here",
    height=200
)

user_goal = st.text_input(
    "Career Goal",
    "Help me get this internship"
)

# MCP TOOL 1
def skill_gap_tool(resume, job_description):

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

        if skill.lower() in job_description.lower():

            if skill.lower() not in resume.lower():
                missing.append(skill)

    return missing


# MCP TOOL 2
def score_job_fit(resume, job_description):

    skills = [
        "Python",
        "SQL",
        "Machine Learning",
        "Statistics",
        "Excel",
        "Pandas",
        "Scikit-learn",
        "GitHub",
        "Generative AI"
    ]

    matches = 0

    required = 0

    for skill in skills:

        if skill.lower() in job_description.lower():

            required += 1

            if skill.lower() in resume.lower():
                matches += 1

    if required == 0:
        return 50

    score = int((matches / required) * 100)

    return score


if st.button("Run Agent"):

    if not resume or not job_description:

        st.warning(
            "Please enter both resume and job description."
        )

    else:

        missing_skills = skill_gap_tool(
            resume,
            job_description
        )

        fit_score = score_job_fit(
            resume,
            job_description
        )

        st.subheader("Custom MCP Tool Output")

        st.write("Job Fit Score")

        st.success(f"{fit_score}/100")

        st.write("Missing Skills")

        st.write(missing_skills)

        genai.configure(
            api_key=st.secrets["GEMINI_API_KEY"]
        )

        model = genai.GenerativeModel(
            "gemini-2.5-flash-lite"
        )

        prompt = f"""
You are an AI Career Agent.

User Goal:
{user_goal}

Resume:
{resume}

Job Description:
{job_description}

MCP Tool Results:

Job Fit Score:
{fit_score}

Missing Skills:
{missing_skills}

Your task:

1. Decide the most important next action.
2. Explain your reasoning.
3. Recommend resume improvements.
4. Suggest skills to learn.
5. Give interview preparation tips.
6. Provide next steps.

Return:

Decision:
Reason:
Resume Improvements:
Skills To Learn:
Interview Prep:
Next Steps:
"""

        response = model.generate_content(prompt)

        st.subheader("Agent Recommendation")

        st.write(response.text)
