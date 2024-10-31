import logging
import asyncio
import os
from dotenv import load_dotenv
import json

from autogen_agentchat import EVENT_LOGGER_NAME
from autogen_agentchat.logging import ConsoleLogHandler
from autogen_agentchat.agents import CodingAssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat, StopMessageTermination
from autogen_core.components.models import OpenAIChatCompletionClient
from monitor_round_robin_group_chat import MonitorRoundRobinGroupChat
from guardian_api import GuardianAPIConfig 

logger = logging.getLogger(EVENT_LOGGER_NAME)
logger.addHandler(ConsoleLogHandler())
logger.setLevel(logging.INFO)

# Load environment variables from the .env file
load_dotenv()

# Retrieve environment variables using os.getenv
guardian_api_key = os.getenv("GUARDIAN_API_KEY")
guardian_api_endpoint = os.getenv("GUARDIAN_API_ENDPOINT")

# Check if the environment variables are loaded correctly
if guardian_api_key is None or guardian_api_endpoint is None:
    logger.error("Failed to load environment variables. Please check your .env file.")
else:
    # Initialize Guardian API Config with loaded environment variables
    guardian_api_config = GuardianAPIConfig(api_key=guardian_api_key, base_url=guardian_api_endpoint)


# Run a monitored task






planner_agent = CodingAssistantAgent(
    "planner_agent",
    model_client=OpenAIChatCompletionClient(model="gpt-4o-mini"),
    description="A helpful assistant that can plan trips.",
    system_message="You are a helpful assistant that can suggest a travel plan for a user based on their request.",
)

local_agent = CodingAssistantAgent(
    "local_agent",
    model_client=OpenAIChatCompletionClient(model="gpt-4o-mini"),
    description="A local assistant that can suggest local activities or places to visit.",
    system_message="You are a helpful assistant that can suggest authentic and interesting local activities or places to visit for a user and can utilize any context information provided.",
)

language_agent = CodingAssistantAgent(
    "language_agent",
    model_client=OpenAIChatCompletionClient(model="gpt-4o-mini"),
    description="A helpful assistant that can provide language tips for a given destination.",
    system_message="You are a helpful assistant that can review travel plans, providing feedback on important/critical tips about how best to address language or communication challenges for the given destination. If the plan already includes language tips, you can mention that the plan is satisfactory, with rationale.",
)

travel_summary_agent = CodingAssistantAgent(
    "travel_summary_agent",
    model_client=OpenAIChatCompletionClient(model="gpt-4o-mini"),
    description="A helpful assistant that can summarize the travel plan.",
    system_message="You are a helpful assistant that can take in all of the suggestions and advice from the other agents and provide a detailed tfinal travel plan. You must ensure th b at the final plan is integrated and complete. YOUR FINAL RESPONSE MUST BE THE COMPLETE PLAN. When the plan is complete and all perspectives are integrated, you can respond with TERMINATE.",
)

group_chat = RoundRobinGroupChat([planner_agent, local_agent, language_agent, travel_summary_agent])
#group_chat = RoundRobinGroupChat([planner_agent, travel_summary_agent])
monitor_chat = MonitorRoundRobinGroupChat(
    group_chat, 
    guardian_api_config, 
    stop_on_violation=True, 
    input_checked=True, 
    verbose=True  # Enable verbose output for intermediate steps
)

async def main():
    # Use await inside an async function
    #result = await group_chat.run(task="Plan a 3 day trip to Nepal.", termination_condition=StopMessageTermination())
    result, validatedMsg = await monitor_chat.runMonitor(
        task="Plan a 3 day trip to Bhuj.", 
        termination_condition=StopMessageTermination()
    )
    
    print("="*50)
    # print (result)
    if hasattr(result, 'messages'):
        formatted_result = json.dumps([message.__dict__ for message in result.messages], indent=4)
        print("\n", formatted_result)
    else:
        print("\n", "No messages found in result.")
    print("="*50)
    print(validatedMsg)
    print("="*50)

# Run the main function
asyncio.run(main())