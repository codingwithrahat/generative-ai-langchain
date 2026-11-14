from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

passthrough = RunnablePassthrough()

result = passthrough.invoke({"text": "Hello, world!"}) # returns {"text": "Hello, world!"}
#it return the same input as output

print("Result:", result) 


