from state.state import AgentState
from tools.tool import fetch_url
from agents.search_agent import search_node

def reader_node(state: AgentState):
    print("\n🌐 Reading...")

    results = state.get("search_result", [])

    if not results:
        return {**state, "content": ""}

    url = results[0]["url"]  # ✅ now works

    content = fetch_url(url)

    return {**state, "content": content}




