# AI Career Agent P3

## Purpose

AI Career Agent helps students prepare for Data Science, Machine Learning, and Generative AI internships.

## Custom MCP Tools

### Skill Gap Analyzer

This tool compares a student's resume against job requirements and identifies missing skills.

### Job Fit Scorer

This tool calculates a job fit score based on the overlap between the resume and job description.

## Agent Workflow

User Resume + Job Description

↓

Skill Gap Analyzer Tool

↓

Job Fit Scorer Tool

↓

Gemini Agent

↓

Decision, Recommendations, and Next Steps

## Model

Gemini 2.5 Flash Lite

## Deployment

Streamlit Cloud

## Autonomous Decision Making

The Gemini agent uses outputs from the MCP tools to determine the most appropriate recommendation for the user. Based on the job fit score and missing skills, the model decides whether the user should focus on interview preparation, resume improvements, or skill development.

## Evaluation

The system was evaluated using five test cases:

1. Strong Match
2. Weak Resume
3. Generative AI Internship
4. Incomplete Resume
5. Failure Case

Results showed that the MCP tools correctly identified missing skills and generated realistic recommendations without inventing experience.

## Grounding

The application uses an external skills dataset
(skills.csv) containing Data Science and Generative AI internship skills.

This dataset is loaded at runtime and used by the MCP tools.

## Architecture

User Input

↓

Resume + Job Description

↓

Skill Gap Analyzer MCP Tool

↓

Job Fit Scorer MCP Tool

↓

Gemini Agent

↓

Recommendations and Next Steps

## Build Process

Version 1:
Created initial Streamlit application.

Version 2:
Added Skill Gap Analyzer MCP tool.

Version 3:
Added Job Fit Scorer MCP tool.

Version 4:
Integrated Gemini 2.5 Flash Lite.

Version 5:
Added evaluation testing and failure cases.

Version 6:
Added external grounding through skills.csv.

Current Limitations

The current version executes MCP tools before passing results to Gemini.

Future work would implement a full tool-calling loop where Gemini autonomously decides when to invoke tools and how to use the returned results.

This would more closely align with a production MCP architecture.
