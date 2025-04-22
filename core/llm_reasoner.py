def generate_plan(prompt):
    prompt = prompt.lower()
    if "ospf" in prompt:
        return ["cấu hình ospf", "show ip ospf neighbor", "ping đến router kế bên", "cấu hình nat"]
    elif "vlan" in prompt:
        return ["tạo vlan", "gán port vào vlan", "show vlan"]
    else:
        return ["không nhận diện được yêu cầu"]