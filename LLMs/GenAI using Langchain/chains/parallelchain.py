from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
load_dotenv()

model1=ChatGroq(model="llama-3.1-8b-instant")
model2= ChatGoogleGenerativeAI(model="gemini-3.6-flash")

prompt1=PromptTemplate(
    template="Generate short notes from the following {text}.",
    input_variables=["text"]
)

prompt2=PromptTemplate(
    template="Generate 3 quizes from the following {text}.",
    input_variables=["text"]
)

final_prompt=PromptTemplate(
    template="Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}.",
    input_variables=["notes","quiz"]
)

parser=StrOutputParser()

#parallel chain

parallel_chain=RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain= final_prompt | model1 | parser

final_chain=parallel_chain | merge_chain

text="""
# LangChain Notes

LangChain is a framework used to build applications powered by Large Language Models (LLMs). It provides tools and components for working with models, prompts, output parsers, documents, embeddings, retrievers, and external tools. Instead of directly sending a prompt to an LLM, LangChain allows developers to connect multiple components together to create complete AI applications.

A basic LangChain workflow can be thought of as Prompt → Model → Output Parser → Response. Prompt templates allow reusable prompts with variables, while output parsers convert model responses into useful formats such as strings, JSON, or structured objects. LangChain also supports RAG, where documents are loaded, split into chunks, converted into embeddings, stored in a vector database, and retrieved when a user asks a question.

LangChain can also be used to build AI agents that interact with external tools such as calculators, search engines, APIs, and databases. Its main advantage is that different components can be combined into flexible workflows. Important concepts to learn are models, prompts, chains, LCEL, runnables, output parsers, embeddings, vector stores, retrievers, RAG, tools, and agents.

One important feature of LangChain is **LCEL (LangChain Expression Language)**, which allows components to be connected using a simple pipe syntax. For example, `prompt | model | parser` connects a prompt, language model, and output parser into one workflow. LangChain also provides **Runnable** components, which can be executed using operations such as `invoke`, `batch`, and `stream`.

LangChain is especially useful for building **RAG applications**. In a RAG system, documents are first loaded and divided into smaller chunks. These chunks are converted into embeddings and stored in a vector store. When a user asks a question, a retriever searches for relevant chunks and provides them to the LLM as context. This allows the model to answer questions using information from external documents.

Another important concept is **structured output**. Instead of receiving free-form text from an LLM, developers can define a specific structure for the response. For example, a model can be asked to return a person's name, age, and address in a predefined format. Pydantic and JSON-based approaches are commonly used for handling structured data.

LangChain also supports **tool calling and agents**. Tools are external functions that an LLM can use, such as calculators, search engines, APIs, or database queries. An agent can decide which tool it needs and when to use it. This makes it possible to build AI systems that can perform multiple actions instead of only generating text.

The main goal of learning LangChain is not to memorize every class or function, but to understand how the components work together. A good learning path is to first understand models and prompts, then output parsers and LCEL, followed by RAG, embeddings, vector stores, retrievers, structured output, tools, and finally agents.

"""
result=final_chain.invoke({"text":text})
print(result)