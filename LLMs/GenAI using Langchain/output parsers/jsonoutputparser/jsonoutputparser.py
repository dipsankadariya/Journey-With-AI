
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model=ChatGroq(
    model="llama-3.1-8b-instant",
)

parser=JsonOutputParser()

template=PromptTemplate(
    template="Give me the name ,age and address of a fictional person \n : {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

prompt=template.format()
result=model.invoke(prompt)
final_result=parser.parse(result.content)
print(final_result)
print(type(final_result))
print(final_result["name"])