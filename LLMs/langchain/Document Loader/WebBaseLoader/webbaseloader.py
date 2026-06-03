from langchain_community.document_loaders import WebBaseLoader

url="https://en.wikipedia.org/wiki/Artificial_intelligence"
loader = WebBaseLoader(url)
documents = loader.load()
print(type(documents))
print(len(documents))   
print(documents[0].page_content)