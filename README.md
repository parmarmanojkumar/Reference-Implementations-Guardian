
# 🌐 Reference Implementations for Secure & Compliant AI Workflows with **🔐 AIShield Guardian** 

![Static Badge](https://img.shields.io/badge/State-Beta-yellow) 
![Static Badge](https://img.shields.io/badge/Notice-Work_in_Progress-blue)



Learn more about AIShield Guardian [here](https://www.boschaishield.com/aishield-guardian/)

This repository provides all integrations leveraging AIShield Guardian for secure, policy-compliant AI workflows for Agentic AI systems.

📜 To know more about 🤖  **Agentic AI system** and 🛡️**AI Agentic Security** read this [primer](LearnAgenticAISecurity/agentic_ai_security.md).

## ⚙️ Common Components

- **Guardian API** : The core [GuardianAPIClient](guardian_api.py) class enables input/output validation for compliance in workflows. In case of socket based connectivity use [GuardianAPIClient](guardian_api_soket.py). For testing connectivity leverage the utility of [GuardianConnectivityTest](utils/guardian_connectivity_test.py).
    - **📝 NOTE:** For getting your `GUARDIAN_API_ENDPOINT` and `GUARDIAN_API_KEY`, please [Contact Us.](mailto:contact.aishield@bosch.com?subject=Request%20for%20Guardian%20API%20key&body=Hello,%0D%0A%0D%0AI%20want%20to%20use%20Guardian%20API%20for%20my%20agentic%20workflow.%20Could%20you%20please%20provide%20me%20an%20API%20key.%0D%0A%0D%0AName:%0D%0AGithub%20profile%20or%20LinkedIn%20profile:%0D%0AIntended%20use:%0D%0AAgentic%20AI%20Framework:%0D%0A)

## 🤖 Agentic AI Implementations

- **CrewAI** : [GuardedCrew](AgentAI/Crewai_Agent_Example) implementation with example of project planning crew
- **Phidata** : [GuardedAgentWorkflow](AgentAI/PhiData_Agent_Examples) implementation with the financial agent workflow
- **Microsoft AutoGen** : [MonitorRoundRobinGroupChat](AgentAI/Microsoft_Autogen_Example) implementation with travel planning agents
- **OpenAI Agents SDK** : [input_guardrail/output_guardrail](AgentAI/OpenAI_Agent_SDK_Example) implementation with customer support agent for bank
- **PydenticAI** : To BE ADDED

## 🖥️↔️💻  MCP Server Implementation

- **MCP** : [MCPSeerver](MCP/mcp_server_guardian.py) implementation with example MCP server and client

## 🦜️🔗 Langchain Implementation

- **Ollama** : [GuardedOllamaChain](Langchain/Ollama_Simplechain_guardian) implementation with example of chatbot chain

## 📅 **[Schedule a call to Learn More!](https://share-eu1.hsforms.com/1er3vym0FRA-r_B2ZnG5OWQffb9n?__hstc=138249519.4d817d58bf2f28287881f1a4495c2daa.1682320777326.1688113936277.1688634393681.37&__hssc=138249519.1.1688634393681&__hsfp=524412920)**

---

## ⚖️ License

This project is licensed under MIT License.
