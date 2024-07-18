from typing import Dict
from fastapi import FastAPI
from langgraph.checkpoint.sqlite import SqliteSaver

from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.prebuilt import create_react_agent

from dotenv import load_dotenv
load_dotenv()

###########################
### ReAct Search Agent ####
###########################

# Create the agent with memory and search tool
memory = SqliteSaver.from_conn_string(":memory:")
model = ChatOpenAI(model='gpt-4o')
search = TavilySearchResults(max_results=2)
tools = [search]
agent_executor = create_react_agent(model, tools, checkpointer=memory)


###########################
###   Nutrition Agent  ####
###########################
## TBD



###########################
###    App Endpoint    ####
###########################

app = FastAPI()

@app.post("/nutrition")
def generate_nutrition():
    return {"response": "WIP"}

@app.post("/event")
def generate_events(data: Dict):
    # TO DO - Use the provided data to find events

    response = 'tbd'
    return {"response": response}