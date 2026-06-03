from langchain_community.document_loaders import CSVLoader
import os

#csv loader loads every row in the csv file as a single document, so a csv file having 400 rows will have 400 documents in the form of list.
csv_path = os.path.abspath(
	os.path.join(os.path.dirname(__file__), "..", "files", "docs", "Social_Network_Ads.csv")
)
loader=CSVLoader(csv_path,encoding='utf-8')
documents=loader.load()
print(type(documents))
print(len(documents))
print(documents[0])
