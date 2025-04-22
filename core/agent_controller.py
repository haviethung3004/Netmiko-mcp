from agent_local.llm_ollama import run_local_ai_reasoning
from agent_local.llm_gemini import run_gemini_ai_reasoning
from agent_local.fallback_reasoner import fallback_reasoning
from config.devices_config import USING_DEVICES
from core.executor import execute_plan

def run_ai_network_agent(mode="ollama"):
    print(f"🤖 AI Network Engineer Agent (Chế độ: {mode})")

    while True:
        user_input = input("\n💬 Nhập đề bài cấu hình (hoặc 'exit'): ")
        if user_input.lower() == "exit":
            break

        print("\n🧠 Đang phân tích đề bài...")

        if mode == "ollama":
            plan = run_local_ai_reasoning(user_input)
        elif mode == "gemini":
            plan = run_gemini_ai_reasoning(user_input)
        else:
            plan = fallback_reasoning(user_input)

        print("\n📋 Kế hoạch:")
        for i, step in enumerate(plan, 1):
            print(f"  {i}. {step}")

        print("\n🛠️ Thực thi:")
        logs = execute_plan(plan, USING_DEVICES)

        for log in logs:
            print(log)