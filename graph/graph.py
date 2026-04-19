from state.state import AgentState
from langgraph.graph import StateGraph, END, START
from agents.search_agent import search_node
from agents.reader_agent import reader_node
from agents.writer_agent import writer_node
from agents.critic_agent import critic_node, decision
from agents.extract_agent import extract_node

graph = StateGraph(AgentState)

# Nodes
graph.add_node("search", search_node)
graph.add_node("extract", extract_node)
graph.add_node("reader", reader_node)
graph.add_node("writer", writer_node)
graph.add_node("critic", critic_node)

# Edges
graph.add_edge(START, "search")
graph.add_edge("search", "extract")
graph.add_edge("extract", "reader")
graph.add_edge("reader", "writer")
graph.add_edge("writer", "critic")

graph.add_conditional_edges(
    "critic",
    decision,
    {
        "writer": "writer",
        END: END
    }
)


app = graph.compile()

