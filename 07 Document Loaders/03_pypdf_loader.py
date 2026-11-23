from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("info/rahat_cv.pdf")

docs = loader.load()

print(len(docs))  #2, beacuse the pdf has 2 pages

print(docs[0].page_content)  #print the content of the first page
print(docs[1].page_content)  #print the content of the second page
print(docs) #print the content of the first page and second page in a list format

# here is give a list of document object
# where every page is a document object with content and metadata
# and list has same length as the number of pages in the pdf



# we use pypdf when the pdf is contain mostly text,
# but it is not better for scanned pdfs and many other things
# some other pdf loader

# for table structure pdf we can use PDFPlumberLoader
# scanned/image based pdf we can use UnstructuredPDFLoader or AmazonTextractPDFLoader
# need layout and image data we can use PyMuPDFLoader
# want best structure extraction we can use UnstructuredPDFLoader