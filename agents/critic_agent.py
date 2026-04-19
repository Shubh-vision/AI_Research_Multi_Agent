
from agents.search_agent import search_node
from agents.writer_agent import writer_node
from langchain_core.prompts import ChatPromptTemplate
from state.state import AgentState
from llm.llm import llm, parser
import re
from langgraph.graph import StateGraph, START, END


critic_prompt = ChatPromptTemplate.from_template("""
Evaluate this report briefly.

{report}

Return:
Score: X/10
One-line feedback:
""")

critic_chain = critic_prompt | llm | parser
def critic_node(state: AgentState):

    
    feedback = critic_chain.invoke({"report": state["report"]})

    match = re.search(r"Score:\s*(\d+)/10", feedback)
    score = int(match.group(1)) if match else 5

    return {
        **state,
        "feedback": feedback,
        "score": score
    }


# ---------------- DECISION ----------------
def decision(state: AgentState):
    if state["score"] < 7:
        return "writer"
    return END

