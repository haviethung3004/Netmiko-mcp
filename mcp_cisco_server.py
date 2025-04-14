import asyncio
from mcp.server.fastmcp import FastMCP
from agent_client.cisco_agent import AgentCiscoClient

# Create MCP server
mcp = FastMCP(name="Cisco-IOS-config", instructions="""
            You are an expert network engineer. You have access to a Cisco device.""",
            debug=True, log_level="DEBUG")

cisco_agent = AgentCiscoClient()

@mcp.tool()
async def config_cisco_command(command, HOST, USERNAME, PASSWORD) -> str:
    """
    Send config commands to cisco device and return the output, the input of this tool should a valid ios cisco command and will be a list
    You don't need to add the "conf t" command in the input, it will be added automatically.
    Args:
    :param config command: separated by new line
    :return: The output of the command. 
    """
    try:
        # Run in thread with timeout to prevent blocking
        output = await asyncio.wait_for(
            asyncio.to_thread(cisco_agent.config_command, command, HOST, USERNAME, PASSWORD),
            timeout=30.0
        )
        return output
    except asyncio.TimeoutError:
        return "Error: Command timed out"
    except Exception as e:
        return f"Error: {e}"

@mcp.tool()
async def show_cisco_command(command, HOST, USERNAME, PASSWORD) -> str:
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
        output = await asyncio.wait_for(
            asyncio.to_thread(cisco_agent.show_command, command, HOST, USERNAME, PASSWORD),
            timeout=30.0
        )
        return output
    except asyncio.TimeoutError:
        return "Error: Command timed out"
    except Exception as e:
        return f"Error: {e}"

@mcp.tool()
async def ping_cisco_device(command, HOST, USERNAME, PASSWORD) -> str:
    """
    Send a ping command to the Cisco device and return the output.
    The input should valid ios ping cisco command with the "ping" keyword.
    """
    try:
        output = await asyncio.wait_for(
            asyncio.to_thread(cisco_agent.ping_cisco_command, command, HOST, USERNAME, PASSWORD),
            timeout=30.0
        )
        return output
    except asyncio.TimeoutError:
        return "Error: Command timed out"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
