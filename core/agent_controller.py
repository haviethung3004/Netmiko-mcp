from langgraph.graph import StateGraph
from core.state import AgentState
from core.plan_generator import generate_plan
from core.llm_reasoner import reason_about_task
from core.executor import execute_task
from core.utils import should_retry

def run_langgraph_agent():
    """Khởi chạy AI Agent dùng LangGraph để tự động lên kế hoạch, cấu hình và xử lý lỗi."""

    # 1. Khởi tạo LangGraph với trạng thái là AgentState
    graph = StateGraph(AgentState)

    # 2. Thêm các node: lập kế hoạch, reasoning, thực thi, kiểm tra retry
    graph.add_node("plan", generate_plan)
    graph.add_node("reason", reason_about_task)
    graph.add_node("execute", execute_task)
    graph.add_node("retry_check", should_retry)

    # 3. Thiết lập entry point và luồng đi
    graph.set_entry_point("plan")
    graph.add_edge("plan", "reason")
    graph.add_edge("reason", "execute")
    graph.add_edge("execute", "retry_check")

    # 4. Điều kiện lặp lại nếu lỗi (dựa vào retry_count)
    graph.add_conditional_edges("retry_check", lambda state: "plan" if state.retry_count < 3 else "end")

    # 5. Compile và chạy với trạng thái ban đầu
    workflow = graph.compile()
    init_state = AgentState(task_description="Configure OSPF on R1", retry_count=0)

    result = workflow.invoke(init_state)
    print("✅ Final state:", result)
