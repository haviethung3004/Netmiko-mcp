from pydantic import BaseModel

class AgentState(BaseModel):
    task_description: str
    plan: str = None
    reasoning: str = None
    execution_result: str = None
    retry_count: int = 0
