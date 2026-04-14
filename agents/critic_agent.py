
from agents.search_agent import search_node
from langchain_core.prompts import ChatPromptTemplate
from state.state import AgentState
from llm.llm import llm, parser
import re


critic_prompt = ChatPromptTemplate.from_template("""
Evaluate this report briefly.

{report}

Give:
Score: X/10
One-line feedback:
""")

def critic_node(state: AgentState):
    print("\n🧑‍⚖️ Evaluating...")

    chain = critic_prompt | llm | parser
    feedback = chain.invoke({"report": state["report"]})

    return {**state, "feedback": feedback}

