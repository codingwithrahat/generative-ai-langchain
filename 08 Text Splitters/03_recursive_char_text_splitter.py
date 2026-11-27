from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
    My name is Rahat.
    Iam 23 Years old.

    Who are you?
    how old are you?
""" 

splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print("Number of chunks: ", len(chunks)) # 2 cz 2 paragraphs in the text
print(chunks)


splitter2 = RecursiveCharacterTextSplitter(
    chunk_size=30,
    chunk_overlap=0
)

chunks2 = splitter2.split_text(text)

print(chunks2)
print("Number of chunks: ", len(chunks2)) # 4 cz 4 lines in the text


# default separators are ["\n\n", "\n", " ", ""]
# first try to split by paragraph, if not possible then by line, if not possible then by space, if not possible then by character count.

