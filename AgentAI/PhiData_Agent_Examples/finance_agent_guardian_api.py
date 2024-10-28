from phi.agent import Agent
from phi.model.ollama import Ollama
from phi.tools.yfinance import YFinanceTools
from guardian_api import GuardianAPIConfig  # Import the GuardianAPIConfig class
from agent_workflow_guardrail import GuardedAgentWorkflow, guardian_config_check_function
from termcolor import colored
from phi.tools.duckduckgo import DuckDuckGo



# Defining the Financial Analyst agent
agent_financial_analyst = Agent(
    name="Financial Analyst Agent",
    model=Ollama(id="llama3.2:1b"),
    role="Search the financial information for stocks",
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=False,
    description="You are an investment analyst that researches stocks and helps users make informed decisions.",
    instructions=["Use tables to display data where possible."],
    markdown=True,
    debug_mode=False,
)

# Defining the Financial Analyst agent
agent_financial_analyst_with_web = Agent(
    name="Financial Analyst Agent",
    model=Ollama(id="llama3.2:1b"),
    role="Search the financial information for stocks",
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=False,
    description="You are an investment analyst that researches stocks and helps users make informed decisions.",
    instructions=["Use tables to display data where possible."],
    markdown=True,
    debug_mode=False,
)

# Guardian SDK configuration
base_url = "GUARDIAN_API_ENDPOINT"
guardian_config = GuardianAPIConfig(base_url=base_url, api_key="GUARDIAN_API_KEY")

# Guardian guardrail configuration (active/inactive, input/output side)
guardrail_config = {
    "active": False,       # Set to False to disable Guardian checks
    "input_side": True,    # Set to True to enable Guardian input check
    "output_side": True   # Set to True to enable Guardian output check
}
#Guardrail configuration print
guardian_config_check_function(guardrail_config)


# User prompts
user_prompts = [
    "Can you provide an analysis of Tesla (TSLA) stock performance over the last year? Please include key trends, significant events that influenced the stock, and an assessment of how broader market conditions or Tesla's own business developments contributed to its performance.",
    "Given the potential outcome of the 2024 U.S. election, specifically a Trump presidency, what general observations can you make about its possible impact on Tesla (TSLA) stocks? Could you provide some hypotheses and recommendations based on historical trends, expected economic policies, and potential market reactions?",
    "Considering the potential developments in the defense industry, particularly the building of advanced weapons and smart bomb, how might this affect Tesla (TSLA) stocks? Could you provide general observations and potential hypotheses on how such technological advancements and geopolitical factors could impact TSLA, directly or indirectly?"
]

# Running the workflow
workflow = GuardedAgentWorkflow(agent_financial_analyst, guardian_config, user_prompts, guardrail_config, verbose_flag=False)
workflow.run()
