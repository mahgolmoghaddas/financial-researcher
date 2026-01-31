#!/usr/bin/env python
# src/financial_researcher/main.py
import os
from .crew import ResearchCrew
from dotenv import load_dotenv
from openai import OpenAI
import os


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

def run():
    """
    Run the research crew.
    """
    inputs = {
        'company': 'Apple'
    }

    # Create and run the crew
    result = ResearchCrew().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL REPORT ===\n\n")
    print(result.raw)

    print("\n\nReport has been saved to output/report.md")

if __name__ == "__main__":
    run()