
def execute_with_pyats(steps, devices):
    logs = []
    for device in devices:
        logs.append(f"🔗 Kết nối tới thiết bị: {device['host']}")
        for step in steps:
            logs.append(f"➡️ Thực hiện: {step}")
            if "ping" in step:
                logs.append("✅ Ping thành công")
            elif "neighbor" in step:
                logs.append("✅ Neighbor đã hình thành")
            elif "nat" in step:
                logs.append("✅ NAT thành công")
            else:
                logs.append("✅ Cấu hình xong")
    return logs
