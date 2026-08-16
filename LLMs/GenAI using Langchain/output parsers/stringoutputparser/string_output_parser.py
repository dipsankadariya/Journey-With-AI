#without using string output parser

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()


model = ChatGroq(
    model="llama-3.1-8b-instant",
)

#first prompt->detal report
template1=PromptTemplate(
    template="Write a detailed report on the following topic: {topic}",
    input_variables=["topic"]
)


#2nd prompt->summary report
template2=PromptTemplate(
    template="Write a 5 line summary report on the following topic: {text}",
    input_variables=["text"]
)

#first send template1
prompt1=template1.invoke({"topic":"Artificial Intelligence"})
result=model.invoke(prompt1)


prompt2=template2.invoke({"text":result.content})
result=model.invoke(prompt2)
print(result.content)
