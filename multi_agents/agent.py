from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import os
from dotenv import load_dotenv

load_dotenv()

# Define the model
AGENT_MODEL = LiteLlm(model="openrouter/deepseek/deepseek-r1")

root_agent = Agent(
    name="root_agent",
    model=AGENT_MODEL,
    description="The main agent",
    instruction="You are tasked with dealing with general questions from everyday life"
)

# FIXED LINE: Use .model instead of .model_name
print(f"Agent initialized with model: {AGENT_MODEL.model}")