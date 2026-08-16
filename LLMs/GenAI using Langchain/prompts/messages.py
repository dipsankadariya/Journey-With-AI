from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model= ChatGoogleGenerativeAI(
    model="gemini-3.6-flash")

#human message->sent by humna
#ai message->sent by ai
#system message->sent to set the context of the conversation

messages=[
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Explain what is a language model?"),
]
result=model.invoke(messages)
messages.append(AIMessage(content=result.content[0]["text"]))
print(messages)

# now we will implement this in chatbot, in a new file chatbot2.py