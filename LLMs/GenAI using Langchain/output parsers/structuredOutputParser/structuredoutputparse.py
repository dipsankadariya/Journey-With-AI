from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model=ChatGroq(model="llama-3.1-8b-instant")

schema=[
    ResponseSchema(name="fact1", description="first fact about the topic"),
    ResponseSchema(name="fact2", description="second fact about the topic"),
    ResponseSchema(name="fact3", description="third fact about the topic"),
]

parser=StructuredOutputParser.from_response_schemas(schema)

template= PromptTemplate(
    template="Give three facts about the following topic: {topic}\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain= template | model | parser
result=chain.invoke({"topic": "causal masking in transformers"})
print(result)
