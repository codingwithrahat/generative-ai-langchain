from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser  

load_dotenv()

prompt = PromptTemplate(
    template="write 5 interesting facts about {topic}",
    input_variables=["topic"]
)

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)   

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic": "icpc"})

print("Result:", result) #we get string output



#visualizing the chain

chain.get_graph().print_ascii()

