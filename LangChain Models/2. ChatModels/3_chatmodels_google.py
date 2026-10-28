from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.8-flash")

response = model.invoke("who is the president of bangladesh?")

print(response.content[0]["text"])