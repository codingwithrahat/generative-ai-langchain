from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader

pdf_loader = DirectoryLoader(
    path = 'info',
    glob="*.pdf",   #all documents with .pdf extension will be loaded
    loader_cls = PyPDFLoader
)

txt_loader = DirectoryLoader(
    path = 'info',
    glob="*.txt",   #all documents with .txt extension will be loaded
    loader_cls = TextLoader
)

docs = pdf_loader.load() + txt_loader.load()

# print(docs)  

print(len(docs))  # 7 (pdf1 - 4 pages, pdf2 - 2 page, txt - 1 page)


for doc in docs:
    print('-------------------')
    print(doc.page_content)  # print the content of each document

