from mcp.server.fastmcp import FastMCP
from agent_client.agent_connector import AgentClient
from typing import List


#Create an MCP server
mcp = FastMCP("Cisco-IOS-config")

cisco_agent = AgentClient()

@mcp.tool()
def config_cisco_command(command, HOST, USERNAME, PASSWORD) -> str:
    """
    Send config commands to cisco device and return the output, the input of this tool should a valid ios cisco command and will be a list
    :param config command: seperated by new line
    :return: The output of the command. 
    """
    try:
        output = cisco_agent.config_command(command, HOST, USERNAME, PASSWORD)
        return output
    except Exception as e:
        return f"Error: {e}"

@mcp.tool()
def show_cisco_command(command, HOST, USERNAME, PASSWORD) -> str:
    """
    Send a 'show' command to the Cisco device and return the output.
    
    Args:
        command: A valid Cisco IOS 'show' command (e.g., "show running-config").
        host: IP/DNS of the Cisco device.
        username: Username for authentication.
        password: Password for authentication.
    
    Returns:
        str: Output of the command execution.
    """
    try:
        output = cisco_agent.show_command(command, HOST, USERNAME, PASSWORD)
        return output
    except Exception as e:
        return f"Error: {e}"

@mcp.tool()
def send_linux_command(command, HOST, USERNAME, PASSWORD) -> str:
    """
    Send commands to Linux device and return device output.

    Args:
        command: A valid Linux command (e.g., "ls -l").
        host: IP/DNS of the Linux device.
        username: Username for authentication.
        password: Password for authentication.
    """
    try:
        output = cisco_agent.linux_command(commands=command, HOST=HOST, USERNAME=USERNAME, PASSWORD=PASSWORD)
        return output
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
def ping_cisco_device(command, HOST, USERNAME, PASSWORD) -> str:
    """
    Send a ping command to the Cisco device and return the output.
    The input should valid  ios ping cisco command with the "ping" keyword.
    """
    try:
        output = cisco_agent.ping_cisco_command(command, HOST, USERNAME, PASSWORD)
        return output
    except Exception as e:
        return f"Error: {e}"
    

# Define a dynamic resource to list devices
@mcp.resource("device://{list_device}")
def get_device(list_device):
    """
    Send configuration commands to a Cisco device and return the output.
    
    Args:
        commands: List of valid Cisco IOS configuration commands.
        host: IP/DNS of the Cisco device.
        username: Username for authentication.
        password: Password for authentication.
    
    Returns:
        str: Output of the command execution.
    """
    return {"device": list_device}


if __name__ == "__main__":
    # Start the MCP server
    mcp.run(transport='stdio')