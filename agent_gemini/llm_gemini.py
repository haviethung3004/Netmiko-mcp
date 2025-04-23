import os
import requests

def run_gemini_ai_reasoning(user_input):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("[❌] Không tìm thấy API key cho Gemini. Hãy đặt trong .env với biến: GEMINI_API_KEY")
        return []

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    prompt = f"""
Bạn là một kỹ sư mạng AI. Hãy phân tích đề bài sau và trả về danh sách các bước cần làm dưới dạng JSON Python List.
Đề bài: {user_input}
Chỉ trả về list JSON như: ["bước 1", "bước 2", ...]
    """.strip()

    try:
        response = requests.post(
            "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent",
            params={"key": api_key},
            headers=headers,
            json={"contents": [{"parts": [{"text": prompt}]}]}
        )
        data = response.json()
        text = data['candidates'][0]['content']['parts'][0]['text']
        plan = eval(text.strip())
        return plan
    except Exception as e:
        print("[❌] Lỗi gọi API Gemini:", e)
        return []
