import os
import requests

def run_gemini_ai_reasoning(prompt):
    print("🔮 AI Gemini đang phân tích...")
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        response = requests.post(
            "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent",
            headers=headers,
            json=data
        )
        raw = response.json()
        text = raw['candidates'][0]['content']['parts'][0]['text']
        return eval(text) if isinstance(eval(text), list) else ["Gemini không phân tích được."]
    except Exception:
        return ["Không thể kết nối Gemini."]