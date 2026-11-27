from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

text_splitter = SemanticChunker(
    embeddings=GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
    ),
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1,
)


# Standard Deviation (SD) tells us how spread out the values are from the average (mean).
# threshole ammount = 1 means that we will consider a breakpoint if it is more than 1 standard deviation away from the mean.

text = """
Python is a popular programming language. Developers use Python to build websites, APIs, and automation tools. FastAPI is a framework used for building backend APIs. Football is a popular sport worldwide. Millions of people watch football matches and support their favorite teams. The FIFA World Cup is the biggest international football tournament.

Artificial Intelligence is changing technology. Machine learning helps computers learn from data. Generative AI can generate text, images, and code.
"""

docs = text_splitter.split_text(text)

print("Number of chunks: ", len(docs))

for i in docs:
    print("-------------------")
    print(i)


