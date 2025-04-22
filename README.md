# AI Network Engineer Agent (Upgraded)

## Cách chạy

```bash
pip install -r requirements.txt
python run_agent.py
```

## Yêu cầu
- Thiết bị Cisco (GNS3, thật, Packet Tracer)
- Đã cấu hình IP và có thể SSH từ máy bạn

## Tính năng
- AI hiểu đề bài tiếng Việt
- Sinh kế hoạch hành động
- Cấu hình OSPF, NAT, VLAN thật bằng Netmiko
- Log từng bước thực thi

# AI Network Agent - Phiên bản nâng cấp

## Tính năng:
✅ AI reasoning: Gemini, Ollama local, fallback rule  
✅ Kết nối nhiều thiết bị (Netmiko)  
✅ Tự sửa lỗi nếu ping/neighbor fail  
✅ Giao diện CLI gọn nhẹ  
✅ Log từng bước thực hiện

## Cách chạy:
```bash
pip install -r requirements.txt
python run_agent.py --mode ollama
```
Chọn `--mode`:
- `ollama`: Dùng AI local Mistral
- `gemini`: Dùng Google Gemini (nhập API key vào `.env`)
- `rule`: Không AI, chỉ rule đơn giản
test
# B1. Tạo môi trường ảo
python -m venv venv
venv\Scripts\activate

# B2. Cài thư viện
pip install netmiko

# B3. Chạy chương trình
python run_agent.py
Bạn sẽ thấy giao diện chọn số xuất hiện:
🔥 Chọn chế độ hoạt động:
1. AI Local (Ollama)
2. Google Gemini
3. Rule Matching (không dùng AI)
> Nhập số:


🐳 Docker hỗ trợ đầy đủ:
Python 3.10+

pyATS, Netmiko, Unicon

Langchain, Gemini SDK, Requests

Ollama CLI (tùy chọn cài nếu dùng local)
# Build Docker Image
docker build -t ai-network-automator .

# Chạy interactive
docker run -it --env-file .env ai-network-automator
