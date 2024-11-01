import json
import logging
from guardian_api import GuardianAPIConfig, CheckResult  # Assuming guardian_api module is correctly set up
from autogen_agentchat.teams import RoundRobinGroupChat

logger = logging.getLogger(__name__)

class MonitorRoundRobinGroupChat:
    def __init__(self, group_chat: RoundRobinGroupChat, guardian_api_config: GuardianAPIConfig, stop_on_violation: bool = False, input_checked: bool = True, verbose: bool = False):
        """
        Initialize the MonitorRoundRobinGroupChat.

        :param group_chat: The RoundRobinGroupChat instance to monitor.
        :param guardian_api_config: The GuardianAPIConfig instance for input/output checks.
        :param stop_on_violation: Whether to stop execution if a validation violation is detected.
        :param input_checked: Whether to perform input validation before running the group chat.
        :param verbose: Whether to print intermediate states.
        """
        self.group_chat = group_chat
        self.guardian_api_config = guardian_api_config
        self.stop_on_violation = stop_on_violation
        self.input_checked = input_checked
        self.verbose = verbose

    def validate_input(self, input_text: str) -> bool:
        """Synchronous input validation with GuardianAPI, with error handling."""
        try:
            check_result = self.guardian_api_config.check_input(input_text)
            if not check_result.approved:
                logger.warning(f"Input validation violation: {check_result.message}")
                if self.verbose:
                    print(f"Validation failed for input: {check_result.message}")
                return False
            logger.info("Input validated successfully.")
            if self.verbose:
                print("Input validated successfully.")
            return True
        except Exception as e:
            logger.error(f"Failed to validate input with GuardianAPI: {str(e)}")
            if self.verbose:
                print(f"Error during input validation: {str(e)}")
            return False

    def validate_output(self, output_text: str) -> bool:
        """Synchronous output validation with GuardianAPI, with error handling."""
        try:
            check_result = self.guardian_api_config.check_output(output_text)
            if not check_result.approved:
                logger.warning(f"Output validation violation: {check_result.message}")
                if self.verbose:
                    print(f"Validation failed for output: {check_result.message}")
                return False
            logger.info("Output validated successfully.")
            if self.verbose:
                print("Output validated successfully.")
            return True
        except Exception as e:
            logger.error(f"Failed to validate output with GuardianAPI: {str(e)}")
            if self.verbose:
                print(f"Error during output validation: {str(e)}")
            return False

    async def runMonitor(self, task: str, termination_condition):
        """
        Run the group chat task with input and output validation monitoring.

        :param task: The task to execute.
        :param termination_condition: Termination condition to stop the task.
        """
        # Perform input validation if input_checked is True
        if self.input_checked:
            input_valid = self.validate_input(task)
            if not input_valid and self.stop_on_violation:
                logger.error("Execution stopped due to input validation failure.")
                if self.verbose:
                    print("Execution stopped due to input validation failure.")
                return

        # Run the group chat and handle potential errors
        try:
            result = await self.group_chat.run(task=task, termination_condition=termination_condition)
        except Exception as e:
            logger.error(f"Error during group chat execution: {str(e)}")
            if self.verbose:
                print(f"Group chat execution failed: {str(e)}")
            return

        # Collect and validate intermediate messages, skipping the first message if input was validated
        validated_messages = []
        start_index = 1 if self.input_checked else 0  # Skip first message if input was validated

        for idx, message in enumerate(result.messages[start_index:], start=start_index):
            if self.verbose:
                print(f"Processing message {idx}: {message.content}")
            output_valid = self.validate_output(message.content)
            if output_valid or not self.stop_on_violation:
                validated_messages.append(message)
            elif self.stop_on_violation:
                logger.error("Execution stopped due to output validation failure.")
                if self.verbose:
                    print("Execution stopped due to output validation failure.")
                return

        # Output the validated result as JSON for structured review
        try:
            formatted_result = json.dumps([message.__dict__ for message in validated_messages], indent=4)
            if self.verbose:
                print("\nValidated Group Chat Result:\n", formatted_result)
            return result, validated_messages
        except (TypeError, ValueError) as e:
            logger.error(f"Failed to format the validated messages: {str(e)}")
            if self.verbose:
                print(f"Error in formatting output: {str(e)}")
            return None