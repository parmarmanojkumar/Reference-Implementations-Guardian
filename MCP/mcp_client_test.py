import requests

# Base URL for your MCP server
MCP_SERVER_URL = "http://localhost:8000"  # Change the port if needed

def test_input_validation(input_text: str):
    url = f"{MCP_SERVER_URL}/validate_input"
    data = {"input_text": input_text}
    response = requests.post(url, json=data)
    return response.json()

def test_output_validation(output_text: str):
    url = f"{MCP_SERVER_URL}/validate_output"
    data = {"output_text": output_text}
    response = requests.post(url, json=data)
    return response.json()

def dummy_llm(prompt: str) -> str:
    """
    A dummy LLM function that simply echoes the prompt.
    Replace this with actual LLM API calls or functions as needed.
    """
    return f"LLM processed output based on: {prompt}"

def run_llm_application():
    # Simulate receiving user input.
    user_input = input("Enter your prompt: ")

    # Validate the user input with the guardrail MCP endpoint.
    input_validation_response = test_input_validation(user_input)
    print("Input Validation Response:", input_validation_response)

    if not input_validation_response.get("success", False):
        print("Input was rejected:", input_validation_response.get("content", [{}])[0].get("text"))
        return

    # Process the prompt through your LLM.
    llm_output = dummy_llm(user_input)
    print("Generated LLM Output:", llm_output)

    # Validate the LLM output with the guardrail MCP endpoint.
    output_validation_response = test_output_validation(llm_output)
    print("Output Validation Response:", output_validation_response)

    if not output_validation_response.get("success", False):
        print("LLM output was rejected:", output_validation_response.get("content", [{}])[0].get("text"))
    else:
        print("LLM output validated successfully!")
        print("Final Output:", llm_output)

if __name__ == "__main__":
    run_llm_application()