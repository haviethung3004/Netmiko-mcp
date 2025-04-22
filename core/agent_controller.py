from core.llm_reasoner import generate_plan
from config.devices_config import USING_DEVICES
from core.executor import execute_plan

def run_ai_network_agent():
    print("🤖 AI Network Engineer Agent (Upgraded)")

    while True:
        user_input = input("\n💬 Nhập đề bài cấu hình (hoặc 'exit'): ")
        if user_input.lower() == "exit":
            break

        print("\n🧠 Đang phân tích đề bài bằng AI...")
        steps = generate_plan(user_input)
        print("\n📋 Kế hoạch:")
        for i, step in enumerate(steps, 1):
            print(f"  {i}. {step}")

        print("\n🧪 Thực thi:")
        logs = execute_plan(steps, USING_DEVICES)
        for log in logs:
            print(log)