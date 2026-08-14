from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

doc = [
    "dhaka is the capital of bd",
    "paris is the capital of france",
    "delhi is the capital of india"
]

result = embedding.embed_documents(doc)

print(str(result))


