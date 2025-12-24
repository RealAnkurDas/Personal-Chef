'''
A Personal chef agent with following features:-
- Uses Groq llm provider
- Has tavily search tool
- Has short term memory
'''

from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langchain.messages import HumanMessage
from typing import Dict, Any
from tavily import TavilyClient
from dotenv import load_dotenv

# Import environment variables at runtime
load_dotenv()

# Definig web search tool
tavily_client = TavilyClient()

@tool
def tavily_web_search(query: str) -> Dict[str, Any]:
    '''Search the web for information'''

    return tavily_client.search(query)

# Initializing the groq llm model
groq_model = init_chat_model(
    model = "llama-3.1-8b-instant",
    model_provider="groq"
)

# Defining system prompt for agent
system_prompt = '''
                You are a personal chef.\n
                You will search the web for recipes based on my available food items.\n
                You will then return each recipe with structured output in the following format:\n
                no. (The recipe number)\n
                name (The name of the recipe)\n
                time_hours (The time in hours needed to complete the recipe)\n
                url (The recipe url)\n
                steps (The steps of the recipe)\n\n
                For multiple found recipes, repeat the response structure for each recipe.
'''

# Defining agent with web search tool, system prompt and short term memory
chef_agent = create_agent(
    model = groq_model,
    tools = [tavily_web_search],
    system_prompt = system_prompt,
    checkpointer = InMemorySaver()
)

# Defining a thread id for session persistence
config = {"configurable": {"thread_id": "1"}}

while True:

    # Getting user input
    q = input("Enter available food items: ")

    # Invoke the agent
    response = chef_agent.invoke(
        {"messages": [HumanMessage(content = q)]},
        config
    )

    # print final AI response
    print(response["messages"][-1].content)
    print()

    if input("Exit? (y or n): ").lower() == 'y':
        print("Exiting...")
        break

    print()