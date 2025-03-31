# Network Automation Tool

A powerful tool for automating Cisco network device configuration and management using AI-powered assistance.

## Overview

This project provides an interface for interacting with Cisco network devices. It allows for executing both show commands and configuration commands with a focus on simplifying network management tasks.

## Features

- Execute show commands on Cisco devices
- Apply configuration changes to network devices
- Natural language processing of network commands
- Simplified network management workflows

## Requirements

- Python 3.13+
- Cisco network device(s) accessible via SSH
- API key for Mistral AI or OpenAI

## Python Environment Management

This project uses UV for efficient Python environment and package management. UV is a modern, fast Python package installer and resolver that significantly outperforms pip.

1. Install UV:
   ```bash
   # Install UV using pip
   pip install uv
   
   # Verify installation
   uv --version
   ```

2. Create and activate a virtual environment with UV:
   ```bash
   # Navigate to your project directory
   cd MCP_Network_automate
   
   # Create virtual environment
   uv venv
   
   # Activate the virtual environment
   # On Windows
   .venv\Scripts\activate
   ```

3. Install dependencies with UV:
   ```bash
   # Sync dependencies
   uv sync
   ```

4. Update dependencies:
   ```bash
   # Update dependencies to their latest compatible versions
   uv pip compile pyproject.toml -o requirements.txt
   
   # Apply updates
   uv pip sync requirements.txt
   ```

5. Check for outdated packages:
   ```bash
   uv pip list --outdated
   ```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd MCP_Network_automate
   ```

2. Install dependencies using UV:
   ```bash
   # Install UV if not already installed
   pip install uv
   
   # Set up virtual environment and install dependencies
   uv venv
   .venv\Scripts\activate
   uv pip install -e .
   ```

3. Create a `.env` file with the following variables:
   ```
   CISCO_HOST=<your_cisco_device_ip>
   CISCO_USERNAME=<your_cisco_username>
   CISCO_PASSWORD=<your_cisco_password>
   API_KEY=<your_api_key> # Don't use for this project
   ```

## Components

- `agent_client/agent_connector.py`: Core connector for Cisco device interaction, handling SSH connections and command execution
- `mcp_server.py`: Server implementation for network automation tools

## Example Commands

The system can process natural language requests like:

```
Show the running interfaces on the router

Configure interface GigabitEthernet0/1 with IP 192.168.1.1/24

Display the routing table

Check the status of BGP neighbors
```

## How It Works

The tool uses:
- **Netmiko**: For SSH connections to Cisco devices
- **Python-dotenv**: For environment variable management
- **Large Language Models**: For understanding network engineering requests

```bash
#Install mcp server to your Claude Desktop
mcp install mcp_server.py

#Inscpect your tool
mcp dev mcp_server.py
```

## Dependencies

This project relies on several key Python packages:
- netmiko: For network device connections
- python-dotenv: For environment management
- mistralai/openai: For AI capabilities
- pydantic: For data validation

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]

