
from ai_agent.llm_reasoner import generate_plan
from config.devices_config import USING_DEVICES
from pyats_executor.handler import execute_with_pyats

def run_ai_network_agent():
    print("🧠 AI Network Agent Started")

    while True:
        user_input = input("\n💬 Nhập đề bài (hoặc 'exit'): ")
        if user_input.lower() == "exit":
            break

        print("\n🤖 Đang phân tích đề bài với AI reasoning...")
        steps = generate_plan(user_input)
        print("\n📋 Kế hoạch hành động:")
        for i, step in enumerate(steps, 1):
            print(f"  {i}. {step}")

        logs = execute_with_pyats(steps, USING_DEVICES)
        print("\n🧾 Kết quả:")
        for log in logs:
            print(log)
