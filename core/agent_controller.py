from langgraph.graph import StateGraph
from logger.print_log import print_result, save_log_file
from core.state import AgentState
from core.plan_generator import generate_plan
from core.llm_reasoner import reason_about_task
from core.executor import execute_task
from core.utils import should_retry
from logger.print_log import log_step
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

# Hàm chính để khởi chạy agent bằng LangGraph
def run_langgraph_agent():
    # Cho phép nhập đề bài động từ dòng lệnh hoặc file
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", help="Nội dung task (e.g., 'Configure OSPF')", required=False)
    parser.add_argument("--task_file", help="Đường dẫn file chứa đề bài", required=False)
    args = parser.parse_args()

    # Ưu tiên task từ file nếu có
    if args.task_file and os.path.exists(args.task_file):
        with open(args.task_file, "r") as f:
            task_description = f.read().strip()
    elif args.task:
        task_description = args.task
    else:
        raise ValueError("Cần truyền --task hoặc --task_file để khởi tạo Agent")

    # Khởi tạo trạng thái ban đầu cho agent
    init_state = AgentState(task_description=task_description, retry_count=0)

    # Xây dựng LangGraph
    graph = StateGraph(AgentState)

    graph.add_node("plan", generate_plan)
    graph.add_node("reason", reason_about_task)
    graph.add_node("execute", execute_task)
    graph.add_node("retry_check", should_retry)
    graph.add_node("fix", fix_task)

    graph.set_entry_point("plan")
    graph.add_edge("plan", "reason")
    graph.add_edge("reason", "execute")
    graph.add_edge("execute", "retry_check")

    # Nếu có lỗi (ví dụ: neighbor, NAT...), đi nhánh fix, nếu không thì quay lại plan
    graph.add_conditional_edges(
        "retry_check",
        lambda s: "fix" if "fail" in (s.execution_result or "").lower() else "plan"
    )

    graph.add_edge("fix", "reason")  # Sau khi fix thì reasoning lại

    # Biên dịch và thực thi workflow
    workflow = graph.compile()
    result = workflow.invoke(init_state)

    print("✅ Final state:", result)

    # 👉 In log chi tiết từng bước và lưu vào file  
    print_result()
    save_log_file(task_name=task_description)
