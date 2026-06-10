from state.state import AgentState
from tools.tool import fetch_url
from agents.search_agent import search_node
from agents.extract_agent import extract_node

def reader_node(state: AgentState):
    docs = []

    for article in state["search_result"]:

        docs.append(
            f"""
            Date: {article.get('published_date')}
            Title: {article['title']}
            URL: {article['url']}
            {article['content'][:1000]}
            """
        )

    return {
        **state,
        "reader_result": "\n\n".join(docs)
    }
 



