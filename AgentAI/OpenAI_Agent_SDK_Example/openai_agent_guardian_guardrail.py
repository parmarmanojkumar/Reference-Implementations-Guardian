from pydantic import BaseModel
import os
import asyncio
from dotenv import load_dotenv

# Import necessary types and decorators from the OpenAI Agent SDK
from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    OutputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    input_guardrail,
    output_guardrail,
)

# -----------------------------------------------------------------------------
# Instantiate the OpenAI API Configuration
# -----------------------------------------------------------------------------

load_dotenv()  # Loads variables from .env into os.environ


# -----------------------------------------------------------------------------
# Instantiate the Guardian API Configuration
# -----------------------------------------------------------------------------

# Import GuardianAPIConfig from your guardian_api module
from guardian_api import GuardianAPIConfig

guardian_config = GuardianAPIConfig(
    api_key=os.getenv("GUARDIAN_API_KEY", "your_api_key_here"),
    base_url=os.getenv("GUARDIAN_BASE_URL", "https://api.your-guardian-domain.com"),
)



# -----------------------------------------------------------------------------
# Define Pydantic Model for Guardrail Check Output
# -----------------------------------------------------------------------------
class GuardianCheckOutput(BaseModel):
    approved: bool
    message: str

# -----------------------------------------------------------------------------
# Define a Message Output Model (for the agent’s output)
# -----------------------------------------------------------------------------
class MessageOutput(BaseModel):
    response: str

# -----------------------------------------------------------------------------
# Custom Input Guardrail Function using AIShield Guardian API
# -----------------------------------------------------------------------------
@input_guardrail
async def aishield_guardian_input_guardrail(
    ctx: RunContextWrapper[None], agent: Agent, input: str
) -> GuardrailFunctionOutput:
    loop = asyncio.get_running_loop()
    # Assume the input is always a text string.
    result = await loop.run_in_executor(None, guardian_config.check_input, input)
    return GuardrailFunctionOutput(
        output_info=GuardianCheckOutput(approved=result.approved, message=result.message),
        tripwire_triggered=not result.approved,
    )

# -----------------------------------------------------------------------------
# Custom Output Guardrail Function using AIShield Guardian API
# -----------------------------------------------------------------------------
@output_guardrail
async def aishield_guardian_output_guardrail(
    ctx: RunContextWrapper, agent: Agent, output: MessageOutput
) -> GuardrailFunctionOutput:
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, guardian_config.check_output, output.response)
    return GuardrailFunctionOutput(
        output_info=GuardianCheckOutput(approved=result.approved, message=result.message),
        tripwire_triggered=not result.approved,
    )

# -----------------------------------------------------------------------------
# Define the Main Agent using the Custom AIShield Guardian Guardrails
# -----------------------------------------------------------------------------
agent = Agent(
    name="Customer support agent",
    instructions="You are a customer support agent. You help customers with their questions.",
    input_guardrails=[aishield_guardian_input_guardrail],
    output_guardrails=[aishield_guardian_output_guardrail],
    output_type=MessageOutput,
)

# -----------------------------------------------------------------------------
# Example Main Function to Test the Guardrail Integration
# -----------------------------------------------------------------------------
async def main():
    test_prompt = "I'm considering applying for a ACME card because their rewards seem better. How does it compare to ZEX Credit card?"
    try:
        result = await Runner.run(agent, test_prompt)
        print("Guardrail did not trip. Final output:", result.final_output.response)
    except InputGuardrailTripwireTriggered:
        print("Input guardrail tripped: Inappropriate input detected.")
    except OutputGuardrailTripwireTriggered:
        print("Output guardrail tripped: Inappropriate output detected.")

if __name__ == "__main__":
    asyncio.run(main())