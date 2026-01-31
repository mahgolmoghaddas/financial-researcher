Financial Researcher

A Python project that uses multiple AI agents to automate company research and produce a structured financial analysis report.

The goal of this project is to demonstrate how agent-based systems, LLM orchestration, and external tools can be combined into a clean, working backend application.

Why this project

I built this project to explore:

Multi-agent coordination using CrewAI

Practical use of LLMs for research and analysis (not chat)

Clean separation between research, analysis, and orchestration

Environment-safe API usage and backend-only execution

This is a backend-focused project designed to be readable, extensible, and easy to reason about.

What the system does

Given a company name as input, the system:

Gathers recent, relevant information using a research agent

Passes findings to an analysis agent for synthesis

Produces a written financial summary

Saves the output as a Markdown report

The system runs deterministically in a sequential pipeline so each step builds on the previous one.

Architecture overview

Agents

Research agent: information gathering via web search

Analysis agent: reasoning, summarization, and report writing

Tasks

Research task → data collection

Analysis task → synthesis and output

Orchestration

CrewAI manages agent execution order and context sharing

Agents are configured via YAML for clarity and easy iteration

Key engineering decisions

Backend-only design
API keys are never exposed to the client or frontend.

Config-driven agents
Agent behavior and prompts live in YAML files, not code.

Explicit environment handling
Environment variables are loaded safely using python-dotenv.

Tool isolation
External tools (web search) are injected per-agent rather than globally.

Project Structure:
<img width="508" height="252" alt="Screenshot 2026-01-31 at 2 38 52 PM" src="https://github.com/user-attachments/assets/6f57200b-5af5-42c4-b1d6-4852b567d7b0" />
Tech stack

Python

CrewAI (agent orchestration)

OpenAI API (LLM reasoning)

Serper API (web search)

python-dotenv

Running the project
crewai run

Or directly:

python -m financial_researcher.main

A report is generated at:

output/report.md
What this demonstrates

This project demonstrates:

Designing agent-based workflows

Using LLMs beyond chat interfaces

Managing external tools and APIs cleanly

Writing maintainable, config-driven Python applications

Building AI systems with clear execution boundaries

Possible extensions

Add more specialized agents (risk, ESG, macro)

Compare multiple companies in one run

Export reports to PDF

Integrate internal documents using RAG

Add a simple web UI on top of the backend

Author

Mahgol Moghaddas
Software Engineer
Montreal, Canada
