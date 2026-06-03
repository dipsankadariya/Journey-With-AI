from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

model=ChatOpenAI()

prompt=PromptTemplate(
    template="Answer the following questions \n {question} from the following text- \n{text}",
    input_variables=["question","text"]
)

parser=StrOutputParser()

url="https://en.wikipedia.org/wiki/Artificial_intelligence"

loader = WebBaseLoader(url)
documents = loader.load()
chain=prompt | model | parser

question="What is Artificial Intelligence?"
output=chain.invoke({"question": question, "text": documents[0].page_content})
print(output)