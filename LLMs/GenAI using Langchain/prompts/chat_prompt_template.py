from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv


load_dotenv()

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} expert."),
    ("human", "Explain in simple terms, what is {topic}?")
])

prompt= chat_template.invoke({"domain": "AI", "topic": "language model"})
print(prompt)