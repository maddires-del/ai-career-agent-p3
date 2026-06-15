# Evaluation

## Test Case 1: Strong Match

Resume:
Python
SQL
Machine Learning
Pandas
GitHub

Job Description:
Data Science Intern requiring Python, SQL, Machine Learning, Pandas and communication skills.

Expected:
High match score and strong alignment.

Actual:
Job Fit Score: 100/100

Missing Skills:
None

Agent Decision:
Focus on resume refinement and interview preparation.

Observation:
The MCP tools correctly identified a strong match and the model shifted recommendations toward interview preparation instead of additional technical training.

---

## Test Case 2: Weak Resume

Resume:
Microsoft Word
PowerPoint
Customer Service

Job Description:
Data Science Intern requiring Python, SQL, Machine Learning and GitHub.

Expected:
Low score and identification of missing technical skills.

Actual:
Job Fit Score: 0/100

Missing Skills:

* Python
* SQL
* Machine Learning
* GitHub

Agent Decision:
Immediate Resume Overhaul and Skill Development.

Observation:
The MCP tools correctly identified all required technical skills as missing and generated a realistic learning roadmap.

---

## Test Case 3: Generative AI Internship

Resume:
Python
SQL
GitHub

Job Description:
Generative AI Intern requiring Python, Prompt Engineering, Generative AI and Machine Learning.

Expected:
Identify missing AI-related skills and provide learning recommendations.

Actual:
Job Fit Score: 33/100

Missing Skills:

* Machine Learning
* Generative AI

Agent Decision:
Prioritize learning Machine Learning and Generative AI.

Observation:
The system correctly adapted recommendations to a Generative AI role.

---

## Test Case 4: Incomplete Resume

Resume:
Student at Oakland University

Job Description:
Data Analyst Intern requiring Python, SQL and Excel.

Expected:
Low score and identification of missing foundational skills.

Actual:
Job Fit Score: 0/100

Missing Skills:

* Python
* SQL
* Excel

Agent Decision:
Focus on acquiring foundational technical skills.

Observation:
The system correctly identified missing qualifications and did not invent experience.

---

## Test Case 5: Failure Case

Resume:
Hardworking student

Job Description:
AI Research Intern requiring TensorFlow, Machine Learning and Python.

Expected:
Very low score, missing skills identified, and no invented experience.

Actual:
Job Fit Score: 0/100

Missing Skills:

* Python
* Machine Learning

Agent Decision:
Immediately focus on acquiring core skills and updating resume.

Observation:
The system correctly handled poor input quality and avoided fabricating qualifications.

