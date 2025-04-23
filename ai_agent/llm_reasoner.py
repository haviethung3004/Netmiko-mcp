
def generate_plan(prompt):
    prompt = prompt.lower()
    if "ospf" in prompt:
        return ["cấu hình ospf", "kiểm tra neighbor", "nếu lỗi thì ping", "nếu ok thì cấu hình nat"]
    elif "vlan" in prompt:
        return ["tạo vlan", "gán vlan vào port", "kiểm tra vlan bằng show vlan"]
    else:
        return ["không nhận diện được yêu cầu, vui lòng mô tả rõ hơn"]
