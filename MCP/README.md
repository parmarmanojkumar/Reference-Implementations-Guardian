# 🚀 AIShield Guardian 🛡️ x FastMCP Guardrail Server ⚙️  

**Secure, Policy‑Compliant Workflows via MCP Guardrails**

Protect your LLM applications with real‑time input and output guardrails enforced by **AIShield Guardian** and a **MCP** server. Every prompt and response is validated against your security policies before it’s processed or delivered.

---

## 📜 Overview

This reference implementation shows how to build a **Guardrail MCP Server** using **FastMCP** that:

1. **Intercepts user inputs**, validates them via the AIShield Guardian API, and rejects unsafe prompts.
2. **Checks LLM outputs** against the same API, retrying or sanitizing if policy violations occur.
3. Provides a **sample client** to demonstrate end‑to‑end testing of the guardrail workflows.

---

## 🔑 Key Takeaways

1. **Policy Enforcement**  
   Non‑compliant inputs or outputs are blocked automatically, ensuring only safe content flows through.

2. **Automated Monitoring**  
   Built‑in logging and retries reduce manual oversight and surface anomalies in real time.

3. **Enhanced Security**  
   Prevent malicious, sensitive, or biased content from being processed or returned by your LLM.

If you want to know more on technical integration and how to run in your environment, 

## 📅 **[Schedule a Call Here!](https://share-eu1.hsforms.com/1er3vym0FRA-r_B2ZnG5OWQffb9n?__hstc=138249519.4d817d58bf2f28287881f1a4495c2daa.1682320777326.1688113936277.1688634393681.37&__hssc=138249519.1.1688634393681&__hsfp=524412920)**

---

## ⚙️ Technical Highlights

- **MCP Server Tools**  
  - `validate_input`: Guards incoming prompts.  
  - `validate_output`: Guards generated responses.

- **Guardian API Integration Classes**  
  - `GuardianAPIClient`: Low‑level HTTP wrapper with retries.  
  - `CheckResult`: Simple result model.  
  - `GuardianAPIConfig`: High‑level methods for input/output checks.

- **Sample LLM Client**  
  - Lightweight Python script simulating an LLM call and showing guardrail enforcement.

---

## Table of Contents

