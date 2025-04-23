from core.executor import execute_plan
from agent_local.llm_ollama import run_local_ai_reasoning
from agent_cloud.gemini_client import run_gemini_reasoning
from config.devices_config import USING_DEVICES
from logger.print_log import print_result, save_log_file

def run_ai_network_agent(mode="rule"):
    user_input = input("\n💬 Nhập đề bài cấu hình (hoặc 'exit'): ")
    if user_input.lower() == "exit":
        return

    if mode == "ollama":
        print("\n🧠 Đang phân tích đề bài bằng Mistral Local...")
        steps = run_local_ai_reasoning(user_input)
    elif mode == "gemini":
        print("\n🧠 Đang phân tích đề bài bằng Gemini AI...")
        steps = run_gemini_reasoning(user_input)
    else:
        print("\n⚙️ Phân tích đề bài bằng rule cơ bản...")
        if "ospf" in user_input.lower():
            steps = ["cấu hình ospf", "show ip ospf neighbor"]
        else:
            steps = ["ping 192.168.0.1"]

    print("\n📋 Kế hoạch hành động:", steps)
    print("\n📡 Bắt đầu thực hiện cấu hình...")

    logs = execute_plan(steps, USING_DEVICES)
    print_result(logs)
    save_log_file(logs)
