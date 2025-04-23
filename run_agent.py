from core.agent_controller import run_ai_network_agent, run_langgraph_agent
from core.utils import choose_mode

if __name__ == "__main__":
    mode = choose_mode()
    print(f"🚀 Starting AI Network Agent in mode: {mode}")

    if mode == "langgraph":
        run_langgraph_agent()
    else:
        run_ai_network_agent(mode=mode)
