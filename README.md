# Financial Researcher


Financial Researcher is a Python project that uses multiple AI agents to research a company and generate a concise financial analysis report.


You provide a company name (for example, *Apple*), and the system gathers relevant information, analyzes it, and saves a written report to a file. The project is designed as a backend research assistant, not a trading or prediction system.


---


## Purpose


This project was built to explore practical, real-world use of agent-based systems for research tasks. The main goals are to:


- Coordinate multiple AI agents in a clear and predictable workflow  
- Separate research and analysis responsibilities  
- Use large language models for structured reasoning rather than chat  
- Keep prompts and configuration out of application logic  


It also serves as a clean, readable example of an AI-powered backend application.


---


## What it does


For a given company name, the system:


1. Collects recent and relevant information from the web  
2. Summarizes key financial and market points  
3. Produces a short, structured analysis  
4. Saves the result as a Markdown report  


The workflow runs sequentially so each step builds on the results of the previous one.


---


## How it works


The project uses **CrewAI** to orchestrate two agents:


- **Research agent**  
  Gathers information using web search tools and public sources.


- **Analysis agent**  
  Reviews the research output and writes the final report.


Agent roles and task instructions are defined in YAML files, which makes the system easy to adjust and extend without changing core code.


---


## Project structure



financial-researcher/
├── src/
│ └── financial_researcher/
│ ├── crew.py # Agent and crew setup
│ ├── main.py # Application entry point
│ └── config/
│ ├── agents.yaml # Agent definitions
│ └── tasks.yaml # Task instructions
├── output/
│ └── report.md # Generated report
├── .env # API keys (not committed)
└── README.md



---


## Technologies used


- Python  
- CrewAI  
- OpenAI API  
- Serper API (web search)  
- python-dotenv  


---


## Running the project


After setting the required environment variables, run:


```bash
crewai run

Or:

python -m financial_researcher.main

The generated report will be saved to:

output/report.md
Configuration

Agent behavior and prompts are defined in agents.yaml

Task instructions are defined in tasks.yaml

API keys are loaded using environment variables

This approach keeps the application logic small, readable, and easy to maintain.

Notes

The project requires valid API keys for external services.

API usage may incur costs depending on volume.

Output quality depends on publicly available information and model responses.

Author

Mahgol Moghaddas
Software Engineer
Montreal, Canada
