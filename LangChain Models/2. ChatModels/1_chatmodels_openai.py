from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(modle = 'gpt-4', temperature=1.5, max_completion_tokens=10)

result = model.invoke("what is the capital of bd.")

print(result)
