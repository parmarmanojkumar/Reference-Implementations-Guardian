
# 🚀 AIShield Guardian 🛡️ x CrewAI Integration ⚙️  

**Agentic AI Security for Safe, Secure and, Policy-Compliant Workflows at Enterprise Scale**

Unlock secure, compliant workflows with the powerful **AIShield Guardian** x **CrewAI** integration. Designed to actively monitor, validate, and guard every step, this integration empowers **Agentic AI** to operate securely, safely and responsibly at enterprise scale.

Join us in securing the future of **Agentic AI** today!

## 📅 **[Schedule a Demo Here!](https://share-eu1.hsforms.com/1er3vym0FRA-r_B2ZnG5OWQffb9n?__hstc=138249519.4d817d58bf2f28287881f1a4495c2daa.1682320777326.1688113936277.1688634393681.37&__hssc=138249519.1.1688634393681&__hsfp=524412920)**

## 📜 Overview

Integrate **AIShield Guardian** ([Link](https://www.boschaishield.com/aishield-guardian/)) with **CrewAI** ([Link](https://www.crewai.com)) for an all-in-one, policy-compliant, safe and secure crews and workflow system!

This reference implementation demonstrates integrating the **Guardian API** with **CrewAI** crews to monitor, validate, and manage task workflows. Using agents for planning, estimating, and resource allocation, it establishes a secure, policy-compliant framework enhanced with automated monitoring. The Guardian API serves as a critical guardrail, helping to enforce content standards, prevent inappropriate task progression, and secure outputs within configurable and predefined compliance boundaries.

With **Guardian** as your compliance and security guardrail, secure every crew, flow, agents and task within **CrewAI** at every step with built-in checks, ensuring only safe, approved content flows through.

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

**📝 NOTE:** For getting your `GUARDIAN_API_ENDPOINT` and `GUARDIAN_API_KEY`, please [Contact Us.](mailto:contact.aishield@bosch.com?subject=Request%20for%20Guardian%20API%20key&body=Hello,%0D%0A%0D%0AI%20want%20to%20use%20Guardian%20API%20for%20my%20agentic%20workflow.%20Could%20you%20please%20provide%20me%20an%20API%20key.%0D%0A%0D%0AName:%0D%0AGithub%20profile%20or%20LinkedIn%20profile:%0D%0AIntended%20use:%0D%0AAgentic%20AI%20Framework:%0D%0A)

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
