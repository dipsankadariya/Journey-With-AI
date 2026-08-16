from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.6-flash",temperature=0.3)
result = model.invoke("when is casual masking applied in the transformer architecture?")
print(result.content[0]["text"])