from fastmcp import McpServer, Tool, ToolResponse
from pydantic import BaseModel

# Import the Guardian API configuration directly from guardian_api.py
from guardian_api import GuardianAPIConfig

# Configuration parameters for AIShield Guardian API.
AISHIELD_API_URL = "your_guardian_api_endpoint_url"  # Base API URL.
AISHIELD_API_KEY = "your_api_key_here"  # Replace with your actual API key.

# Initialize the Guardian API configuration using the pre-built client.
guardian_api_config = GuardianAPIConfig(api_key=AISHIELD_API_KEY, base_url=AISHIELD_API_URL)

# Initialize the MCP server.
server = McpServer(name="GuardrailServer", version="1.0.0")

# Define Pydantic schemas for input/output payload validation.
class InputSchema(BaseModel):
    input_text: str

class OutputSchema(BaseModel):
    output_text: str

# Input Guardrail Tool: validates incoming user input.
@server.tool(name="validate_input", description="Validates user input against safety policies.", schema=InputSchema)
def validate_input(input_text: str) -> ToolResponse:
    check = guardian_api_config.check_input(input_text)
    if not check.approved:
        return ToolResponse(
            content=[{"type": "text", "text": f"Input rejected: {check.message}"}],
            success=False,
        )
    return ToolResponse(
        content=[{"type": "text", "text": "Input is valid."}],
        success=True,
    )

# Output Guardrail Tool: validates generated LLM output.
@server.tool(name="validate_output", description="Validates LLM generated output against safety policies.", schema=OutputSchema)
def validate_output(output_text: str) -> ToolResponse:
    check = guardian_api_config.check_output(output_text)
    if not check.approved:
        return ToolResponse(
            content=[{"type": "text", "text": f"Output rejected: {check.message}"}],
            success=False,
        )
    return ToolResponse(
        content=[{"type": "text", "text": "Output is valid."}],
        success=True,
    )

if __name__ == "__main__":
    print("Starting Guardrail MCP Server...")
    server.run()