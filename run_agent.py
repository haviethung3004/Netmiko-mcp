import argparse
from core.agent_controller import run_ai_network_agent

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=str, default="ollama", help="Chế độ AI: ollama, gemini, rule")
    args = parser.parse_args()

    run_ai_network_agent(mode=args.mode)