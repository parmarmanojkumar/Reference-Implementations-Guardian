
# 🚀 AIShield Guardian 🛡️ x phidata Integration ⚙️  

**Agentic AI Security for Safe, Secure and, Policy-Compliant Workflows at Enterprise Scale**

Unlock secure, compliant workflows with the powerful **AIShield Guardian** x **phidata** integration. Designed to actively monitor, validate, and guard every step, this integration empowers **Agentic AI** to operate securely, safely and responsibly at enterprise scale.

Join us in securing the future of **Agentic AI** today!

## 📅 **[Schedule a Demo Here!](https://share-eu1.hsforms.com/1er3vym0FRA-r_B2ZnG5OWQffb9n?__hstc=138249519.4d817d58bf2f28287881f1a4495c2daa.1682320777326.1688113936277.1688634393681.37&__hssc=138249519.1.1688634393681&__hsfp=524412920)**

## 📜 Overview

Integrate **Guardian** ([Link](https://www.boschaishield.com/aishield-guardian/)) with **phidata** ([Link](https://www.phidata.com)) for an all-in-one, policy-compliant, safe and secure crews and workflow system!

This reference implementation demonstrates integrating the **Guardian API** with **phidata** agents to monitor, validate, and manage task workflows. Using agents for planning, and execution, it establishes a secure, policy-compliant framework enhanced with automated monitoring. The Guardian API serves as a critical guardrail, helping to enforce content standards, prevent inappropriate task progression, and secure outputs within configurable and predefined compliance boundaries.

With **Guardian** as your compliance and security guardrail, secure every agents and workflow within **CrewAI** at every step with built-in checks, ensuring only safe, approved content flows through.

## 🔑 Key Takeaways

1. **Policy Enforcement**: Guardian halts non-compliant inputs/outputs, <u>*enforcing policy at every step!*</u> **Guardian** acts as a guardrail, ensuring inputs/outputs are compliant, halting operations for non-compliant outputs even at intermediate stages, if needed.


2. **Automated Monitoring and Improved Compliance**: *From start to finish*, Guardian <u>*automates validations and reduces manual reviews*.</u> **Guardian**’s integration automates compliance validation at each step, reducing manual checks. Flags anomalies in realtime.


3. **Enhanced Security**: *Block unauthorized, sensitive content or malicious content*, <u>ensuring compliant workflows every time</u>. **Guardian** secures task workflows by detecting and blocking (if needed) any unauthorized, malicious or sensitive content. 

## ⚙️ Technical Highlights

- **`MonitoredCrew` Class**: Extends `Crew` ([Crew class documentation](https://docs.crewai.com/concepts/crews)) to integrate Guardian, adding task-by-task compliance checks via custom callbacks and workflow.
  
- **Guardian API Classes**: `GuardianAPIConfig` and `GuardianAPIClient` ensure secure API handling, retry mechanisms, and compliance validation across all project stages.

- **Modular Configurations**: Agents, tasks and crew are YAML-defined, enabling easy customization and scalable, reusable workflows. Refer this [Quickstart](https://docs.crewai.com/quickstart) from **CrewAI** for more details.

---

## Table of Contents

- [📜 Overview](#-overview)
  - [🔑 Key Takeaway](#-key-takeaways)
  - [⚙️ Technical Highlight](#️-technical-highlights)
- [🏁 Getting Started](#-getting-started)
  - [📋 Prerequisites](#-prerequisites)
  - [🛠️ Installation & Setup](#️-installation--setup)
  - [▶️  Run the Example](#️--run-the-example)
- [🔧 Technical Details](#-technical-details)
  - [🔌 GuardianAPIClient 🛡️](#-guardianapiclient-️)
  - [✔️ CheckResult](#️-checkresult)
  - [🔐 GuardianAPIConfig](#-guardianapiconfig)
  - [🕵️‍♂️ MonitoredCrew](#️️-monitoredcrew)
  - [🗂️ Agent and Task Configuration](#️-agent-and-task-configuration)
- [⚖️ License](#️-license)

---

## 🏁 Getting Started

### 📋 Prerequisites

- CrewAI (Refer this [installation](https://docs.crewai.com/installation) guide)
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

2. Configure environment variables for working with your preferred choice of LLM (Refer this [LLM guide](https://docs.crewai.com/concepts/llms) provided by CrewAI).

**📝 NOTE:** For this implementation, OpenAI API end point is used along with `gpt-4o-mini` model .

###  ▶️  Run the Example

```bash
python crewai_sample_projectplan_guardian.py
```

---
If you want to know more about its usage and implications, 

## 📅 **[Schedule a Demo Here!](https://share-eu1.hsforms.com/1er3vym0FRA-r_B2ZnG5OWQffb9n?__hstc=138249519.4d817d58bf2f28287881f1a4495c2daa.1682320777326.1688113936277.1688634393681.37&__hssc=138249519.1.1688634393681&__hsfp=524412920)**

---

## 🔧 Technical Details

The integration of **Guardian API** within **CrewAI** adds a layer of validation and monitoring to ensure each task and process adheres to specified policies. This section provides an in-depth overview of key components in this setup.

### 🔌 GuardianAPIClient 🛡️

The `GuardianAPIClient` class is responsible for interacting with the Guardian API. It centralizes request handling, enabling secure and reliable data exchange.

- **Initialization**: Configures a base URL and optional API key with authorization headers.
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

### 🕵️‍♂️ MonitoredCrew

The `MonitoredCrew` class extends CrewAI’s `Crew` class, adding monitoring with Guardian callbacks:

- **Initialization**: Accepts `agents`, `tasks`, and optional `guardian_config`.
- **Callbacks**: Validates outputs at various levels:
  - **Step Callback**: Examines each step’s output for compliance.
  - **Task Callback**: Operates at the task level to monitor final outputs.
  - **Blocking Task Callback**: Halts workflow on detecting policy violations.
- **Kickoff**: Executes all checks, verifying inputs and reviewing outputs, with real-time Guardian API validation.

### 🗂️ Agent and Task Configuration

Agents and tasks are defined in YAML files, allowing modular customization:

- **Agents** (`agents.yaml`): Represent distinct roles within the project, such as `project_planning_agent`, `estimation_agent`, and `resource_allocation_agent`.
- **Tasks** (`tasks.yaml`): Define workflow sequence, including:
  - **Task Breakdown**: Divides requirements into tasks.
  - **Time and Resource Estimation**: Determines resources for each task.
  - **Resource Allocation**: Tracks milestones using the `ProjectPlan` model.

This configuration enables scalability and adaptability by allowing task and agent customization per project.
---

If you want to know more on technical integration and how to run in your environment, 

## 📅 **[Schedule a Call Here!](https://share-eu1.hsforms.com/1er3vym0FRA-r_B2ZnG5OWQffb9n?__hstc=138249519.4d817d58bf2f28287881f1a4495c2daa.1682320777326.1688113936277.1688634393681.37&__hssc=138249519.1.1688634393681&__hsfp=524412920)**

---

## ⚖️ License

This project is licensed under MIT License.

---
---
Thank you for providing all three code files. Here’s a README tailored to your project, highlighting its functionality, structure, and technical details.

---

# 🛡️ Guardian Integration with Financial Analysis Agents

**Enable secure and policy-compliant workflows for financial data analysis.** This project integrates the Guardian API with an AI-based financial analysis agent to ensure content policy compliance on both input and output.

## 📖 Overview

This repository provides a reference implementation for integrating **Guardian API** with AI-driven financial analysis tools. With Guardian serving as a policy and compliance guardrail, financial analysis agents can perform tasks securely, ensuring outputs remain within set content boundaries.

Key features include:

- **Guardian API Integration**: Enforces content policies on input and output for secure, responsible analysis.
- **Automated Compliance Checks**: Guardian monitors each interaction for adherence to specified rules, blocking any content that violates policies.
- **Modular Agent Framework**: Each agent is modular, making it customizable and easy to extend for varied financial analysis needs.

## ⚙️ Key Components

1. **GuardianAPIClient**: Handles API communication with Guardian, including checking connectivity and managing requests.
2. **GuardianAPIConfig**: Configures Guardian for input/output validation, ensuring each prompt and response adheres to content standards.
3. **GuardedAgentWorkflow**: Manages workflow processes, running prompts through compliance checks and the financial agent model.

## 🏁 Getting Started

### 📋 Prerequisites

- Python 3.7+
- Necessary libraries, installable via:

  ```bash
  pip install -r requirements.txt
  ```

### 🛠️ Installation & Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/your-repo/guardian-financial-agent
   cd guardian-financial-agent
   ```

2. Set up the required environment variables:

   ```bash
   export GUARDIAN_API_ENDPOINT="your_guardian_api_endpoint"
   export GUARDIAN_API_KEY="your_guardian_api_key"
   ```

### ▶️ Running the Workflow

To start the agent and run example prompts through Guardian validation, execute:

```bash
python main_workflow.py
```

This will validate user prompts and model outputs, ensuring they meet policy standards before delivering results.

## 🔧 Technical Details

### GuardianAPIClient

The `GuardianAPIClient` class provides a client interface for interacting with the Guardian API. It supports endpoints for configuration, dashboard summaries, and query history, along with a chat interface that validates input/output.

### CheckResult

The `CheckResult` class represents the status of compliance checks, storing a flag for policy approval and a message.

### GuardedAgentWorkflow

The `GuardedAgentWorkflow` class orchestrates the following steps:

1. **Input Check**: Validates prompts against Guardian’s compliance policies.
2. **Agent Processing**: Runs the prompt through the financial analysis agent model.
3. **Output Check**: Verifies that model outputs meet policy guidelines.
4. **Result Display**: Shows the final validated response.

---

## 📜 Example Code

Here's an example of how a prompt is processed within the workflow:

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

## ⚖️ License

This project is licensed under the MIT License. See `LICENSE` for more details.

---

This README is designed to give users a clear understanding of the project's setup, functionality, and purpose. Let me know if there are any additional features or sections you'd like to add!
