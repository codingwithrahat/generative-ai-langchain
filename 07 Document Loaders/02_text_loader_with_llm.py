from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

loader = TextLoader("icpc.txt", encoding="utf-8")

documents = loader.load()

prompt = PromptTemplate(
    template="Give me 5 question from this {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"text": documents[0].page_content})

print("Result:", result)




