from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("info/result.csv", encoding="utf-8")

docs = loader.load()

print(len(docs))  # prints the number of raws in the CSV file, cause every raw is considered as a document

print(docs[0].page_content)  # prints the content of the first raw in the CSV file
