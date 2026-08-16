#use of stroutputparser

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatGroq(
    model="llama-3.1-8b-instant",
)

prompt1=PromptTemplate(
    template="Write a detailed report on the following topic: {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="Write a 5 line summary report on the following topic: {text}",
    input_variables=["text"]
)

parser=StrOutputParser()

chain= prompt1 | model | parser | prompt2 | model | parser

result=chain.invoke({"topic":"Artificial Intelligence"})
print(result)