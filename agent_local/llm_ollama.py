import subprocess

def run_local_ai_reasoning(prompt):
    print("💡 AI Local (Ollama - Mistral) đang phân tích...")
    try:
        process = subprocess.Popen(
            ["ollama", "run", "mistral"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )
        prompt_text = f"""Hãy phân tích đề bài sau và trả về một danh sách các bước thực hiện cấu hình mạng:
{prompt}
Trả lời bằng Python list."""
        output, _ = process.communicate(prompt_text)
        steps = eval(output.split("```")[0].strip()) if "```" in output else eval(output)
        return steps if isinstance(steps, list) else ["Không nhận diện được bước."]
    except Exception:
        return ["Không thể phân tích đề bài bằng AI Local."]
