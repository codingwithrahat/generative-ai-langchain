
#load function use eager loading, which means it loads all the documents at once. 
#To avoid this, we can use lazy loading, loads on demand, gives a generator object

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

# docs = pdf_loader.lazy_load() + txt_loader.lazy_load()
#genrator object can't be added like a normal list


docs = pdf_loader.lazy_load()  # returns a generator object

for doc in docs:
    print('-------------------')
    print(doc.page_content) 

# generator object is returned, we can iterate over it to get the documents one by one



