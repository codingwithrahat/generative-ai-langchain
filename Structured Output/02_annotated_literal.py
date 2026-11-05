from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Literal


load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)   

class response_schema(TypedDict):

    #here annotated is used to provide a description for the summary key in the TypedDict
    #so that model can generate a more accurate summary based on the description provided
    summary: Annotated[str, "A brief summary of the review)"]
    sentiment: Annotated[Literal["positive", "negative"], "The sentiment of the review"]  # sentiment can only be one of these three values

structured_response = model.with_structured_output(response_schema)

response = structured_response.invoke("""The hardware is great, but the software feels bloated. There are
    too many pre-installed apps that I can't remove. Also, the UI looks
    outdated compared to other brands. Hoping for a software update to fix this.""")


#response is a TypedDict with the keys defined in response_schema
print("Structured response:", response)


print("specific key value:", response["sentiment"])  # "negative or positive"


