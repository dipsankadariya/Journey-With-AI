# showing the connected workflow of document loader last time we learned and text splitter 

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

pdf_path = os.path.abspath(
	os.path.join(os.path.dirname(__file__), "..", "..", "Document Loader", "files", "docs", "book.pdf")
)
loader = PyPDFLoader(pdf_path)
docs = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0,separator='')

results = text_splitter.split_documents(docs)

print(results[0])
print(results[0].page_content)
print(results[1])
print(results[1].page_content)

