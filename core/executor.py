from netmiko import ConnectHandler

def execute_plan(steps, devices):
    logs = []
    for device in devices:
        logs.append(f"🔗 Kết nối tới {device['host']}")
        try:
            conn = ConnectHandler(**device)
            conn.enable()
            for step in steps:
                if "ospf" in step:
                    cmds = ["router ospf 1", "network 192.168.0.0 0.0.0.255 area 0"]
                    output = conn.send_config_set(cmds)
                    logs.append(f"[{device['host']}] ✅ Đã cấu hình OSPF")

                elif "neighbor" in step:
                    output = conn.send_command("show ip ospf neighbor")
                    logs.append(f"[{device['host']}] 👁️ Neighbor:\n{output}")

                elif "ping" in step:
                    output = conn.send_command("ping 192.168.0.1")
                    logs.append(f"[{device['host']}] 📡 Ping:\n{output}")

                else:
                    logs.append(f"[{device['host']}] ⚠️ Không rõ bước: {step}")

            conn.disconnect()

        except Exception as e:
            logs.append(f"❌ Lỗi khi xử lý thiết bị {device['host']}: {e}")
    return logs