- [📜 Overview](#-overview)  
  - [🔑 Key Takeaways](#-key-takeaways)  
  - [⚙️ Technical Highlights](#️-technical-highlights)  
- [🏁 Getting Started](#-getting-started)  
  - [📋 Prerequisites](#-prerequisites)  
  - [🛠️ Installation & Setup](#️-installation--setup)  
  - [▶️ Run the Example](#️-run-the-example)  
- [🔧 Technical Details](#-technical-details)  
  - [🔌 Guardian API Integration](#-guardian-api-integration)  
    - [GuardianAPIClient 🛡️](#guardianapiclient-️)  
    - [✔️ CheckResult](#️-checkresult)  
    - [🔐 GuardianAPIConfig](#-guardianapiconfig)  
  - [🛡️ MCP Server Implementation](#️-mcp-server-implementation)  
    - [Input Guardrail Tool](#️-mcp-server-implementation)
    - [Output Guardrail Tool](#️-mcp-server-implementation)  
  - [🤖 Sample LLM Client Integration](#-sample-llm-client-integration)  
- [⚖️ License](#️-license)  

---

## 🏁 Getting Started

### 📋 Prerequisites

- **Python 3.7+**  
- **FastMCP** (e.g., `pip install fastmcp`)  
- **Requests** (`pip install requests`)  
- **Pydantic** (`pip install pydantic`)  
- **Tenacity** (`pip install tenacity`)  
- **Termcolor** (`pip install termcolor`)  

### 🛠️ Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/bosch-aisecurity-aishield/Reference-Implementations-Guardian.git
   cd mcp
   ```



2. **Configure environment variables**  
   ```bash
   export GUARDIAN_API_ENDPOINT="https://your_guardian_api_endpoint"
   export GUARDIAN_API_KEY="your_guardian_api_key"
   ```
**📝 NOTE:** For getting your `GUARDIAN_API_ENDPOINT` and `GUARDIAN_API_KEY`, please [Contact Us.](mailto:contact.aishield@bosch.com?subject=Request%20for%20Guardian%20API%20key&body=Hello,%0D%0A%0D%0AI%20want%20to%20use%20Guardian%20API%20for%20my%20agentic%20workflow.%20Could%20you%20please%20provide%20me%20an%20API%20key.%0D%0A%0D%0AName:%0D%0AGithub%20profile%20or%20LinkedIn%20profile:%0D%0AIntended%20use:%0D%0AAgentic%20AI%20Framework:%0D%0A)
---

### ▶️ Run the Example

1. **Start the Guardrail MCP server**  
   ```bash
   python mcp_server_guardian.py
   ```

2. **Run the sample LLM test client**  
   ```bash
   python mcp_client_test.py
   ```

Interactively enter safe or unsafe prompts to see input/output validations in action.

---

## 🔧 Technical Details

### 🔌 Guardian API Integration

#### GuardianAPIClient 🛡️

Manages HTTP communication with AIShield Guardian:

- Sets base URL and headers (includes API key).  
- Provides `_get`/`_post` with retries via **Tenacity**.  
- Implements `chat_app1(prompt)` to send text for policy checks.

#### ✔️ CheckResult

Captures validation outcomes:

- **approved** (`bool`): Pass/fail.  
- **message** (`str`): Details on any policy violation.

#### 🔐 GuardianAPIConfig

High‑level wrapper that:

- Initializes the client and verifies connectivity.  
- Implements:
  ```python
  def check_input(self, prompt: str) -> CheckResult
  def check_output(self, output: str) -> CheckResult
  ```
- Performs basic sanity checks before API calls.

---

### 🛡️ MCP Server Implementation

```python
from fastmcp import McpServer, ToolResponse
from pydantic import BaseModel
from guardian_api import GuardianAPIConfig

# Load endpoint and key from environment
import os
endpoint = os.getenv("GUARDIAN_API_ENDPOINT")
key      = os.getenv("GUARDIAN_API_KEY")

guardian = GuardianAPIConfig(api_key=key, base_url=endpoint)
server   = McpServer(name="GuardrailServer", version="1.0.0")

class InputSchema(BaseModel):
    input_text: str

class OutputSchema(BaseModel):
    output_text: str

@server.tool(name="validate_input", description="Validate user input.", schema=InputSchema)
def validate_input(input_text: str) -> ToolResponse:
    result = guardian.check_input(input_text)
    if not result.approved:
        return ToolResponse(
            content=[{"type":"text","text":f"Input rejected: {result.message}"}],
            success=False,
        )
    return ToolResponse(
        content=[{"type":"text","text":"Input is valid."}],
        success=True,
    )

@server.tool(name="validate_output", description="Validate LLM output.", schema=OutputSchema)
def validate_output(output_text: str) -> ToolResponse:
    result = guardian.check_output(output_text)
    if not result.approved:
        return ToolResponse(
            content=[{"type":"text","text":f"Output rejected: {result.message}"}],
            success=False,
        )
    return ToolResponse(
        content=[{"type":"text","text":"Output is valid."}],
        success=True,
    )

if __name__ == "__main__":
    server.run()
```

---

### 🤖 Sample LLM Client Integration

```python
import requests

MCP_URL = "http://localhost:8000"

def test_input_validation(txt):
    return requests.post(f"{MCP_URL}/validate_input", json={"input_text": txt}).json()

def test_output_validation(txt):
    return requests.post(f"{MCP_URL}/validate_output", json={"output_text": txt}).json()

def dummy_llm(prompt):
    return f"LLM response based on: {prompt}"

def run_test():
    user_prompt = input("Enter prompt: ")
    resp_in = test_input_validation(user_prompt)
    if not resp_in.get("success"):
        print("Rejected:", resp_in["content"][0]["text"])
        return

    llm_out = dummy_llm(user_prompt)
    resp_out = test_output_validation(llm_out)
    if not resp_out.get("success"):
        print("Rejected:", resp_out["content"][0]["text"])
    else:
        print("Final Output:", llm_out)

if __name__ == "__main__":
    run_test()
```
If you want to know more on technical integration and how to run in your environment, 

## 📅 **[Schedule a Call Here!](https://share-eu1.hsforms.com/1er3vym0FRA-r_B2ZnG5OWQffb9n?__hstc=138249519.4d817d58bf2f28287881f1a4495c2daa.1682320777326.1688113936277.1688634393681.37&__hssc=138249519.1.1688634393681&__hsfp=524412920)**

---

## ⚖️ License

This project is licensed under the **MIT License**. Feel free to adapt and extend as needed!