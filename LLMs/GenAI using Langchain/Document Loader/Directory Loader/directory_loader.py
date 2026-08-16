from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
import os

loader = DirectoryLoader(
    path=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'files', 'books')),
    glob='*.pdf',
    loader_cls=PyPDFLoader
)
documents = loader.load()
# we can use loader.lazy_load() instead of loader.load() if we want to load many documents and we don't want to load all the documents at once. It will return a generator which will load the documents one by one when we iterate over it.
# print(len(documents))
print(documents[0].page_content)
print(documents[0].metadata)
print(documents[411].page_content)
print(documents[411].metadata)
