import datetime
import os

# Danh sách log sẽ lưu tất cả các bước trong quá trình chạy agent
logs = []

def log_step(step_name: str, state):
    """
    Ghi lại trạng thái của từng bước xử lý trong LangGraph (plan, reason, execute, fix...).
    In ra màn hình và lưu vào danh sách logs để dùng về sau.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"[{timestamp}] [{step_name.upper()}] -> {state.dict()}"
    print(message)
    logs.append(message)

def print_result():
    """
    In toàn bộ kết quả logs cuối cùng sau khi agent hoàn tất.
    """
    print("\n📋 Tổng kết quá trình agent thực hiện:")
    print("\n".join(logs))

def save_log_file(task_name="network_task"):
    """
    Lưu log toàn bộ quá trình vào file .txt theo timestamp và tên task.
    Ví dụ: logs/log_Configure_OSPF_on_R1_20250423_170000.txt
    """
    folder = "logs"
    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_task_name = task_name.replace(" ", "_").replace("/", "_")[:30]
    filename = f"{folder}/log_{safe_task_name}_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(logs))

    print(f"\n📝 Log đã được lưu tại: {filename}")
