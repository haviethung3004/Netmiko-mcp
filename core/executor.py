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
                    logs.append(f"[{device['host']}] ✅ Cấu hình OSPF")
                elif "show ip ospf neighbor" in step:
                    output = conn.send_command("show ip ospf neighbor")
                    logs.append(f"[{device['host']}] 👁️ Neighbor:\n{output}")
                    if "FULL" not in output:
                        logs.append(f"[{device['host']}] ⚠️ Neighbor chưa FULL, thử ping...")
                        ping = conn.send_command("ping 192.168.0.2")
                        logs.append(f"[{device['host']}] 📡 Ping:\n{ping}")
                elif "ping" in step:
                    output = conn.send_command("ping 192.168.0.2")
                    logs.append(f"[{device['host']}] 📡 Ping:\n{output}")
                elif "nat" in step:
                    cmds = ["ip nat inside source list 1 interface FastEthernet0/1 overload"]
                    output = conn.send_config_set(cmds)
                    logs.append(f"[{device['host']}] ✅ Cấu hình NAT")
                else:
                    logs.append(f"[{device['host']}] ⚠️ Không xử lý được bước: {step}")
            conn.disconnect()
        except Exception as e:
            logs.append(f"❌ Lỗi khi xử lý thiết bị {device['host']}: {e}")
    return logs
