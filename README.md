# -PDF-Knowledge-Q-A-Bot

This project is a basic question-answering bot that uses CrewAI and its built-in PDFSearchTool to answer user questions about the content of a PDF file. It demonstrates how to build a simple agent that retrieves information from a PDF using semantic search.
--------------------------------------------------------------
🚀 Features

* Question-answering from any PDF document
* Uses semantic search to locate relevant answers
* User inputs questions dynamically
* Modular and easy to extend
* Built with CrewAI multi-agent framework
--------------------------------------------------------------
📌 How It Works

A PDF Expert Agent is defined with PDFSearchTool as its tool
A Task describes what question to answer, specifying the PDF path
A Crew coordinates the agent and task in a simple sequential flow
The agent uses semantic search on the PDF to extract relevant chunks and answer the question
--------------------------------------------------------------
🧩 Tech Stack

CrewAI
crewai-tools
Python
OpenAI API 
--------------------------------------------------------------
📌 Project Highlights
✅ Modular CrewAI agent and task design
✅ Easy to extend for other PDF use cases
✅ Clean user prompt-based question answering
✅ Example of how to integrate PDFSearchTool into a working flow
--------------------------------------------------------------
🤝 Contributions
Feel free to fork this repo and extend its features!
PRs and suggestions are welcome.
--------------------------------------------------------------
📄 License
This project is for educational and demonstration purposes.
Please check dependencies’ licenses before production use.











--------------------------------------------------------------
pdf_qa_bot/
│
├── tools/
│   └── pdf_tool.py
│
├── main.py
├── requirements.txt
├── sample.pdf   # Your PDF file
├── .env         # stores your OPENAI_API_KEY
└── README.md
