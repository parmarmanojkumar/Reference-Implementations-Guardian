
# 🚀 AIShield Guardian 🛡️ x Phidata Integration ⚙️  

**Agentic AI Security for Safe, Secure and, Policy-Compliant Workflows at Enterprise Scale**

Unlock secure, compliant workflows with the powerful **AIShield Guardian** x **Phidata** integration. Designed to actively monitor, validate, and guard every step, this integration empowers **Agentic AI** to operate securely, safely and responsibly at enterprise scale.

Join us in securing the future of **Agentic AI** today!

🔐 See Agentic Security in Action in this youtube [video.](https://youtu.be/d9ZLyrNgiLU?si=bGm8C_0e9k0krHq7)

[![Watch the video](https://img.youtube.com/vi/d9ZLyrNgiLU/0.jpg)](https://youtu.be/d9ZLyrNgiLU?si=bGm8C_0e9k0krHq7)

## 📅 **[Schedule a Demo Here!](https://share-eu1.hsforms.com/1er3vym0FRA-r_B2ZnG5OWQffb9n?__hstc=138249519.4d817d58bf2f28287881f1a4495c2daa.1682320777326.1688113936277.1688634393681.37&__hssc=138249519.1.1688634393681&__hsfp=524412920)**

## 📜 Overview

Integrate **Guardian** ([Link](https://www.boschaishield.com/aishield-guardian/)) with **Phidata** ([Link](https://www.phidata.com)) for an all-in-one, policy-compliant, safe and secure agents and workflow system!

This reference implementation demonstrates integrating the **Guardian API** with **Phidata** agents to monitor, validate, and manage agents and related workflows. Using agents for planning, and execution, it establishes a secure, policy-compliant framework enhanced with automated monitoring. The Guardian API serves as a critical guardrail, helping to enforce content standards, prevent inappropriate agent/workflow progression, and secure outputs within configurable and predefined compliance boundaries.

With **Guardian** as your compliance and security guardrail, secure every agents and workflow within **Phidata** at every step with built-in checks, ensuring only safe, approved content flows through.

## 🔑 Key Takeaways

1. **Policy Enforcement**: Guardian monitors and halts non-compliant inputs/outputs, <u>*enforcing policy at every step!*</u> **Guardian** acts as a guardrail, ensuring inputs/outputs are compliant, halting operations for non-compliant outputs even at intermediate stages, if needed.

2. **Automated Monitoring and Improved Compliance**: *From start to finish*, Guardian <u>*automates validations and reduces manual reviews*.</u> **Guardian**’s integration automates compliance validation at each step, reducing manual checks. Flags anomalies in realtime.

3. **Enhanced Security**: *Block unauthorized, sensitive content or malicious content*, <u>ensuring compliant workflows every time</u>. **Guardian** secures agent workflows by detecting and blocking (if needed) any unauthorized, malicious or sensitive content.

## ⚙️ Technical Highlights

- **`GuardedAgentWorkflow` Class**: Created a new agentic workflow class to integrate Guardian with agent. Manages workflow processes, running prompts through compliance checks and the agent model at every step.
  
- **Guardian API Classes**: `GuardianAPIConfig` and `GuardianAPIClient` ensure secure API handling, retry mechanisms, and compliance validation across all project stages.

- **Modular Configurations**: Any Agents can be added to the `GuardedAgentWorkflow` in modular fashion, enabling easy customization and scalable, reusable workflows.

---

## Table of Contents

- [📜 Overview](#-overview)
  - [🔑 Key Takeaway](#-key-takeaways)
  - [⚙️ Technical Highlight](#️-technical-highlights)
- [🏁 Getting Started](#-getting-started)
  - [📋 Prerequisites](#-prerequisites)
  - [🛠️ Installation & Setup](#️-installation--setup)
  - [▶️  Run the Example](#️--run-the-example)
    - [💻 Example Code](#-example-code)
- [🔧 Technical Details](#-technical-details)
  - [🔌 GuardianAPIClient 🛡️](#-guardianapiclient-️)
  - [✔️ CheckResult](#️-checkresult)
  - [🔐 GuardianAPIConfig](#-guardianapiconfig)
  - [🛡️ GuardedAgentWorkflow](#️-guardedagentworkflow)
  - [🗂️ Agent and Workflow Configuration](#️-agent-and-workflow-configuration)
- [⚖️ License](#️-license)

---

## 🏁 Getting Started

### 📋 Prerequisites

- Phidata (Refer this [guide](https://docs.phidata.com/agents))
- Required libraries:

  ```bash
  pip install -r requirement.txt
  ```

### 🛠️ Installation & Setup

1. Clone the repo and configure environment variables for working with **Guardian**:

   ```bash
   export GUARDIAN_API_ENDPOINT="https://your-guardian-api-endpoint.com"
   export GUARDIAN_API_KEY="your_guardian_api_key"
   ```

- **📝 NOTE:** For getting your `GUARDIAN_API_ENDPOINT` and `GUARDIAN_API_KEY`, please [Contact Us.](mailto:contact.aishield@bosch.com?subject=Request%20for%20Guardian%20API%20key&body=Hello,%0D%0A%0D%0AI%20want%20to%20use%20Guardian%20API%20for%20my%20agentic%20workflow.%20Could%20you%20please%20provide%20me%20an%20API%20key.%0D%0A%0D%0AName:%0D%0AGithub%20profile%20or%20LinkedIn%20profile:%0D%0AIntended%20use:%0D%0AAgentic%20AI%20Framework:%0D%0A)

2. Configure environment variables for working with your preferred choice of LLM (Refer this [Model guide](https://docs.phidata.com/models/introduction) provided by Phidata).

- **📝 NOTE:** For this implementation, Ollama ([configuration](https://docs.phidata.com/models/ollama)) is used along with `llama3.2:1b` model ([Model card from Ollama](https://ollama.com/library/llama3.2:1b); [Model card from huggingface](https://huggingface.co/meta-llama/Llama-3.2-1B)).

###  ▶️  Run the Example
To start the financial agent (Phidata reference agent [implementation](https://github.com/phidatahq/phidata/blob/924a61169a46b57204a932896249165c99d8eecc/cookbook/assistants/finance.py#L4) without guardrail) and run example prompts through Guardian validation, execute:

```bash
python finance_agent_guardian_api.py
```

This will validate user prompts and model outputs, ensuring they meet policy standards before delivering results.

### 💻 Example Code

Here's an example of how a prompt is processed with `GuardedAgentWorkflow`:

```python
from guardian_workflow import GuardedAgentWorkflow
from guardian_api import GuardianAPIConfig
from phi.agent import Agent

# Define Guardian configuration and agent setup
guardian_config = GuardianAPIConfig(api_key="your_api_key", base_url="https://your-guardian-api-endpoint.com")
workflow = GuardedAgentWorkflow(agent=financial_agent, guardian_config=guardian_config, prompts=["Your prompt"], guardrail_config={"active": True})

# Run the workflow
workflow.run()
```

### 🔐 See Agentic Security in Action

Click to watch youtube [video.](https://youtu.be/d9ZLyrNgiLU?si=bGm8C_0e9k0krHq7)

[![Watch the video](https://img.youtube.com/vi/d9ZLyrNgiLU/0.jpg)](https://youtu.be/d9ZLyrNgiLU?si=bGm8C_0e9k0krHq7)

---
If you want to know more about its usage and implications,

## 📅 **[Schedule a Demo Here!](https://share-eu1.hsforms.com/1er3vym0FRA-r_B2ZnG5OWQffb9n?__hstc=138249519.4d817d58bf2f28287881f1a4495c2daa.1682320777326.1688113936277.1688634393681.37&__hssc=138249519.1.1688634393681&__hsfp=524412920)**

---

## 🔧 Technical Details

The integration of **Guardian API** within **Phidata** adds a layer of validation and monitoring to ensure each agent and workflow adheres to specified policies. This section provides an in-depth overview of key components in this setup.

### 🔌 GuardianAPIClient 🛡️

The `GuardianAPIClient` class is responsible for interacting with the Guardian API. It centralizes request handling, enabling secure and reliable data exchange.

- **Initialization**: Configures a base URL and optional API key with authorization headers.
  - **📝 NOTE:** For getting your `GUARDIAN_API_ENDPOINT` and `GUARDIAN_API_KEY`, please [Contact Us.](mailto:contact.aishield@bosch.com?subject=Request%20for%20Guardian%20API%20key&body=Hello,%0D%0A%0D%0AI%20want%20to%20use%20Guardian%20API%20for%20my%20agentic%20workflow.%20Could%20you%20please%20provide%20me%20an%20API%20key.%0D%0A%0D%0AName:%0D%0AGithub%20profile%20or%20LinkedIn%20profile:%0D%0AIntended%20use:%0D%0AAgentic%20AI%20Framework:%0D%0A)
- **GET and POST Methods**: Simplify API communication, including error handling for logging issues.
- **Endpoints**:
  - **Configuration**: Retrieves configuration details.
  - **Dashboard Summary**: Provides an overview of system usage.
  - **Query History**: Accesses historical API queries.
  - **Chat API**: Validates prompts for policy compliance.
  - **LLM Configuration and Mode Configuration**: Adjust settings for large language models (e.g., Llama) and operational modes.
- **Connectivity Check**: Uses retry to ensure Guardian API availability at runtime.

### ✔️ CheckResult

`CheckResult` represents the result of data validation checks performed by Guardian API with:

- **Approved**: Boolean flag indicating compliance.
- **Message**: Provides details on compliance or policy violations.

### 🔐 GuardianAPIConfig

`GuardianAPIConfig` wraps `GuardianAPIClient` for structured input and output validation.

- **Input Validation** (`check_input`): Screens prompts for policy compliance.
- **Output Validation** (`check_output`): Ensures generated content adheres to policies, flagging violations.

### 🛡️ GuardedAgentWorkflow

The `GuardedAgentWorkflow` class integrates an AI agent with the Guardian API, enforcing compliance checks on inputs and outputs through configurable guardrails.

- **Initialization**: Takes `agent`, `guardian_config`, `prompts`, and `guardrail_config`.
- **Prompt Processing**: Validates the prompt to ensure it’s usable.
- **Guardian Input Check**: Checks input compliance using Guardian if enabled.
- **Agent Execution**: Sends the prompt to the agent and retrieves the response.
- **Guardian Output Check**: Validates the agent’s output for compliance.
- **Result Display**: Shows the agent’s validated response in a readable format.
- **Workflow Execution**: Runs the complete process for each prompt, ensuring policy compliance at each step.

### 🗂️ Agent and Workflow Configuration

The Phidata Agent Framework is designed for building and managing agentic systems. It supports:

- **Agent Creation**: Enables agents with memory, knowledge, tools, and reasoning capabilities.
- **Agent Teams**: Allows collaboration between agents for complex tasks.
- **Extensibility**: Integrates with various tools, knowledge bases, and vector databases.

The `GuardedAgentWorkflow` class can integrate with this framework, applying compliance checks seamlessly across various agents within Phidata's modular system. More details can be found [here](https://docs.phidata.com/agents).

This configuration enables scalability and adaptability by allowing agent customization per project.

---

If you want to know more on technical integration and how to run in your environment,

## 📅 **[Schedule a Call Here!](https://share-eu1.hsforms.com/1er3vym0FRA-r_B2ZnG5OWQffb9n?__hstc=138249519.4d817d58bf2f28287881f1a4495c2daa.1682320777326.1688113936277.1688634393681.37&__hssc=138249519.1.1688634393681&__hsfp=524412920)**

---

## ⚖️ License

This project is licensed under MIT License.
