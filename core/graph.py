from langgraph.graph import StateGraph
from core.state import AgentState
from core.llm_reasoner import llm_reasoner
from core.executor import executor_function

graph = StateGraph(AgentState)

graph.add_node("reason", llm_reasoner)
graph.add_node("execute", executor_function)

graph.set_entry_point("reason")
graph.add_edge("reason", "execute")
graph.add_edge("execute", "reason")  # nếu muốn loop theo trạng thái

workflow = graph.compile()
