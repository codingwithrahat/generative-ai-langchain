from langchain_text_splitters import CharacterTextSplitter

text = """
    Here is a sample text that we will use to demonstrate the CharacterTextSplitter. The CharacterTextSplitter is a utility that allows us to split a given text into smaller chunks based on a specified length. This can be particularly useful when dealing with large texts that need to be processed in smaller segments for tasks such as natural language processing, machine learning, or data analysis.
"""

splitter = CharacterTextSplitter(chunk_size=50, chunk_overlap=0, separator="")

chunks = splitter.split_text(text)

print(chunks)

print("Number of chunks: ", len(chunks))

# it wiil return an list of text chunks, each with a maximum length of 50 characters and an overlap of 10 characters between consecutive chunks. 