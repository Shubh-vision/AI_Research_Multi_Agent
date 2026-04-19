from state.state import AgentState
from tools.tool import web_search


#===============================Search Agent ==================================

def search_node(state: AgentState):

    result = web_search(state["query"])
    return {**state, "search_result": result}