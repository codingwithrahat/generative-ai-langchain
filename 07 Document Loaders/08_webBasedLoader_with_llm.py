from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader

load_dotenv()

loader = WebBaseLoader("https://codingwithrahat.me/")

docs = loader.load()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Here is the info of this person : {text} \n Give me a short overview of this person",
    input_variables=["text"]
)

chain = prompt | model | parser

result = chain.invoke({"text": docs[0].page_content})

print("Result:", result)