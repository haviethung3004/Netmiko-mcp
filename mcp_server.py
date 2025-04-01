from mcp.server.fastmcp import FastMCP
from agent_client.agent_connector import AgentClient
from typing import List


#Create an MCP server
mcp = FastMCP("Cisco-IOS-config")

cisco_agent = AgentClient()

@mcp.tool()
def config_command(command, HOST, USERNAME, PASSWORD) -> str:
    """
    Send config commands to cisco device and return the output, the input of this tool should a valid ios cisco command and will be a list
    :param config command: seperated by new line
    :return: The output of the command. 
    """
    print(f"Sending command: {command}")
    output = cisco_agent.config_command(command, HOST, USERNAME, PASSWORD)
    return output if output else "Failed to execute command."


@mcp.tool()
def show_command(command, HOST, USERNAME, PASSWORD) -> str:
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

    print(f"Sending command: {command}")
    output = cisco_agent.show_command(command, HOST, USERNAME, PASSWORD)
    return output if output else "Failed to execute command."

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
    print(f"Fetching information for device(s): {list_device}")
    return {"device": list_device}


if __name__ == "__main__":
    # Start the MCP server
    mcp.run(transport='stdio')