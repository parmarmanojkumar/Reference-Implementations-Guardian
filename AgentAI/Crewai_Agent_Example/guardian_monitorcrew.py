


guardian_base_url = "GUARDIAN_API_ENDPOINT"
guardian_api_KEY = "GUARDIAN_API_KEY"

from crewai import Crew
from guardian_api import GuardianAPIConfig, CheckResult
from typing import Any, Dict

class MonitoredCrew(Crew):
    def __init__(self, agents, tasks, guardian_config: GuardianAPIConfig = None, **kwargs):
        # Set default Guardian configuration if none is provided
        if guardian_config is None:
            guardian_config = GuardianAPIConfig(base_url=guardian_base_url, api_key=guardian_api_KEY)
        
        super().__init__(
            agents=agents,
            tasks=tasks,
            process='sequential',
            step_callback=self._guardian_step_callback_monitor,
            task_callback=self._guardian_task_callback_monitor,
            **kwargs
        )
        self._guardian_api = guardian_config

    def _guardian_step_callback_monitor(self, step_output) -> CheckResult:
        print("======Step Output Received========")
        print(step_output)
        check_result = self._guardian_api.check_input(step_output)
        print(f"Step Output Check Result: {check_result.approved}")
        if not check_result.approved:
            print(f"Step output rejected: {check_result.message}")
        return check_result

    def _guardian_task_callback_monitor(self, task_output) -> CheckResult:
        output_str = str(task_output) if not isinstance(task_output, str) else task_output
        print("======Task Output Received========")
        check_result = self._guardian_api.check_output(output_str)
        print(f"Task Output Check Result: {check_result.approved}")
        if not check_result.approved:
            print(f"Task output rejected: {check_result.message}")
        return check_result

    def _guardian_task_callback_block(self, task_output) -> CheckResult:
        output_str = str(task_output) if not isinstance(task_output, str) else task_output
        print("======Task Output Received========")
        check_result = self._guardian_api.check_output(output_str)
        print(f"Task Output Check Result: {check_result.approved}")
        if not check_result.approved:
            print(f"Task output rejected: {check_result.message}")
            raise ValueError("Output validation failed: inappropriate content")
        return check_result

    def _check_input(self, input_data: str) -> CheckResult:
        # Call Guardian API to validate input data
        return self._guardian_api.check_input(input_data)

    def _check_output(self, output_data: str) -> CheckResult:
        # Call Guardian API to validate output data
        return self._guardian_api.check_output(output_data)

    def kickoff(self, inputs: Dict[str, Any]) -> Any:
        # Pre-check input using Guardian
        input_str = str(inputs) if not isinstance(inputs, str) else inputs
        print("Input Received for Validation:", input_str)
        input_check_result = self._check_input(input_str)
        if not input_check_result.approved:
            print(f"User Input rejected: {input_check_result.message}")
            #raise ValueError(f"Input validation failed: {input_check_result.message}")

        # Execute normal kickoff with input validation complete
        print("Starting monitored crew kickoff...")
        result = super().kickoff(inputs=inputs)

        # Post-check output using Guardian
        output_str = str(result.raw) if not isinstance(result.raw, str) else result.raw
        output_check_result = self._check_output(output_str)
        if not output_check_result.approved:
            print(f"Crew output rejected: {output_check_result.message}")
            #raise ValueError(f"Output validation failed: {output_check_result.message}")

        return result
