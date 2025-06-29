from crewai import Agent, Task, Crew, Process
from tools.pdf_tool import pdf_tool
from dotenv import load_dotenv
import os

load_dotenv()

# Create the agent
pdf_agent = Agent(
    role="PDF Expert",
    goal="Answer user questions about the machine learning PDF document.",
    backstory="An expert at reading PDF documents and retrieving information.",
    tools=[pdf_tool],
    allow_delegation=False
)

# Get user question
question = input("❓ Enter your question about the PDF: ")

# Create the task
task = Task(
    description=(
        f"Use Search a PDF's content tool with the query: '{question}' "
        f"and the PDF path: 'sample.pdf'. Return a clear, relevant answer."
    ),
    expected_output="A direct and accurate answer extracted from the PDF.",
    agent=pdf_agent
)

# Create the crew
crew = Crew(
    agents=[pdf_agent],
    tasks=[task],
    process=Process.sequential,
    verbose=True
)

# Run
result = crew.kickoff()
print("\n✅ Answer:\n", result)
