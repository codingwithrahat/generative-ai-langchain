from langchain_huggingface import HuggingFaceEmbeddings
import os

os.environ["HF_HOME"] = "/home/rahat/local_models/huggingface_cache"

embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

text = "dhaka is the capital of bd"

result = embedding.embed_query(text)

print(result)