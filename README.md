# 🍳 AI Personal Chef Agent

A specialized AI agent that transforms your available ingredients into structured, professional recipes. Built with **LangChain**, **LangGraph**, and **Groq**, this agent searches the live web to find the best culinary matches for your pantry.

## 🚀 Features
- **Lightning Fast LLM**: Powered by Groq's `Llama-3.1-8b-instant` for near-instant responses.
- **Real-Time Web Search**: Integrates **Tavily AI** to browse the web for the latest recipes.
- **Conversational Memory**: Maintains context using `InMemorySaver`, allowing for follow-up questions.
- **Structured Output**: Automatically formats recipes with titles, cooking times, URLs, and steps.

## 🛠️ Tech Stack
- **Framework**: LangChain & LangGraph
- **LLM Provider**: Groq
- **Search Engine**: Tavily AI
- **Environment**: Python 3.10+

## 📋 Setup & Installation

1. **Install required packages:**
   ```bash
   pip install langchain langchain-groq python-dotenv tavily-python langgraph

2. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add your API keys:
   ```env
   GROQ_API_KEY=your_groq_key_here
   TAVILY_API_KEY=your_tavily_key_here

3. **Run the Agent:**
   ```bash
   python personal_chef.py

## 📖 How it Works
* **Tool Use**: The agent uses the `tavily_web_search` tool to find recipes based on your specific ingredient input.
* **System Prompt**: A specialized prompt ensures the LLM parses raw search results into a clean, specific schema (no., name, time, url, steps).
* **Memory**: Uses a `thread_id` to persist history, so the chef remembers what it suggested previously in the same session.