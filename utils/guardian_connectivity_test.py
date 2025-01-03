from guardian_api_socket import GuardianAPIConfig as SocketGuardianAPIConfig
from guardian_api import GuardianAPIConfig as APIGuardianAPIConfig

def test_socket_connectivity(base_url, api_key):
    print("\n--- Testing Socket Connectivity ---")
    # Initialize socket-based client with provided base URL
    socket_guardian_config = SocketGuardianAPIConfig(base_url=base_url, api_key=api_key)

    try:
        # Check connectivity using the socket-based client
        if socket_guardian_config.client.check_connectivity():
            print(f"Socket connectivity test passed: API is reachable at {base_url}.")
        else:
            print(f"Socket connectivity test failed: Unable to reach API at {base_url}.")
    except Exception as e:
        print(f"Socket connectivity test failed with exception: {e}")


def test_api_connectivity(base_url, api_key):
    print("\n--- Testing API Connectivity ---")
    # Initialize requests-based client with provided base URL
    api_guardian_config = APIGuardianAPIConfig(base_url=base_url, api_key=api_key)

    try:
        # Check connectivity using the requests-based client
        if api_guardian_config.client.check_connectivity():
            print(f"API connectivity test passed: API is reachable at {base_url}.")
        else:
            print(f"API connectivity test failed: Unable to reach API at {base_url}.")
    except Exception as e:
        print(f"API connectivity test failed with exception: {e}")


def test_input_check(base_url, api_key):
    print("\n--- Testing Input Check ---")
    user_prompt = "This is a prompt."

    # Initialize requests-based client with provided base URL
    api_guardian_config = APIGuardianAPIConfig(base_url=base_url, api_key=api_key)

    try:
        # Validate the user prompt using the API
        input_check_result = api_guardian_config.check_input(user_prompt)
        print(f"Input check result: Approved = {input_check_result.approved}, Message = {input_check_result.message}")

        # Extract policy violation details if input is not approved
        if not input_check_result.approved:
            parts = input_check_result.message.split("Policy violated:")
            if len(parts) > 1:
                msg = parts[1].strip()
                print(f"Policy Violation Details: {msg}")
    except Exception as e:
        print(f"Input check test failed with exception: {e}")


if __name__ == "__main__":
    # Provide the base URLs for testing
    base_url_hostname = "GUARDIAN_API_HOSTNAME"
    api_key = "GUARDIAN_API_KEY"

    print("Running tests with hostname-based URL...")
    test_api_connectivity(base_url_hostname, api_key)
    test_socket_connectivity(base_url_hostname, api_key)
    test_input_check(base_url_hostname, api_key)