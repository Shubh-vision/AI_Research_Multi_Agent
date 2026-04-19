from state.state import AgentState
from tools.tool import fetch_url
from agents.search_agent import search_node
from agents.extract_agent import extract_node

def reader_node(state: AgentState):
    data = []

    for url in state["urls"]:
        data.append(fetch_url(url))

    return {**state, "reader_result": "\n\n".join(data)}

# def reader_node(state: AgentState):

#     results = state.get("search_result", [])

#     if not results:
#         return {**state, "content": ""}

#     url = results[0]["url"]  # ✅ now works

#     content = fetch_url(url)

#     return {**state, "content": content}




