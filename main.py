from langgraph.prebuilt import create_react_agent
from langchain_mistralai import ChatMistralAI
from agent_client.cisco_agent import AgentCiscoClient
from langchain.tools import tool
from langchain.prompts import PromptTemplate

import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize the agent client and model
cisco_agent = AgentCiscoClient()
model = ChatMistralAI(api_key=cisco_agent.api_key, model="mistral-large-2411")


# Initialize the template for the agent
template = """
You are a network engineer. You have access to a Cisco device. 
You can run commands on the device and get the output.
    1. Use [show_command] tool to get the output of show command, the input of this tool should a valid ios cisco command and will be a string
    2. Use [show_command] tool to get the output of config command, the input of this tool will be a list
        For example:
            Turn on interface ethernet 0/0
            config_command(["interface ethernet 0/0", "no shutdown"])
       Use [show_command] again to validate the configuration and will be a string
{messages}
"""

prompt_template = PromptTemplate.from_template(template)

# Define the tool for the agent to use
tool()
def show_command(command: str) -> str:
    """
    Send a command to the Cisco device and return the output.
    :param command: The command to be executed on the device.
    :return: The output of the command.
    """
    logger.info(f"Sending command: {command}")
    output = cisco_agent.show_command(command)
    print(output)
    return output if output else "Failed to execute command."


tool()
def config_command(command: list) -> str:
    """
    Send config commands to cisco device and return the output.
    :param config command: seperated by new line
    :return: The output of the command. 
    """
    logger.info(f"Sending command: {command}")
    output = cisco_agent.config_command(command)
    logger.info(output)
    return output if output else "Failed to execute command."
    
agent = create_react_agent(
    model=model,
    tools=[show_command, config_command],
    prompt=prompt_template,
)

# Run the agent with a sample command
if __name__ == "__main__":

    while True:
        user_input = input("Please input your question you want to ask the agent: ")
        inputs = {
            "messages":[("user", user_input)]
        }
        for s in agent.stream(inputs, stream_mode="values"):
            message = s["messages"][-1]
            if isinstance(message, tuple):
                print(message)
            else:
                message.pretty_print()
