
📊 Financial Researcher

AI-powered financial research & analysis using autonomous agents

Financial Researcher is an AI-driven research system built with CrewAI that automates company analysis by coordinating multiple specialized agents. It gathers up-to-date information, performs structured analysis, and generates a clean, shareable report — all with minimal human input.

✨ What This Project Does

Given a company name (e.g. Apple), the system:

🔎 Researches the company using web search and LLM reasoning

📈 Analyzes financial, market, and strategic signals

📝 Generates a structured report in Markdown format

💾 Saves the final output for easy sharing and review

This makes it useful for:

Investment research

Market intelligence

Competitive analysis

Strategy & business insights

Rapid due-diligence workflows

🧠 How It Works (High Level)

The system uses a multi-agent architecture:

Agents

Researcher Agent

Gathers information from the web

Uses search tools for real-world data

Analyst Agent

Interprets findings

Produces structured insights and conclusions

Tasks

Research Task → data collection

Analysis Task → synthesis + reporting

Agents collaborate sequentially to ensure accuracy and logical flow.

🏗️ Architecture
User Input (Company Name)
        ↓
Research Agent (Web + LLM)
        ↓
Analysis Agent (Reasoning + Synthesis)
        ↓
Final Report (output/report.md)
📁 Project Structure
financial-researcher/
├── src/
│   └── financial_researcher/
│       ├── crew.py          # Agent & crew definitions
│       ├── main.py          # Entry point
│       └── config/
│           ├── agents.yaml  # Agent behavior & roles
│           └── tasks.yaml   # Task definitions
├── output/
│   └── report.md            # Generated research report
├── .env                     # API keys (not committed)
├── pyproject.toml
└── README.md
⚙️ Tech Stack

Python

CrewAI – multi-agent orchestration

OpenAI API – LLM reasoning & generation

Serper API – real-time web search

dotenv – environment management

🚀 Getting Started
1️⃣ Clone the repository
git clone https://github.com/mahgolmoghaddas/financial-researcher.git
cd financial-researcher
2️⃣ Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Set environment variables

Create a .env file in the project root:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
SERPER_API_KEY=xxxxxxxxxxxxxxxx

⚠️ Never commit .env to GitHub.

5️⃣ Run the project
crewai run

Or directly:

python -m financial_researcher.main
📄 Output

After execution, the final report is saved to:

output/report.md

The report is:

Human-readable

Easy to share

Ready for presentations or further analysis

🧩 Customization

You can easily adapt this system by:

Changing agent behavior in agents.yaml

Modifying task prompts in tasks.yaml

Adding new agents (e.g. Risk Analyst, ESG Analyst)

Integrating additional tools or APIs

🔐 Security Notes

API keys are loaded via environment variables

No secrets are stored in code

Designed for backend/server execution only

💡 Use Cases

Investment research automation

Startup or company profiling

Competitive landscape analysis

Financial due diligence

Internal research tooling

🛠️ Future Enhancements

PDF report generation

Multi-company comparison

Historical trend analysis

RAG integration with internal documents

Web UI / dashboard

👩‍💻 Author

Mahgol Moghaddas
Software Engineer | AI & Agentic Systems
📍 Montreal, Canada
