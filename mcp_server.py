from mcp.server.fastmcp import FastMCP
from agent_client.agent_connector import AgentClient

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
    Send a command to the Cisco device and return the output, the input of this tool should a valid ios cisco command and will be a string
    :param command: The command to be executed on the device.
    :return: The output of the command.
    """
    print(f"Sending command: {command}")
    output = cisco_agent.show_command(command, HOST, USERNAME, PASSWORD)
    return output if output else "Failed to execute command."

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Start the MCP server
    mcp.run(transport='stdio')