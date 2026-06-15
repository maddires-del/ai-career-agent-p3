# Build Log

## Version 1

Created the initial project structure with:

* app.py
* README.md
* build_log.md
* eval_examples.md
* requirements.txt

Goal:
Build an AI career assistant for Data Science and Generative AI internships.

---

## Version 2

Added Streamlit deployment.

Result:
Created a publicly accessible web application that accepts resumes and job descriptions.

---

## Version 3

Added Custom MCP Tool: Skill Gap Analyzer.

Problem:
The application could not identify which internship skills were missing.

Change:
Created a tool that compares resumes against internship skill requirements and returns missing skills.

Result:
The application can now identify skill gaps before generating recommendations.

---

## Version 4

Added Custom MCP Tool: Job Fit Scorer.

Problem:
Users had no quantitative measure of internship readiness.

Change:
Created a tool that calculates a job fit score using required skills from the job description.

Result:
Users receive a match score and can better understand their current alignment.

---

## Version 5

Integrated Gemini 2.5 Flash Lite.

Problem:
The application only displayed tool outputs and did not provide actionable guidance.

Change:
Connected MCP tool outputs to Gemini.

Result:
The language model now uses structured tool results to generate recommendations.

---

## Version 6

Added Autonomous Agent Workflow.

Problem:
The application needed evidence of agentic behavior.

Change:
The Gemini agent now evaluates MCP tool outputs and autonomously decides the most important next action.

Possible actions:

* Skill Development
* Resume Improvement
* Interview Preparation
* Application Readiness Review

Result:
The system demonstrates autonomous decision-making instead of returning fixed outputs.

---

## Evaluation Summary

Five evaluation cases were completed:

1. Strong Match
2. Weak Resume
3. Generative AI Internship
4. Incomplete Resume
5. Failure Case

Observation:
The MCP tools consistently identified missing skills and generated realistic recommendations without inventing experience.
