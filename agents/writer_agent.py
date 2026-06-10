from state.state import AgentState
from langchain_core.prompts import ChatPromptTemplate
from llm.llm import llm, parser
from agents.reader_agent import reader_node


writer_prompt = ChatPromptTemplate.from_template("""
You MUST use only the provided data.

Never use your own knowledge.

Every key finding must be supported by the supplied data.

If the data does not contain the answer, explicitly say so.

Topic:
{query}

Data:
{data}

Include:
- Introduction
- Key Findings
- Conclusion
- Sources
""")

writer_chain = writer_prompt | llm | parser

def writer_node(state: AgentState):
    report = writer_chain.invoke({
        "query": state["query"],
        "data": state["reader_result"]
    })


    return {**state, "report": report}
