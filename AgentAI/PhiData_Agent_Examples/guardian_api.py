import requests
from tenacity import retry, stop_after_attempt, wait_fixed
from termcolor import colored

# Defining the Guardian API Client class
class GuardianAPIClient:
    def __init__(self, base_url, api_key=None):
        # Initialize the Guardian API Client with base URL and optional API key
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {'Content-Type': 'application/json'}
        if api_key:
            self.headers['Authorization'] = f'Bearer {api_key}'

    def _get(self, endpoint, params=None):
        # Helper function to send a GET request to the API with error handling
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error during GET request to {url} with params {params}: {str(e)}")
            raise

    def _post(self, endpoint, data=None, files=None):
        # Helper function to send a POST request to the API
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.post(url, headers=self.headers, json=data, files=files)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error during POST request to {url} with data {data}: {str(e)}")
            raise

    # Example: Configuration Endpoint
    def get_configuration(self):
        # Get configuration details from the API
        return self._get("/configuration")

    # Example: Dashboard Summary Endpoint
    def get_dashboard_summary(self):
        # Get dashboard summary from the API
        return self._get("/dashboard/summary")

    # Example: Query History Endpoint
    def get_query_history(self):
        # Get query history from the API
        return self._get("/dashboard/queryHistory")

    # Example: Chat API for App1
    def chat_app1(self, prompt):
        # Send a prompt to the chat endpoint and parse the response
        data = {"prompt": prompt}
        response = self._post("/chat/app1", data=data)
        return self.parse_chat_app1_response(response)

    def parse_chat_app1_response(self, response):
        # Parse the response from the chat API with error handling for missing keys
        try:
            parsed_response = {}
            for key, value in response.items():
                parsed_response[key] = value
            return parsed_response
        except AttributeError:
            print("Unexpected response structure from chat_app1 API. Expected a dictionary.")
            return {}

    # Example: Configure LLM for Llama
    def configure_llm_llama(self, metadata):
        # Configure LLM with provided metadata
        data = {"metadata": metadata}
        return self._post("/configureLLM/Llama", data=data)

    # Example: Configure Mode
    def configure_mode(self, mode):
        # Configure the mode of operation
        data = {"mode": mode}
        return self._post("/configureMode", data=data)

    # Check connectivity with the Guardian API endpoint
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def check_connectivity(self):
        # Check if the API endpoint is reachable with retry mechanism
        try:
            response = requests.get(f"{self.base_url}/configuration", headers=self.headers)
            if response.status_code == 200:
                print(colored("Successfully connected to Guardian API endpoint.", "green"))
                return True
            else:
                print(colored(f"Failed to connect to Guardian API endpoint. Status code: {response.status_code}", "red"))
                return False
        except requests.exceptions.RequestException as e:
            print(f"Error while checking connectivity: {str(e)}")
            raise


# Defining the check result class
class CheckResult:
    def __init__(self, approved: bool, message: str):
        # Initialize the result of a check with approved status and a message
        self.approved = approved
        self.message = message


# Defining the Guardian API configuration class
class GuardianAPIConfig:
    def __init__(self, api_key: str, base_url: str):
        # Initialize the Guardian API configuration with API key and base URL
        self.api_key = api_key
        self.base_url = base_url
        self.client = GuardianAPIClient(base_url=self.base_url, api_key=self.api_key)
        # Check connectivity during initialization
        if not self.client.check_connectivity():
            raise ConnectionError("Unable to connect to Guardian API endpoint.")

    def check_input(self, prompt: str):
        # Validate the prompt before making an API call
        if not prompt or not isinstance(prompt, str) or len(prompt.strip()) == 0:
            return CheckResult(approved=False, message="Invalid input prompt provided.")
        # Check the input prompt for policy violations using the Guardian API
        response = self.client.chat_app1(prompt)
        policy_violated = response.get("policy_violated", False)
        policy_violated_reason = response.get("ip_op_blocked", "")
        policy_type = response.get("policy_type", "")
        if policy_violated and policy_violated_reason == "InputBlocked":
            return CheckResult(approved=False, message=f"Input contains inappropriate content. Policy violated: {policy_type}")
        return CheckResult(approved=True, message="Input approved.")

    def check_output(self, output: str):
        # Validate the output before making an API call
        if not output or not isinstance(output, str) or len(output.strip()) == 0:
            return CheckResult(approved=False, message="Invalid model output provided.")
        # Check the output generated by the model for policy violations using the Guardian API
        response = self.client.chat_app1(output)
        policy_violated = response.get("policy_violated", False)
        policy_type = response.get("policy_type", "")
        if policy_violated:
            return CheckResult(approved=False, message=f"Output contains inappropriate content. Policy violated: {policy_type}")
        return CheckResult(approved=True, message="Output approved.")
    
    