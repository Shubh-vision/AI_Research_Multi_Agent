from state.state import AgentState
from tools.tool import web_search


#===============================Search Agent ==================================

def search_node(state: AgentState):

    results = web_search(state["query"])

    urls = [r["url"] for r in results]

    return {
        **state,
        "search_result": results,
        "urls": urls
    }