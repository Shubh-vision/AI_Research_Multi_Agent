from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()



llm = ChatGroq(model="llama-3.3-70b-versatile")
parser = StrOutputParser()