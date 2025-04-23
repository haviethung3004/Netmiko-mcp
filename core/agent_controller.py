from langgraph.graph import StateGraph
from logger.print_log import print_result, save_log_file, log_step
from core.state import AgentState
from core.plan_generator import generate_plan_by_mode
from core.llm_reasoner import reason_about_task
from core.executor import execute_task
from core.utils import should_retry
import argparse
import os

# Node xử lý lỗi: kiểm tra nội dung lỗi và chỉnh lại kế hoạch nếu phát hiện sự cố rõ ràng
def fix_task(state):
    if state.execution_result:
        if "neighbor" in state.execution_result.lower():
            state.plan = "Fix OSPF neighbor issue: reconfigure router-id or adjust area config"
        elif "nat" in state.execution_result.lower():
            state.plan = "Fix NAT issue: check ip nat inside/outside and access-list"
        else:
            state.plan = "Generic fix: retry last configuration with modification"
    else:
        state.plan = "Fallback: re-attempt previous plan"
    log_step("fix", state)
    return state

# ✅ Agent thông minh dùng LangGraph + AI (Ollama, Gemini, Rule) chọn theo mode
def run_langgraph_agent():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", help="Nội dung task (e.g., 'Configure OSPF')", required=False)
    parser.add_argument("--task_file", help="Đường dẫn file chứa đề bài", required=False)
    parser.add_argument("--mode", help="Chọn chế độ AI reasoning: ollama / gemini / rule", default="rule")
    args = parser.parse_args()

    if args.task_file and os.path.exists(args.task_file):
        with open(args.task_file, "r") as f:
            task_description = f.read().strip()
    elif args.task:
        task_description = args.task
    else:
        raise ValueError("Cần truyền --task hoặc --task_file để khởi tạo Agent")

    init_state = AgentState(task_description=task_description, retry_count=0)
    mode = args.mode

    # 🌐 LangGraph với LLM reasoning theo chế độ
    def generate_plan_with_mode(state):
        steps = generate_plan_by_mode(state.task_description, mode=mode)
        state.plan = " -> ".join(steps)
        log_step("plan", state)
        return state

    graph = StateGraph(AgentState)
    graph.add_node("plan", generate_plan_with_mode)
    graph.add_node("reason", reason_about_task)
    graph.add_node("execute", execute_task)
    graph.add_node("retry_check", should_retry)
    graph.add_node("fix", fix_task)

    graph.set_entry_point("plan")
    graph.add_edge("plan", "reason")
    graph.add_edge("reason", "execute")
    graph.add_edge("execute", "retry_check")
    graph.add_conditional_edges(
        "retry_check",
        lambda s: "fix" if "fail" in (s.execution_result or "").lower() else "plan"
    )
    graph.add_edge("fix", "reason")

    workflow = graph.compile()
    result = workflow.invoke(init_state)

    print("✅ Final state:", result)
    print_result()
    save_log_file(task_name=task_description)
