from core.executor import execute_plan
from core.plan_generator import generate_plan_by_mode
from config.devices_config import USING_DEVICES

def run_ai_network_agent(mode="rule"):
    print(f"[!] Agent controller running mode: {mode}")

    while True:
        user_input = input("💬 Nhập đề bài (hoặc 'exit'): ")
        if user_input.lower() == "exit":
            break

        steps = generate_plan_by_mode(user_input, mode)
        logs = execute_plan(steps, USING_DEVICES)

        print("\n📄 Log kết quả:")
        for log in logs:
            print(log)
