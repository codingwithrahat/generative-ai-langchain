from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

template = PromptTemplate(
    template="write a detailed description about {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="write a 5 line summary about the following {text}",
    input_variables=["text"]
)

prompt = template.invoke({"topic": "icpc"})

result = model.invoke(prompt)

prompt2 = template2.invoke({"text": result.content[0]['text']})

result2 = model.invoke(prompt2)

#here we use result2.content[0]['text'] to get the text from the response object which is a list of dictionaries and we access the first dictionary and then access the 'text' key to get the generated text.
print("Result:", result2.content[0]['text'])
