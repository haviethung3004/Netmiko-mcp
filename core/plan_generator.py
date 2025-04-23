from agent_local.llm_ollama import run_local_ai_reasoning
from agent_gemini.llm_gemini import run_gemini_ai_reasoning
from logger.print_log import log_step

def generate_plan_by_mode(user_input, mode="rule"):
    if mode == "ollama":
        return run_local_ai_reasoning(user_input)
    elif mode == "gemini":
        return run_gemini_ai_reasoning(user_input)
    else:
        print("[!] Đang sử dụng chế độ rule đơn giản.")
        return rule_based_plan(user_input)

def rule_based_plan(text):
    text = text.lower()
    steps = []
    if "ospf" in text:
        steps.append("cấu hình ospf")
    if "neighbor" in text:
        steps.append("show ip ospf neighbor")
    if "ping" in text:
        steps.append("ping 192.168.0.1")
    if "nat" in text:
        steps.append("cấu hình nat")
    return steps


def generate_plan(state):
    steps = generate_plan_by_mode(state.task_description, mode="rule")
    state.plan = " -> ".join(steps)
    log_step("plan", state)
    return state
