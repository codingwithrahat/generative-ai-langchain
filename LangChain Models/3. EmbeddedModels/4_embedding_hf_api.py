from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEndpointEmbeddings(model = 'sentence-transformers/all-MiniLM-L6-v2')

text = "dhaka is the capital of bd"

result = embedding.embed_query(text)

print(result)