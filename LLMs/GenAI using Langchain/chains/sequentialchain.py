from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 
load_dotenv()


model=ChatGroq(model="llama-3.1-8b-instant")

prompt1=PromptTemplate(
    template="Generate a 8 line report about {topic}.",
    input_variables=["topic"]
)
prompt2=PromptTemplate(
    template="Generate 3 line summary of {text}.",
    input_variables=["text"])

parser=StrOutputParser()

chain=prompt1 | model | parser| prompt2 | model | parser
result=chain.invoke({"topic":"astronomy"})
print(result)