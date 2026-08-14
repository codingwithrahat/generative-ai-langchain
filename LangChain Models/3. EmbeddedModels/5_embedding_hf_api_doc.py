from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEndpointEmbeddings(model = 'sentence-transformers/all-MiniLM-L6-v2')

doc = [
    "dhaka is the capital of bd",
    "paris is the capital of france",
    "delhi is the capital of india"
]

result = embedding.embed_documents(doc)
#same for local 

print(str(result))