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
============================================================================================
 TỔNG QUAN NÂNG CẤP (trên nền MCP_Network_automator gốc)

Thành phần	Nâng cấp chi tiết
🧠 Tích hợp AI đa chế độ: Cho phép chọn giữa 3 chế độ AI khi chạy:
-> AI Local (Ollama Mistral)
-> AI Cloud (Gemini API)
-> Rule Matching (nội suy đơn giản không cần AI)
🧱 Giữ nguyên cấu trúc cũ: Mọi thư mục và phân chia như agent_local, agent_cloud, core, logger, config được giữ nguyên nhưng có bổ sung logic mới
🖥️ Cải tiến CLI dễ dùng: Giao diện dòng lệnh với menu chọn số 1 / 2 / 3 giúp chọn chế độ AI dễ dàng
⚙️ Xử lý lệnh mạng thực: Trong core/executor.py, lệnh OSPF, show ip ospf neighbor, ping, NAT... được gửi bằng Netmiko
📡 Kết nối nhiều thiết bị: Cho phép gửi cấu hình qua nhiều thiết bị định nghĩa trong config/devices_config.py
🧪 Tự kiểm tra lỗi cấu hình: Nếu OSPF neighbor chưa "FULL", sẽ tự động ping kiểm tra lại kết nối
📁 Tự ghi log cấu hình: Kết quả được in ra màn hình và có thể lưu log (logger/print_log.py)
🧩 Tùy chọn AI Local: Có thể chạy mà không cần mạng nếu dùng --mode ollama (khi cài Mistral qua Ollama)
🔐 Tùy chọn AI Gemini API	Nếu dùng Google Gemini thì chỉ cần đặt key trong .env
🐳 Chuẩn bị Dockerfile & cấu trúc build: Đã hỗ trợ project chạy được trong Docker (bản nâng cao sẽ cập nhật thêm pyATS sau)
📦 requirements.txt & khởi tạo môi trường: Có đầy đủ hướng dẫn tạo venv, requirements.txt, khởi chạy đúng cách