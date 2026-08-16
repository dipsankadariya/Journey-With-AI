from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", output_dimensionality=768)
documents=[
    "What is machine learning?",
    "What is deep learning?",
    "What is natural language processing?"  
]

results = embeddings.embed_documents(documents)
print(str(results))