from netmiko import ConnectHandler
from dotenv import load_dotenv, find_dotenv
import os
import logging

# Load environment variables from .env file
load_dotenv(find_dotenv(), override=True)


# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AgentClient:

    def __init__(self):
    
        self.device_info = {
            'device_type': 'cisco_ios',
            'host': os.getenv("CISCO_HOST"),
            'username': os.getenv("CISCO_USERNAME"),
            'password': os.getenv("CISCO_PASSWORD"),
        }

    def connect_to_device(self, device_info):
        try:
            connection = ConnectHandler(**device_info)
            print(f"Connected to {device_info['host']}")
            return connection
        except Exception as e:
            print(f"Failed to connect to {device_info['host']}: {e}")
            return None
    
if __name__ == "__main__":
    device_info = {
        'device_type': 'cisco_ios',
        'host': '192.168.1.28',
        'username': 'admin',
        'password': 'cisco',
    }

    connection = connect_to_device(device_info)


