import socket
import json
from termcolor import colored

class GuardianAPIClient:
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.headers = {'Content-Type': 'application/json'}
        if api_key:
            self.headers['Authorization'] = f'Bearer {api_key}'

    def _parse_url(self, url):
        """Parse the base URL and endpoint to extract host and port."""
        if url.startswith("http://"):
            url = url[len("http://"):]
        elif url.startswith("https://"):
            raise ValueError("HTTPS is not supported in this implementation")
        
        parts = url.split("/", 1)
        host_port = parts[0]
        path = f"/{parts[1]}" if len(parts) > 1 else "/"
        
        if ":" in host_port:
            host, port = host_port.split(":")
            port = int(port)
        else:
            host, port = host_port, 80
        
        return host, port, path

    def _send_request(self, method, endpoint, data=None):
        """Send an HTTP request using sockets."""
        host, port, path = self._parse_url(f"{self.base_url}{endpoint}")
        body = data.encode('utf-8') if data else b""

        # Build HTTP request
        request = f"{method} {path} HTTP/1.1\r\n"
        request += f"Host: {host}\r\n"
        for header, value in self.headers.items():
            request += f"{header}: {value}\r\n"
        request += f"Content-Length: {len(body)}\r\n"
        request += "\r\n"
        if body:
            request += body.decode('utf-8')

        # Open socket connection
        with socket.create_connection((host, port), timeout=10) as sock:  # Added timeout
            sock.sendall(request.encode('utf-8'))  # Send the request
            response = b""
            while True:
                chunk = sock.recv(4096)
                if not chunk:
                    break
                response += chunk

        # Decode and parse response
        response = response.decode('utf-8')
        response_headers, response_body = response.split("\r\n\r\n", 1)
        return json.loads(response_body)  # Parse JSON response

    def _get(self, endpoint, params=None):
        """Perform a GET request."""
        query = ""
        if params:
            query = "?" + "&".join(f"{k}={v}" for k, v in params.items())
        return self._send_request("GET", f"{endpoint}{query}")

    def _post(self, endpoint, data=None):
        """Perform a POST request."""
        return self._send_request("POST", endpoint, data)

    def get_configuration(self):
        """Get configuration details from the API."""
        return self._get("/configuration")

    def get_dashboard_summary(self):
        """Get dashboard summary from the API."""
        return self._get("/dashboard/summary")

    def get_query_history(self):
        """Get query history from the API."""
        return self._get("/dashboard/queryHistory")

    def chat_app1(self, prompt):
        """Send a prompt to the chat endpoint and parse the response."""
        data = json.dumps({"prompt": prompt})  # Use JSON.dumps for proper formatting
        response = self._post("/chat/app1", data)
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

    def configure_llm_llama(self, metadata):
        """Configure LLM with provided metadata."""
        data = json.dumps({"metadata": metadata})
        return self._post("/configureLLM/Llama", data)

    def configure_mode(self, mode):
        """Configure the mode of operation."""
        data = json.dumps({"mode": mode})
        return self._post("/configureMode", data)
    
    def check_connectivity(self):
        """Check if the API endpoint is reachable."""
        try:
            # Extract host and port from the base URL
            host, port, _ = self._parse_url(self.base_url)

            # Attempt to establish a socket connection
            with socket.create_connection((host, port), timeout=5):
                print(colored(f"Successfully connected to {host}:{port}", 'green'))
                return True
        except (socket.timeout, socket.error) as e:
            print(colored(f"Failed to connect to {self.base_url}. Error: {e}",'red'))
            return False

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