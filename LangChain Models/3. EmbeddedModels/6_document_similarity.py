from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = HuggingFaceEndpointEmbeddings(model = 'sentence-transformers/all-MiniLM-L6-v2')

doc = [
    'arduino uno is a microcontroller board based on the ATmega328P',
    'stm32 is a family of 32-bit microcontroller integrated circuits by STMicroelectronics',
    'raspberry pi is a series of small single-board computers developed in the United Kingdom',
    'esp32 is a low-cost, low-power system on a chip microcontroller with integrated Wi-Fi and dual-mode Bluetooth'
]

query = 'what is stm32'

doc_embedding = embedding.embed_documents(doc)
query_embedding = embedding.embed_query(query)

# query_embedding need to convert in 2D array to use in cosine_similarity function
cosine_sim = cosine_similarity([query_embedding], doc_embedding)

print("Cosine Similarity 2d list: ", cosine_sim)

#2d first list convert to single list
single_list_convert = cosine_sim[0] 

print("cosine similarity single list: ", single_list_convert)

print("add a index to the list: ", list(enumerate(single_list_convert)))

#now sort the list based on the similarity score in descending order
sorted_list = sorted(list(enumerate(single_list_convert)), key=lambda x: x[1], reverse=True)

print("sorted list: ", sorted_list)

index , score = sorted_list[0]
print("Most similar document index: ", index)
print("Most similar document score: ", score)
print("Most similar document: ", doc[index])