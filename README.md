Financial Researcher

Financial Researcher is a Python project that uses multiple AI agents to research a company and generate a short financial analysis report.

You provide a company name (for example, Apple), and the system collects relevant information, analyzes it, and saves a written report to a file. The project is designed as a backend research assistant rather than a trading or prediction tool.

Purpose

This project was built to explore practical use of agent-based systems for research tasks, with a focus on:

Coordinating multiple AI agents in a clear workflow

Separating research and analysis responsibilities

Using LLMs for structured reasoning instead of chat

Keeping configuration and prompts out of application code

It also serves as a clean, readable example of an AI-powered backend application.

What it does

For a given company name, the system:

Gathers recent and relevant information from the web

Reviews and summarizes key financial and market points

Produces a short, structured analysis

Saves the result as a Markdown report

The workflow runs sequentially so each step builds on the previous one.

How it works

The project uses CrewAI to orchestrate two agents:

Research agent
Responsible for gathering information using web search tools.

Analysis agent
Reviews the research output and writes the final report.

Agent roles and task instructions are defined in YAML files, making it easy to adjust behavior without changing code.

Project structure


<img width="553" height="286" alt="Screenshot 2026-01-31 at 2 48 01 PM" src="https://github.com/user-attachments/assets/14a8da98-34a9-4d54-a9aa-9bdb2a31a8d9" />


Python

CrewAI

OpenAI API

Serper API (web search)

python-dotenv

Running the project

After setting your environment variables, run:

crewai run

Or:

python -m financial_researcher.main

The generated report will be saved to:

output/report.md
Configuration

Agent behavior and prompts are defined in agents.yaml

Task instructions are defined in tasks.yaml

API keys are loaded from environment variables

This setup keeps the application logic small and easy to maintain.

Notes

The project requires valid API keys for external services.

API usage may incur costs depending on usage.

Output quality depends on available public information and model responses.

Author

Mahgol Moghaddas
Software Engineer
Montreal, Canada
