from phi.agent import Agent, RunResponse
from guardian_api import GuardianAPIConfig  # Import the GuardianAPIConfig class
from termcolor import colored
from phi.utils.pprint import pprint_run_response
import time

class GuardedAgentWorkflow:
    def __init__(self, agent: Agent, guardian_config: GuardianAPIConfig, prompts: list, guardrail_config: dict, verbose_flag=False):
        self.agent = agent
        self.guardian_config = guardian_config
        self.prompts = prompts
        self.guardrail_config = guardrail_config  # Configuration for Guardian guardrails
        self.verbose_flag = verbose_flag

    def process_prompt(self, user_prompt: str):
        print(colored("=" * 50, "blue"))
        if not user_prompt:
            print("No prompt provided in inputs.")
            return {"status": "error", "message": "No prompt provided."}
        
        print(colored(f"Received user prompt: {user_prompt}", "cyan"))
        return {"status": "success", "user_prompt": user_prompt}

    def guardian_input_check(self, user_prompt: str):
        if self.guardrail_config.get("active", False) and self.guardrail_config.get("input_side", False):
            if self.verbose_flag:
                print("AIShield Guardian check on Input started.")
            input_check_result = self.guardian_config.check_input(user_prompt)
            if self.verbose_flag:
                print("AIShield Guardian check on Input completed.")
            
            if not input_check_result.approved:
                return {"status": "error", "message": f"Input check failed: {input_check_result.message}"}
            else:
                print(colored(f"Check passed for input prompt: {input_check_result.message}", "green"))
                return {"status": "success", "message": "Input check passed"}
        return {"status": "success", "message": "Input check skipped (inactive)"}

    def run_agent(self, user_prompt: str):
        if self.verbose_flag:
            print(colored(f"Passing prompt to Financial agent: {user_prompt}", "grey"))
        
        agent_result: RunResponse = self.agent.run(user_prompt, stream=False)
        agent_output = agent_result.content
        
        if self.verbose_flag:
            print(colored(f"Received output from Financial agent model: {agent_output}", "grey"))
        
        return {"status": "success", "agent_output": agent_output, "agent_result": agent_result}

    def guardian_output_check(self, agent_output: str):
        if self.guardrail_config.get("active", False) and self.guardrail_config.get("output_side", False):
            if self.verbose_flag:
                print("AIShield Guardian check on Output started.")
            
            output_check_result = self.guardian_config.check_output(agent_output)
            
            if self.verbose_flag:
                print("AIShield Guardian check on Output completed.")
    
            if not output_check_result.approved:
                return {"status": "error", "message": f"Output check failed: {output_check_result.message}"}
            else:
                print(colored(f"Check passed for model output: {output_check_result.message}", "green"))
                return {"status": "success", "message": "Output check passed"}
        return {"status": "success", "message": "Output check skipped (inactive)"}

    def display_result(self, agent_result: RunResponse):
        # Step 6: Return model output
        pprint_run_response(agent_result, markdown=True, show_time=True)
        return {"status": "success", "message": "Result displayed"}

    def run(self):
        for user_prompt in self.prompts:
            # Step 1: Process Prompt
            process_response = self.process_prompt(user_prompt)
            if process_response["status"] == "error":
                print(colored(process_response["message"], "red"))
                continue

            # Step 2: Guardian Input Check
            input_check_response = self.guardian_input_check(process_response["user_prompt"])
            if input_check_response["status"] == "error":
                print(colored(input_check_response["message"], "red"))
                continue

            # Step 3: Run Agent
            agent_response = self.run_agent(process_response["user_prompt"])
            if agent_response["status"] == "error":
                print(colored(agent_response["message"], "red"))
                continue

            # Step 4: Guardian Output Check
            output_check_response = self.guardian_output_check(agent_response["agent_output"])
            if output_check_response["status"] == "error":
                print(colored(output_check_response["message"], "red"))
                continue

            # Step 5: Display Result
            display_response = self.display_result(agent_response["agent_result"])
            if display_response["status"] == "error":
                print(colored(display_response["message"], "red"))
                continue

            time.sleep(1)
            

def guardian_config_check_function(guardrail_config):
    """
    Function to check and print the status of the AIShield Guardian guardrail configuration.
    """
    print(colored("=" * 90, "cyan"))
    if guardrail_config.get("active") == False or (not guardrail_config.get("input_side") and not guardrail_config.get("output_side")):
        print(colored("AIShield Guardian Guardrails are completely inactive and results might be disturbing.", "red"))
    elif not guardrail_config.get("input_side") or not guardrail_config.get("output_side"):
        print(colored("AIShield Guardian Guardrails are partially active and results might be disturbing.", "yellow"))
    else:
        print(colored("AIShield Guardian Guardrails are active on both input and output sides.", "green"))
    print(colored("=" * 90, "cyan"))