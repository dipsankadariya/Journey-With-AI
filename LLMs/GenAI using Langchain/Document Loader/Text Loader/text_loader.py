import os

from langchain_community.document_loaders import TextLoader

movies_path = os.path.abspath(
	os.path.join(os.path.dirname(__file__), "..", "files", "docs", "movies.txt")
)

#create  loder object which is a document loader object
loader=TextLoader(movies_path,encoding='utf-8')
#now there is a function called load which will load the document and return a list of documents
documents=loader.load()
#any loader that lanchain provides will return documents in the form of list.
print(type(documents)) 
print(len(documents))

print(documents[0].page_content) #it will return the content of the document which is the text in our file.
print(documents[0].metadata) #it will return the metadata of the document which is a dictionary containing the source of the document which is the file name in this case.