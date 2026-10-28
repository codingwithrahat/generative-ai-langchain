from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)  

messages = [
    SystemMessage(content="You are a helpful programming tutor."),
    HumanMessage(content="What is a pointer in C++?"),
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content[0]['text']))

print(messages)