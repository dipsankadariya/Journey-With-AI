from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

documents = [
    "Machine learning is a field of computer science that focuses on the development of algorithms and models that enable computers to learn from and make predictions or decisions based on data. It involves training models on large datasets to recognize patterns, make predictions, and improve performance over time without being explicitly programmed for specific tasks.",
    "Deep learning is a subset of machine learning that uses neural networks with multiple layers to model and solve complex problems. It has shown remarkable success in areas such as image recognition, natural language processing, and speech recognition.",
    "Natural language processing is a subfield of artificial intelligence that focuses on the interaction between computers and human language. It involves developing algorithms and models that enable computers to understand, interpret, and generate human language in a valuable way.",
    "Computer vision is a field of artificial intelligence that enables computers to understand and interpret visual information from images and videos. It is used in applications such as object detection, facial recognition, medical imaging, and autonomous vehicles.",
    "Reinforcement learning is a type of machine learning in which an agent learns to make decisions by interacting with an environment. The agent receives rewards or penalties based on its actions and uses this feedback to learn strategies that maximize its long-term reward."
]

question="tell me about machine learning"
document_embeddings = embeddings.embed_documents(documents, output_dimensionality=768)
question_embedding = embeddings.embed_query(question, output_dimensionality=768)
similarity_scores = cosine_similarity([question_embedding], document_embeddings)[0]
print("Similarity Scores:", similarity_scores)
index, score = (sorted(list(enumerate(similarity_scores)),key=lambda x: x[1])[-1])
print(question)
print(documents[index])
print("Best Match Score:", score)