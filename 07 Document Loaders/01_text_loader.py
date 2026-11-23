from langchain_community.document_loaders import TextLoader

loader = TextLoader("info/icpc.txt", encoding="utf-8")
#encoding is not mandartory
#but it is important to read accurate if document has special characters like non-english characters, emojis, etc.


documents = loader.load()

# document object has 2 part, one is content and other is metadata.

print(type(documents))  # type is list

print(type(documents[0]))  # type is langchain document object

print(type(documents[0].page_content))  # type str



print(documents[0])  # print the first document (content and metadata)

print(documents[0].page_content)  # print the content of the first document
