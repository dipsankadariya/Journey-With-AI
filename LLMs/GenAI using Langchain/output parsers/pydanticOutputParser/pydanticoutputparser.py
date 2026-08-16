
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

load_dotenv()

model=ChatGroq(
    model="llama-3.1-8b-instant",
)

class Person(BaseModel):
    name:str=Field(description="name of the person")
    age:int=Field(gt=18,description="age of the person")
    city:str=Field(description="city of the person")

parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template="Give me the name ,age and address of a fictional  {place} person \n : {format_instructions}",
    input_variables=["place"],
    partial_variables={"format_instructions":parser.get_format_instructions()}
)

chain= template | model | parser
result=chain.invoke({"place": "New York"})
print(result)