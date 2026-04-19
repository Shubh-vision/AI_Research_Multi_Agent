from agents.search_agent import search_node
from state.state import AgentState
from langchain_core.prompts import ChatPromptTemplate
from llm.llm import llm, parser
import re

# ---------------- EXTRACT NODE ----------------
extract_prompt = ChatPromptTemplate.from_template("""
From search result below extract top 3 URLs.

Return only URLs one per line.

Search:
{search}
""")

extract_chain = extract_prompt | llm | parser


def extract_node(state: AgentState):
    urls_text = extract_chain.invoke({"search": state["search_result"]})

    urls = re.findall(r'https?://\\S+', urls_text)

    return {**state, "urls": urls[:3]}