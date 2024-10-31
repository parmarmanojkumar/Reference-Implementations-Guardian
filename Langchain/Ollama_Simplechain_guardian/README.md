
# 🚀 AIShield Guardian 🛡️ x LangChain Integration ⚙️

**Generative AI Security for Safe and Policy-Compliant Workflows in LangChain**

Unlock secure, compliant workflows with the powerful **AIShield Guardian** x **Langchain** integration. Designed to actively monitor, validate, and guard every step, this integration empowers **AI Applications** and **Agentic AI** to operate securely, safely and responsibly at enterprise scale.

Join us in securing the future of **Gen AI** today!

🔐 See secure Langchain with Ollama in Action in this youtube [video.](https://youtu.be/A0Dk3tQEvfg)

[![Watch the video](https://img.youtube.com/vi/A0Dk3tQEvfg/0.jpg)](https://youtu.be/A0Dk3tQEvfg)

## 📅 **[Schedule a Demo Here!](https://share-eu1.hsforms.com/1er3vym0FRA-r_B2ZnG5OWQffb9n?__hstc=138249519.4d817d58bf2f28287881f1a4495c2daa.1682320777326.1688113936277.1688634393681.37&__hssc=138249519.1.1688634393681&__hsfp=524412920)**

## 📜 Overview

Integrate **Guardian** ([Link](https://www.boschaishield.com/aishield-guardian/)) with **Langchain** ([Link](https://www.langchain.com)) for an all-in-one, policy-compliant, safe and secure ai applications, agents and workflow system!

This reference implementation demonstrates integrating the **Guardian API** with **Langchain** to monitor, validate, and manage ai applications, agents and related workflows. Using chat example with **Ollama** [Link](https://ollama.com), it establishes a secure, policy-compliant framework enhanced with automated monitoring. The Guardian API serves as a critical guardrail, helping to enforce content standards, prevent inappropriate agent/workflow progression, and secure outputs within configurable and predefined compliance boundaries.

With **Guardian** as your compliance and security guardrail, secure every ai application, agents and workflow within **Langchain** at every step with built-in checks, ensuring only safe, approved content flows through.

## 🔑 Key Features

1. **Policy Enforcement**: Guardian monitors and halts non-compliant inputs/outputs, <u>*enforcing policy at every step!*</u> **Guardian** acts as a guardrail, ensuring inputs/outputs are compliant, halting operations for non-compliant outputs even at intermediate stages, if needed.

2. **Automated Monitoring and Improved Compliance**: *From start to finish*, Guardian <u>*automates validations and reduces manual reviews*.</u> **Guardian**’s integration automates compliance validation at each step, reducing manual checks. Flags anomalies in realtime.

3. **Enhanced Security**: *Block unauthorized, sensitive content or malicious content*, <u>ensuring compliant workflows every time</u>. **Guardian** secures ai applications, agents and workflows by detecting and blocking (if needed) any unauthorized, malicious or sensitive content.

4. **Integration Flexibility**: *Designed for use with* <u>any **LangChain**-compatible components</u>; the example here uses Ollama.

## ⚙️ Technical Highlights

- **`GuardedOllamaChain` Class**: Extends `Chain` ([Chain class documentation](https://python.langchain.com/v0.1/docs/modules/chains/))to integrate Guardian, adding step-by-step compliance checks during execution of chain. Refer this [Quickstart](https://python.langchain.com/docs/integrations/llms/ollama/) to understand the **Ollama** working with **Langchain**.

- **Guardian API Classes**: `GuardianAPIConfig` and `GuardianAPIClient` ensure secure API handling, retry mechanisms, and compliance validation across all project stages.

- **Modular Configurations with Flexible Compliance Integration**: Any Langchain component can be integrated with  `GuardianAPIConfig` in modular fashion, enabling easy customization and scalable, reusable with Langchain Expression Language [LCEL](https://python.langchain.com/docs/concepts/lcel/).

---

## Table of Contents

- [📜 Overview](#-overview)
  - [🔑 Key Features](#-key-features)
  - [⚙️ Technical Highlights](#️-technical-highlights)
- [🏁 Getting Started](#-getting-started)
  - [📋 Prerequisites](#-prerequisites)
  - [🛠️ Installation & Setup](#️-installation--setup)
  - [▶️ Run the Example](#️-run-the-example)
- [🔧 Technical Details](#-technical-details)
  - [🔌 GuardianAPIClient 🛡️](#-guardianapiclient-️)
  - [✔️ CheckResult](#️-checkresult)
  - [🔐 GuardianAPIConfig](#-guardianapiconfig)
  - [🧩 GuardedOllamaChain](#-guardedollamachain)
- [⚖️ License](#️-license)

---

## 🏁 Getting Started

### 📋 Prerequisites

- Python
- Ollama: Refer this [Ollama Guide](https://github.com/ollama/ollama)
- Langchain: Refer this [Installation Guide](https://python.langchain.com/docs/how_to/installation/)
- Langchain + Ollama: Refer this [quick Start](https://python.langchain.com/docs/integrations/llms/ollama/)
- Required packages:

  ```bash
  pip install -r requirements.txt
  ```

### 🛠️ Installation & Setup

1. Clone the repo and configure environment variables for working with **Guardian**:

   ```bash
   export GUARDIAN_API_ENDPOINT="https://your-guardian-api-endpoint.com"
   export GUARDIAN_API_KEY="your_guardian_api_key"
   ```

- **📝 NOTE:** For getting your `GUARDIAN_API_ENDPOINT` and `GUARDIAN_API_KEY`, please [Contact Us.](mailto:contact.aishield@bosch.com?subject=Request%20for%20Guardian%20API%20key&body=Hello,%0D%0A%0D%0AI%20want%20to%20use%20Guardian%20API%20for%20my%20agentic%20workflow.%20Could%20you%20please%20provide%20me%20an%20API%20key.%0D%0A%0D%0AName:%0D%0AGithub%20profile%20or%20LinkedIn%20profile:%0D%0AIntended%20use:%0D%0AAgentic%20AI%20Framework:%0D%0A)

2. Configure environment variables for working with your preferred choice of LLM (Refer this [Model guide](https://python.langchain.com/docs/integrations/llms/) provided by Langchain).

- **📝 NOTE:** For this implementation, Ollama ([configuration](https://python.langchain.com/docs/integrations/llms/ollama/)) is used along with `llama3.2:1b` model ([Model card from Ollama](https://ollama.com/library/llama3.2:1b); [Model card from huggingface](https://huggingface.co/meta-llama/Llama-3.2-1B)).

### ▶️ Run the Example

To test the integration, execute:

```bash
python Guardian_ollama_langchain_demo.py
```

This runs the chain on example prompts, validating each step with Guardian.

---

## 🔧 Technical Details

The integration of **Guardian API** within **Langchain** adds a layer of validation and monitoring to ensure each ai application, agent and workflow adheres to specified policies. This section provides an in-depth overview of key components in this setup.

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

### 🧩 GuardedOllamaChain

The `GuardedOllamaChain` class customizes **LangChain** `Chain` by adding compliance monitoring with Guardian API to run with **Ollama**:

- **Initialization**: Takes an `ollama_model` and a `guardian_config` for validation setup.
- **Compliance Checks**: Enforces policy checks at multiple points:
  - **Input Validation**: Checks user prompts for compliance before passing to the model.
  - **Output Validation**: Examines model responses to ensure policy adherence.
  - **Error Handling**: Manages issues during model generation and API calls, providing secure, controlled interactions.
- **Execution**: Runs each prompt through compliance and generation steps, ensuring safe, policy-aligned outputs.

### 🗂️ AI Applications, Agents and Workflow Configuration

The **Langchain Framework** is designed for building and managing ai applications, agents and workflow systems. It supports:

- **Language Model Chains**: Allows for sequential task execution, linking various models and tools for complex, dynamic workflows.
- **Tool Integration**: Easily connects to external tools (e.g., APIs, databases) to extend AI capabilities.
- **Modularity**: Enables flexible, customizable chains for diverse applications, optimizing workflows for various use cases.

The `GuardedOllamaChain` class can integrate with this framework, applying compliance checks seamlessly across various Langchain components within Langchain's modular system. More details are available [here](https://python.langchain.com/docs/integrations/components/).

This configuration enables scalability and adaptability by allowing  chain customization per project.

---

## ⚖️ License

This project is licensed under the MIT License.
