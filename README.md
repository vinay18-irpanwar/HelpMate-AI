🚀 HelpMate AI – Customer Support Assistant

HelpMate AI is an internal AI-powered assistant built to support customer service teams. The application integrates a Large Language Model (LLM) with multiple tools to intelligently handle customer queries such as order tracking, shipping cost calculation, and web search.

📌 Features

🌐 Web Search – Uses Tavily Search to fetch up-to-date information.

📦 Order Status Lookup – Checks order status using a custom tool.

🚚 Shipping Cost Calculator – Calculates shipping cost based on weight and destination.

🤖 Smart Tool Selection – The LLM automatically decides which tool to use based on the user's query.

⚙️ Manual Tool Execution – The application executes the suggested tool and returns the final result.

🛠️ Tech Stack

Python

LangChain

Google Gemini (via langchain-google-genai)

Tavily Search API

Streamlit (for UI)

📂 Project Structure
├── app.py
├── requirements.txt
└── README.md
🔑 API Keys Required

You need:

Google API Key (Gemini)

Tavily API Key

These can be provided through:

Streamlit sidebar input
OR

.streamlit/secrets.toml file

📦 Installation

Clone the repository:

git clone <your-repo-url>
cd <your-repo-folder>

Create a virtual environment:

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

Install dependencies:

pip install -r requirements.txt
▶️ Run the Application
streamlit run app.py
🧠 Example Queries

Check order ORD123

Shipping cost for 5kg to india

Latest AI news

Who is PM of India

🎯 Project Goal

The goal of this project is to demonstrate how an LLM can intelligently decide when to call external tools and how those tools can be manually executed to produce accurate, real-world responses for customer support operations.

