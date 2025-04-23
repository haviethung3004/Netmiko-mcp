from datetime import datetime

def print_result(logs):
    print("\n📝 Kết quả thực hiện:")
    for line in logs:
        print(line)

def save_log_file(logs):
    filename = f"logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for line in logs:
            f.write(line + "\n")
    print(f"\n💾 Log đã được lưu tại: {filename}")
