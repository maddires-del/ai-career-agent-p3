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
