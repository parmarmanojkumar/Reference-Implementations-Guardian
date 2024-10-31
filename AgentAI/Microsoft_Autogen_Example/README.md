
# 🚀 AIShield Guardian 🛡️ x Microsoft AutoGen Integration ⚙️  

**Agentic AI Security for Safe, Secure and, Policy-Compliant Workflows at Enterprise Scale**

Securely use **Agentic AI**  at enterprise scale without hassle. Leverage multi-agent platforms with safe, secure and compliant workflows through the integration of **AIShield Guardian** & **Microsoft AutoGen**.

Join us in securing the future of **Agentic AI** today!

## 📅 **[Schedule a Demo Here!](https://share-eu1.hsforms.com/1er3vym0FRA-r_B2ZnG5OWQffb9n?__hstc=138249519.4d817d58bf2f28287881f1a4495c2daa.1682320777326.1688113936277.1688634393681.37&__hssc=138249519.1.1688634393681&__hsfp=524412920)**

## 📜 Overview

Integrate **AIShield Guardian** ([Link](https://www.boschaishield.com/aishield-guardian/)) with **Microsoft AutoGen** ([Link](https://microsoft.github.io/autogen/0.2/)) for an all-in-one, policy-compliant, safe and secure crews and workflow system!

This reference implementation demonstrates how the **Guardian API** integrates with **Microsoft AutoGen** to monitor, validate, and secure agent workflows seamlessly. Leveraging agents for planning, estimation, and resource allocation, it establishes a policy-compliant framework strengthened by automated oversight. Guardian serves as a crticial safeguard, enforcing standards, blocking unauthorized/unsafe progress, and securing outputs within defined compliance boundaries that you can set as per your need.

With **Guardian** as your compliance and security backbone, every workflow, agent, and task in **Microsoft AutoGen** is secured with built-in checks, ensuring only safe and approved content flows through each stage.

## 🔑 Key Takeaways

1. **Policy Enforcement**: Guardian halts non-compliant inputs/outputs, <u>*enforcing policy at every step!*</u> **Guardian** acts as a guardrail and firewall, ensuring inputs/outputs are compliant, halting operations for non-compliant outputs even at intermediate stages, if needed.

2. **Automated Monitoring and Improved Compliance**: *From start to finish*, Guardian <u>*automates validations and reduces manual reviews*.</u> **Guardian**’s integration streamlines the validation process and flags anomalies in real-time.

3. **Enhanced Security**: *Detect and block (if needed) unauthorized, sensitive content or malicious content*, <u>ensuring compliant agentic workflows every time</u>. **Guardian** secures agentic workflows at every step, every time.

## ⚙️ Technical Highlights

- **`MonitorRoundRobinGroupChat` Class**: Extends `RoundRobinGroupChat` ([RoundRobinGroupChat class documentation](https://microsoft.github.io/autogen/dev/reference/python/autogen_agentchat/autogen_agentchat.teams.html#autogen_agentchat.teams.RoundRobinGroupChat)) to integrate Guardian, adding task-by-task compliance checks via custom workflow.
  
- **Guardian API Classes**: `GuardianAPIConfig` and `GuardianAPIClient` ensure secure API handling, retry mechanisms, and compliance validation across all project stages.

- **Modular Configurations**: Agents, and teams are easily-defined, enabling easy customization and scalable, reusable workflows. Refer this [Quickstart](https://microsoft.github.io/autogen/dev/user-guide/agentchat-user-guide/quickstart.html#) from **Microsoft AutoGen** for more details.

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
  - [🛡️ MonitorRoundRobinGroupChat](#️-monitorroundrobingroupchat)
  - [🗂️ Agent and Workflow Configuration](#️-agent-and-workflow-configuration)
- [⚖️ License](#️-license)

---

## 🏁 Getting Started

### 📋 Prerequisites

- Microsoft AutoGen (Refer this [installation](https://microsoft.github.io/autogen/dev/user-guide/agentchat-user-guide/installation.html) guide)
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

**📝 NOTE:** For getting your `GUARDIAN_API_ENDPOINT` and `GUARDIAN_API_KEY`, please [Contact Us.](mailto:contact.aishield@bosch.com?subject=Request%20for%20Guardian%20API%20key&body=Hello,%0D%0A%0D%0AI%20want%20to%20use%20Guardian%20API%20for%20my%20agentic%20workflow.%20Could%20you%20please%20provide%20me%20an%20API%20key.%0D%0A%0D%0AName:%0D%0AGithub%20profile%20or%20LinkedIn%20profile:%0D%0AIntended%20use:%0D%0AAgentic%20AI%20Framework:%0D%0A)

2. Configure environment variables for working with your preferred choice of LLM (Refer this [LLM guide](https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/framework/model-clients.html) provided by Microsoft AutoGen).

**📝 NOTE:** For this implementation, OpenAI API end point is used along with `gpt-4o-mini` model .

###  ▶️  Run the Example

```bash
python travel_panning_guardian.py
```

---
If you want to know more about its usage and implications,

## 📅 **[Schedule a Demo Here!](https://share-eu1.hsforms.com/1er3vym0FRA-r_B2ZnG5OWQffb9n?__hstc=138249519.4d817d58bf2f28287881f1a4495c2daa.1682320777326.1688113936277.1688634393681.37&__hssc=138249519.1.1688634393681&__hsfp=524412920)**

---

## 🔧 Technical Details

The integration of **Guardian API** within **Microsoft AutoGen** adds a layer of validation and monitoring to ensure each task and process adheres to specified policies. This section provides an in-depth overview of key components in this setup.

### 🔌 GuardianAPIClient 🛡️

The `GuardianAPIClient` class is responsible for interacting with the Guardian API. It centralizes request handling, enabling secure and reliable data exchange.

**📝 NOTE:** For getting your `GUARDIAN_API_ENDPOINT` and `GUARDIAN_API_KEY`, please [Contact Us.](mailto:contact.aishield@bosch.com?subject=Request%20for%20Guardian%20API%20key&body=Hello,%0D%0A%0D%0AI%20want%20to%20use%20Guardian%20API%20for%20my%20agentic%20workflow.%20Could%20you%20please%20provide%20me%20an%20API%20key.%0D%0A%0D%0AName:%0D%0AGithub%20profile%20or%20LinkedIn%20profile:%0D%0AIntended%20use:%0D%0AAgentic%20AI%20Framework:%0D%0A)

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

### 🛡️ MonitorRoundRobinGroupChat

The `MonitorRoundRobinGroupChat` class wraps around the `RoundRobinGroupChat` to add real-time monitoring and validation through **Guardian**, ensuring compliance and security throughout the chat workflow:

- **Initialization**: Takes the following parameters:
  - `group_chat`: An instance of `RoundRobinGroupChat` representing the group chat to monitor.
  - `guardian_api_config`: Configuration for interacting with the **Guardian API** for validation.
  - `stop_on_violation`: A boolean flag indicating whether to halt the workflow if a policy violation is detected.
  - `input_checked`: A boolean flag to enable or disable input validation before starting the group chat.
  - `verbose`: Enables detailed output for intermediate states and validations.

- **Input Validation**:
  - Validates the initial input task using Guardian to ensure it complies with the set policies.
  - If the input is non-compliant and `stop_on_violation` is `True`, the execution is halted immediately.

- **Output Validation**:
  - After running the group chat, each agent's output is validated in real-time.
  - Non-compliant outputs are logged, and if `stop_on_violation` is `True`, the workflow stops immediately upon detecting a violation.

- **Message Handling**:
  - Collects and processes each message from the group chat, skipping initial input if it was pre-validated.
  - Validates messages sequentially, ensuring that only compliant messages are included in the final output.

- **RunMonitor Method**:
  - Initiates the monitoring process by first validating the input (if enabled).
  - Executes the group chat task with continuous output validation.
  - Returns the result along with a list of validated messages for review.

This setup provides a robust mechanism to enforce policy compliance dynamically across multi-agent conversations, making it ideal for secure enterprise applications.

### 🗂️ Agent and Workflow Configuration

The **Microsoft AutoGen** Agent Framework is designed for building and managing agentic systems. It supports:

- **Agent Creation**: Enables agents with memory, knowledge, tools, and reasoning capabilities.
- **Agent Teams**: Allows collaboration between agents for complex tasks.
- **Extensibility**: Integrates with various tools, knowledge bases, and vector databases.

The `MonitorRoundRobinGroupChat` class can integrate with this framework, applying compliance checks seamlessly across various agents within Microsoft AutoGen modular system. More details can be found [here](https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/index.html).

This configuration enables scalability and adaptability by allowing agent customization per project.

---

If you want to know more on technical integration and how to run in your environment,

## 📅 **[Schedule a Call Here!](https://share-eu1.hsforms.com/1er3vym0FRA-r_B2ZnG5OWQffb9n?__hstc=138249519.4d817d58bf2f28287881f1a4495c2daa.1682320777326.1688113936277.1688634393681.37&__hssc=138249519.1.1688634393681&__hsfp=524412920)**

---

## ⚖️ License

This project is licensed under MIT License.
