
# 🚀 AIShield Guardian 🛡️ x OpenAI Agents SDK Integration ⚙️  

**Agentic AI Security for Safe, Secure and, Policy-Compliant Workflows at Enterprise Scale**

Securely use **Agentic AI**  at enterprise scale without hassle. Leverage multi-agent platforms with safe, secure and compliant workflows through the integration of **AIShield Guardian** & **OpenAI Agents SDK**. 

Join us in securing the future of **Agentic AI** today!

## 📅 **[Schedule a Demo Here!](https://share-eu1.hsforms.com/1er3vym0FRA-r_B2ZnG5OWQffb9n?__hstc=138249519.4d817d58bf2f28287881f1a4495c2daa.1682320777326.1688113936277.1688634393681.37&__hssc=138249519.1.1688634393681&__hsfp=524412920)**

## 📜 Overview

Integrate **AIShield Guardian** ([Link](https://www.boschaishield.com/aishield-guardian/)) with **OpenAI Agents** ([Link](https://openai.github.io/openai-agents-python/)) for an all-in-one, policy-compliant, safe and secure crews and workflow system!

This reference implementation demonstrates how the **Guardian API** integrates with **OpenAI Agents** to monitor, validate, and secure task workflows seamlessly. Leveraging agents for planning, estimation, and resource allocation, it establishes a policy-compliant framework strengthened by automated oversight. Guardian serves as a crticial safeguard, enforcing standards, blocking unauthorized/unsafe progress, and securing outputs within defined compliance boundaries that you can set as per your need. 

With **Guardian** as your compliance and security backbone, every workflow, agent, and task in **OpenAI Agents** is secured with built-in checks, ensuring only safe and approved content flows through each stage.

## 🔑 Key Takeaways

1. **Policy Enforcement**: Guardian halts non-compliant inputs/outputs, <u>*enforcing policy at every step!*</u> **Guardian** acts as a guardrail and firewall, ensuring inputs/outputs are compliant, halting operations for non-compliant outputs even at intermediate stages, if needed.

2. **Automated Monitoring and Improved Compliance**: *From start to finish*, Guardian <u>*automates validations and reduces manual reviews*.</u> **Guardian**’s integration streamlines the validation process and flags anomalies in real-time.

3. **Enhanced Security**: *Detect and block (if needed) unauthorized, sensitive content or malicious content*, <u>ensuring compliant workflows every time</u>. **Guardian** secures task workflows at every step, every time.

## ⚙️ Technical Highlights

- **`input_guardrails/output_guardrails` Parameter**: Extends `OpenAI Agents` ([OpenAI Agents SDK - Guardrail](https://openai.github.io/openai-agents-python/guardrails/)) to integrate Guardian, adding task-by-task compliance checks.
  
- **Guardian API Classes**: `GuardianAPIConfig` and `GuardianAPIClient` ensure secure API handling, retry mechanisms, and compliance validation across all project stages.

---

Below is the updated markdown starting with the Table of Contents and all subsequent sections adjusted to reflect the OpenAI Agents SDK integration:

---

## Table of Contents

- [📜 Overview](#-overview)
  - [🔑 Key Takeaways](#-key-takeaways)
  - [⚙️ Technical Highlights](#-technical-highlights)
- [🏁 Getting Started](#-getting-started)
  - [📋 Prerequisites](#-prerequisites)
  - [🛠️ Installation & Setup](#-installation--setup)
  - [▶️ Run the Example](#-run-the-example)
- [🔧 Technical Details](#-technical-details)
  - [🔌 Guardian API Integration](#-guardian-api-integration)
    - [GuardianAPIClient 🛡️](#guardianapiclient-)
    - [✔️ CheckResult](#checkresult-)
    - [🔐 GuardianAPIConfig](#guardianapiconfig-)
  - [🤖 OpenAI Agents SDK Integration](#-openai-agents-sdk-integration)
    - [Custom Guardrail Functions](#-custom-guardrail-functions)
    - [Agent Configuration & Execution](#-agent-configuration--execution)
- [⚖️ License](#-license)

---

## 🏁 Getting Started

### 📋 Prerequisites

- **Python 3.7+** is required.
- Install the **OpenAI Agents SDK**. Refer to the [OpenAI Agents SDK Installation Guide](https://openai.github.io/openai-agents-python/) for details.
- Install required libraries:

  ```bash
  pip install -r requirements.txt
  ```

### 🛠️ Installation & Setup

1. **Clone the Repository** and set up environment variables for the Guardian API:

   ```bash
   export GUARDIAN_API_ENDPOINT="https://your-guardian-api-endpoint.com"
   export GUARDIAN_API_KEY="your_guardian_api_key"
   ```

2. **Configure Your OpenAI Environment**  
   Follow the guidelines provided by the OpenAI Agents SDK to set up your environment and select your preferred model (e.g., using the `gpt-4o-mini` model).

### ▶️ Run the Example

Run the integration script using:

```bash
python openai_agent_guardian_guardrail.py
```

This command starts the agent, processes a sample prompt, and demonstrates real-time input/output validation via the Guardian API.

---

## 🔧 Technical Details

The integration combines secure Guardian API validations with the powerful OpenAI Agents SDK to ensure each prompt and response complies with established policies.

### 🔌 Guardian API Integration

#### GuardianAPIClient 🛡️

The `GuardianAPIClient` class manages interactions with the Guardian API. It provides:

- **Secure Communication**: Configures base URLs, handles API keys, and manages authorization headers.
- **Endpoints**:
  - **Configuration**: Retrieves system settings.
  - **Dashboard Summary & Query History**: Offers insights and historical data.
  - **Chat API**: Validates prompts and responses.
  - **LLM & Mode Configuration**: Adjusts settings for various language models.
- **Connectivity**: Implements retry logic to ensure API availability.

#### ✔️ CheckResult

The `CheckResult` model captures the outcome of Guardian API validations:

- **Approved**: A boolean indicating if the content meets compliance standards.
- **Message**: A detailed message explaining the result or noting any violations.

#### 🔐 GuardianAPIConfig

`GuardianAPIConfig` acts as a wrapper around `GuardianAPIClient`, providing structured methods for:

- **Input Validation (`check_input`)**: Screens user prompts for policy compliance.
- **Output Validation (`check_output`)**: Ensures that the agent’s generated responses adhere to set guidelines.

### 🤖 OpenAI Agents SDK Integration

#### Custom Guardrail Functions

The integration defines custom guardrail functions to validate content using the Guardian API. These functions leverage Python’s asynchronous capabilities:

- **Input Guardrail** (`aishield_guardian_input_guardrail`):  
  Validates incoming prompts asynchronously and triggers a tripwire if non-compliant.

- **Output Guardrail** (`aishield_guardian_output_guardrail`):  
  Checks the agent’s responses before delivery, ensuring they comply with policies.

```python
@input_guardrail
async def aishield_guardian_input_guardrail(
    ctx: RunContextWrapper[None], agent: Agent, input: str
) -> GuardrailFunctionOutput:
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, guardian_config.check_input, input)
    return GuardrailFunctionOutput(
        output_info=GuardianCheckOutput(approved=result.approved, message=result.message),
        tripwire_triggered=not result.approved,
    )

@output_guardrail
async def aishield_guardian_output_guardrail(
    ctx: RunContextWrapper, agent: Agent, output: MessageOutput
) -> GuardrailFunctionOutput:
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, guardian_config.check_output, output.response)
    return GuardrailFunctionOutput(
        output_info=GuardianCheckOutput(approved=result.approved, message=result.message),
        tripwire_triggered=not result.approved,
    )
```

#### Agent Configuration & Execution

The OpenAI Agents SDK is used to configure and run the customer support agent with built-in safety validations:

- **Agent Setup**:  
  The agent is initialized with a name, role instructions, and the custom input/output guardrails. The `output_type` is set to a `MessageOutput` model.

- **Execution**:  
  The `Runner.run` method processes prompts asynchronously. If any validation fails, custom exceptions (`InputGuardrailTripwireTriggered` or `OutputGuardrailTripwireTriggered`) are raised.

```python
agent = Agent(
    name="Customer support agent",
    instructions="You are a customer support agent. You help customers with their questions.",
    input_guardrails=[aishield_guardian_input_guardrail],
    output_guardrails=[aishield_guardian_output_guardrail],
    output_type=MessageOutput,
)

async def main():
    test_prompt = "Hello, can you help me solve for x: 2x + 3 = 11?"
    try:
        result = await Runner.run(agent, test_prompt)
        print("Guardrail did not trip. Final output:", result.final_output.response)
    except InputGuardrailTripwireTriggered:
        print("Input guardrail tripped: Inappropriate input detected.")
    except OutputGuardrailTripwireTriggered:
        print("Output guardrail tripped: Inappropriate output detected.")

if __name__ == "__main__":
    asyncio.run(main())
```

---

## ⚖️ License

This project is licensed under the MIT License.

---

This updated documentation now reflects the OpenAI Agents SDK integration with AIShield Guardian while maintaining a clear and structured table of contents and detailed technical sections. If you need further adjustments or additional details, feel free to ask!

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
