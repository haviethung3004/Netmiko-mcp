def choose_mode():
    print("\n🔥 Chọn chế độ hoạt động:")
    print("1. AI Local (Ollama)")
    print("2. Google Gemini")
    print("3. Rule Matching (không dùng AI)")
    while True:
        mode_input = input("\n> Nhập số (1/2/3): ").strip()
        if mode_input == "1":
            return "ollama"
        elif mode_input == "2":
            return "gemini"
        elif mode_input == "3":
            return "rule"
        else:
            print("Vui lòng nhập đúng số 1, 2 hoặc 3.")
