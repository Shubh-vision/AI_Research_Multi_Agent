from typing import TypedDict

class AgentState(TypedDict):
    query: str
    search_result: str
    urls: list
    reader_result: str
    report: str
    feedback: str
    score: int
