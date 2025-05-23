# Netmiko mcp

A powerful, AI-assisted solution for automating Cisco network device configuration and management using Model Context Protocol (MCP).

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📋 Overview

This application provides a sophisticated interface for interacting with Cisco network devices through an AI-powered automation layer. It leverages Claude AI's capabilities via the Model Context Protocol (MCP) to enable network engineers to manage Cisco devices with natural language processing.

## ✨ Key Features

- **Show Command Execution**: Execute show commands on Cisco devices with simplified syntax
- **Configuration Management**: Apply configuration changes to network devices safely
- **Ping Testing**: Perform network connectivity tests using Cisco ping commands
- **Natural Language Processing**: Interpret network commands through conversational language
- **Claude Integration**: Works as an MCP extension for Claude Desktop

## 🔧 System Requirements

- Python 3.10 or higher
- Cisco network device(s) accessible via SSH or you can use CML Cisco sandbox
- Windows/Linux/macOS compatible

## 🚀 Quick Start

### Environment Setup with UV

This project leverages UV for efficient Python environment and package management:

```bash
# Install UV
pip install uv

# Create and activate virtual environment
cd MCP_Network_automator
uv venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/macOS

# Install dependencies
uv sync
```

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd MCP_Network_automator
   ```

2. Install project and dependencies:
   ```bash
   uv venv
   .venv\Scripts\activate
   uv pip install -e .
   ```

### Claude Desktop Integration

1. Install the MCP server to your Claude Desktop:
   ```bash
   mcp install mcp_cisco_server.py
   ```

2. Inspect your mcp server:
   ```bash
   mcp dev mcp_cisco_server.py
   ```
   ![MCP Inspection](image/image.png)

   You can test if this tool works correctly or not.

3. Configure Claude Desktop by adding this to your `claude_desktop_config.json`:
   ```json
   {
     "mcpServers": {
       "Cisco-IOS-config": {
         "command": "uv",
         "args": [
           "run",
           "--with",
           "mcp[cli], netmiko",
           "mcp",
           "run",
           "C:\\Users\\<your-username>\\Documents\\MCP_Network_automator\\mcp_cisco_server.py" #Choose correct your path
         ]
       }
     }
   }
   ```
   Default location: `C:\Users\<your-username>\AppData\Roaming\Claude\claude_desktop_config.json`

## 🧰 Core Components

- **mcp_cisco_server.py**: Main MCP server implementation for Cisco network automation tools
- **agent_client/cisco_agent.py**: Core connector for Cisco device interaction, handling SSH connections and command execution

## 🔧 Available Tools

The MCP Network Automator provides three main tools:

1. **show_cisco_command**: Execute show commands on Cisco devices
   - Examples: "show running-config", "show interfaces", "show ip route"

2. **config_cisco_command**: Apply configuration changes to Cisco devices
   - Automatically enters configuration mode
   - Handles multi-line configuration commands

3. **ping_cisco_device**: Test network connectivity from Cisco devices
   - Executes ping commands to verify network reachability

## 💬 Example Usage

For this example, we use Cisco Modeling Labs (CML) on Cisco Sandbox to manage multiple network devices:

![CML Cisco Sandbox](image/CML_Cisco_Sandbox.png)

This case is for SSH, so you need to configure SSH for every device. By default, these devices use telnet.

The system processes natural language requests for network operations through Claude Desktop:

![Claude Desktop Integration](image/Claude_Desktop.png)

Example commands you can use:

```
"Show the running interfaces on the router R1"

"Configure interface GigabitEthernet0/1 with IP 192.168.1.1/24"

"Display the routing table"

"Ping 8.8.8.8 from router R1"
```

To use this tool, simply:
1. Configure your Claude Desktop with the MCP server
2. Open Claude Desktop and select the "Cisco-IOS-config" tool
3. Provide the network device credentials when prompted (HOST, USERNAME, PASSWORD)
4. Enter your network commands in natural language

## 🔍 Technical Details

### Technology Stack

- **Netmiko**: Powers SSH connections to Cisco devices
- **MCP**: Model Context Protocol for Claude integration
- **Python-dotenv**: Manages environment variables and secrets
- **FastMCP**: Provides the MCP server implementation

### Dependency Management

```bash
# Update all dependencies
uv pip compile pyproject.toml -o requirements.txt
uv pip sync requirements.txt

# Check for outdated packages
uv pip list --outdated
```

## 📦 Dependencies

Primary dependencies include:
- netmiko: Network device SSH connection management
- python-dotenv: Environment variable management
- mcp: Model Context Protocol for Claude integration

## 📞 Support

For questions or issues, please open an issue on our GitHub repository.

