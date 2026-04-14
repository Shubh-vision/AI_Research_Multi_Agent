from typing import TypedDict

class AgentState(TypedDict):
    query: str
    search_result: list
    content: str
    report: str
    feedback: str
