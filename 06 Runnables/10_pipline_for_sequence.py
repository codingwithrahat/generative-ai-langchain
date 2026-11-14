from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template="write 5 interesting facts about {topic}",
    input_variables=["topic"]
)

model= ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Give 5 questions about {text}",
    input_variables=["text"]
)

chain = prompt | model | parser | prompt2 | model | parser
# no need to use RunnableSequence, we can use the pipe operator to create a sequence of runnables

result = chain.invoke({"topic": "icpc"})

print("Result:", result) #we get string output
