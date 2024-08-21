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
    event_type = data.get("event_type")
    location = data.get("location")
    time_frame = data.get("time_frame")
    
    # Use the extracted data to generate a query string
    user_input = f"Find me {event_type} events in {location} around {time_frame} time frame in 2024. Return back specific events."
    
    # Set memory for a specific thread
    config = {"configurable": {"thread_id": "rc45"}}

    # call the agent executor with the user input and configuration
    response = agent_executor.invoke({"messages": [("user", user_input)]}, config)

    response = response["messages"][-1].content

    return {"response": response}