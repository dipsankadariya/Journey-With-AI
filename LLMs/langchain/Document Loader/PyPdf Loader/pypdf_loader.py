import os

from langchain_community.document_loaders import PyPDFLoader

pdf_path = os.path.abspath(
	os.path.join(os.path.dirname(__file__), "..", "files", "docs", "book.pdf")
)
loader = PyPDFLoader(pdf_path)
docs = loader.load()
print(docs)
print(docs[0].page_content)
print(docs[0].metadata)
