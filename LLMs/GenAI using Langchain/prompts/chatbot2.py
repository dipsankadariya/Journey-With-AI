from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
load_dotenv()

model= ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

chat_history=[
    SystemMessage(content="You are a helpful assistant.")
]

while True:
   user_input=input("you:")
   chat_history.append(HumanMessage(content=user_input))
   if user_input =="exit":
      break
   result=model.invoke(chat_history)
   chat_history.append(AIMessage(content=result.content[0]["text"]))
   print("bot:",result.content[0]["text"])

print(chat_history)