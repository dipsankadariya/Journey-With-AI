from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", output_dimensionality=768)

vector = embeddings.embed_query("What is machine learning?")
print(vector)
print(len(vector))