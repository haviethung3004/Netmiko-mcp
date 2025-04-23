from core.agent_controller import run_ai_network_agent
from core.utils import choose_mode

if __name__ == "__main__":
    mode = choose_mode()
    run_ai_network_agent(mode=mode)
