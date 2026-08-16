from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
text="Machine learning is a field of computer science that focuses on the development of algorithms and models that enable computers to learn from and make predictions or decisions based on data. It involves training models on large datasets to recognize patterns, make predictions, and improve performance over time without being explicitly programmed for specific tasks."
vector = embeddings.embed_query(text)
print(str(vector))