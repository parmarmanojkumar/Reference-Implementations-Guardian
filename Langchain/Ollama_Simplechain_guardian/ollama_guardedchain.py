from langchain.chains.base import Chain
from langchain_ollama.llms import OllamaLLM
from guardian_api import GuardianAPIConfig  # Import the GuardianAPIConfig class
from termcolor import colored
from pydantic import Field
import requests

# Defining the chain
class GuardedOllamaChain(Chain):
    ollama_model: OllamaLLM = Field(...)
    guardian_config: GuardianAPIConfig = Field(...)

    @property
    def input_keys(self):
        # Defines the expected input keys for the chain
        return ["prompt"]

    @property
    def output_keys(self):
        # Defines the expected output keys for the chain
        return ["response"]

    def _call(self, inputs):
        user_prompt = inputs.get("prompt")
        if not user_prompt:
            # If no prompt is provided, return an error response
            print("No prompt provided in inputs.")
            return {"response": "No prompt provided."}
        print(colored(f"Received user prompt: {user_prompt}", "cyan"))

        # Step 2: Check input prompt with Guardian API check
        print("AIShield Guardian check on Input started.")
        input_check_result = self.guardian_config.check_input(user_prompt)
        print("AIShield Guardian check on Input completed.")
        if not input_check_result.approved:
            # If the prompt is not approved, return the check message
            print(colored(f"Check failed for input prompt: {input_check_result.message}", "red"))
            return {"response": f"Input check failed: {input_check_result.message}"}
        else:
            print(colored(f"Check passed for input prompt: {input_check_result.message}", "green"))

        # Step 3: Pass input prompt to Ollama model with error handling
        try:
            print(colored(f"Passing prompt to Ollama model: {user_prompt}", "grey"))
            ollama_result = self.ollama_model.generate([user_prompt])
            ollama_output = ollama_result.generations[0][0].text
            print(colored(f"Received output from Ollama model: {ollama_output}", "grey"))
        except requests.exceptions.RequestException as e:
            # Handle any exceptions that occur during model generation related to network issues
            error_message = f"Network error during model generation: {str(e)}"
            print(error_message)
            return {"response": error_message}
        except TimeoutError as e:
            # Handle timeout-specific errors
            error_message = f"Timeout error during model generation: {str(e)}"
            print(error_message)
            return {"response": error_message}
        except Exception as e:
            # Handle other general exceptions that may occur
            error_message = f"Error during model generation: {str(e)}"
            print(error_message)
            return {"response": error_message}

        # Step 5: Check Ollama model's output with Guardian API check
        print("AIShield Guardian check on Output started.")
        output_check_result = self.guardian_config.check_output(ollama_output)
        print("AIShield Guardian check on Output completed.")
        if not output_check_result.approved:
            # If the model output is not approved, return the check message
            print(colored(f"Check failed for model output: {output_check_result.message}", "red"))
            return {"response": f"Output check failed: {output_check_result.message}"}
        else:
            print(colored(f"Check passed for model output: {output_check_result.message}", "green"))

        # Step 6: Return model output
        print(colored(f"Final response to user: {ollama_output}", "cyan"))
        return {"response": ollama_output}