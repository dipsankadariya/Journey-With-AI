from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model= ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

chat_history=[]

while True:
   user_input=input("you:")
   chat_history.append(user_input)
   if user_input =="exit":
      break
   result=model.invoke(chat_history)
   chat_history.append(result.content[0]["text"])
   print("bot:",result.content[0]["text"])

print(chat_history)