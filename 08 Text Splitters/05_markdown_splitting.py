from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
# web-and-internet-programming
My university learning repository for Web and Internet Programming, containing practice codes, coursework, and projects using HTML, CSS, JavaScript, PHP, and related web technologies.

Learning Resources : [ThreaTLess Web 01](https://threatless.io/web101)
"""


splitters = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=100,
    chunk_overlap=0
)

chunks = splitters.split_text(text)

print("number of chunks: ", len(chunks))

for i in chunks:
    print("-------------------")
    print(i)

