from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = 'info',
    glob="*.pdf",   #all documents with .pdf extension will be loaded
    loader_cls = PyPDFLoader
)

docs = loader.load()

print(len(docs))  # 3, because the directory has 2 pdf file with total (2 + 1 )3 pages

print(docs)  # print the whole list of document object with content and metadata