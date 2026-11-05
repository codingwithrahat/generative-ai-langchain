from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict


load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)   

class response_schema(TypedDict):
    summary: str
    sentiment: str

structured_response = model.with_structured_output(response_schema)

response = structured_response.invoke("""The hardware is great, but the software feels bloated. There are
    too many pre-installed apps that I can't remove. Also, the UI looks
    outdated compared to other brands. Hoping for a software update to fix this.""")


#response is a TypedDict with the keys defined in response_schema
print("Structured response:", response)


#response type
print("Response type:", type(response["summary"]))  # <class 'str'>

print("specific key value:", response["sentiment"])  # "can be anything like negative, positive, neutral etc."


