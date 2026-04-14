from state.state import AgentState
from langgraph.graph import StateGraph, END
from agents.search_agent import search_node
from agents.reader_agent import reader_node
from agents.writer_agent import writer_node
from agents.critic_agent import critic_node

graph = StateGraph(AgentState)

graph.add_node("search", search_node)
graph.add_node("reader", reader_node)
graph.add_node("writer", writer_node)
graph.add_node("critic", critic_node)

graph.set_entry_point("search")

graph.add_edge("search", "reader")
graph.add_edge("reader", "writer")
graph.add_edge("writer", "critic")
graph.add_edge("critic", END)


app = graph.compile()

