from state.state import AgentState
from langchain_core.prompts import ChatPromptTemplate
from llm.llm import llm, parser
from agents.reader_agent import reader_node


writer_prompt = ChatPromptTemplate.from_template("""
Write a research report.

Topic: {query}

Content:
{content}

Include:
- Introduction
- Key Findings
- Conclusion
- Sources
""")

def writer_node(state: AgentState):
    print("\n✍️ Writing...")

    chain = writer_prompt | llm | parser

    report = chain.invoke({
        "query": state["query"],
        "content": state["content"]
    })

    return {**state, "report": report}
