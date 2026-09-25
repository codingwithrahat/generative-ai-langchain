from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

#temperature=0 means the model will be deterministic and always give the same answer for the same prompt.
#tmeperature=1.5 means the model will be more creative and give different answers for the same prompt.
model = ChatOpenAI(modle = 'gpt-4', temperature=0, max_completion_tokens=10)

result = model.invoke("what is the capital of bd.")

print(result.content)
