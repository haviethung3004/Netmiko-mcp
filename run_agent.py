from core.agent_controller import run_ai_network_agent

def select_mode():
    print("""
🔥 Chọn chế độ hoạt động:
1. AI Local (Ollama)
2. Google Gemini
3. Rule Matching (không dùng AI)
    """)
    mode_map = {'1': 'ollama', '2': 'gemini', '3': 'rule'}
    choice = input("> Nhập số (1/2/3): ").strip()
    return mode_map.get(choice, 'rule')

if __name__ == "__main__":
    mode = select_mode()
    print(f"🤖 AI Network Engineer Agent (Chế độ: {mode})")
    run_ai_network_agent(mode=mode)
