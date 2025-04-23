def fallback_reasoning(prompt):
    if "ospf" in prompt.lower():
        return ["cấu hình ospf", "show ip ospf neighbor", "ping đến router kế bên", "cấu hình nat"]
    if "vlan" in prompt.lower():
        return ["tạo vlan", "gán port vào vlan", "show vlan"]
    return ["không nhận diện được yêu cầu"]