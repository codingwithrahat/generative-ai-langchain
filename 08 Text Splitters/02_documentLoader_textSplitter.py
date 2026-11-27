from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("info/rahat_cv.pdf")

documents = loader.load()

splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20, separator="")
# 10-20% overlap is recommended for better context retention between chunks.

#sperator can be
# "" - no separator, just split by character count
# " " - split by space, so that words are not cut off
# "/n/n" - split by paragraph, so that paragraphs are not cut off
# "/n" - split by line, so that lines are not cut off



chunks = splitter.split_documents(documents)

# for i in chunks:
#     print(i)

print(chunks[0].page_content)

print("Number of chunks: ", len(chunks))

print(chunks[1].page_content)
