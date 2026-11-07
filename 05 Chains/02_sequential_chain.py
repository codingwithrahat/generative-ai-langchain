from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)   

prompt1 = PromptTemplate(
    template="generate a detailed report on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="write a 5 point of the following report: {report}",
    input_variables=["report"]

)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "icpc"})

print("Result:", result) 

chain.get_graph().print_ascii()

