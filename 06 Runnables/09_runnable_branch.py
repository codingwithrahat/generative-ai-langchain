from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnablePassthrough, RunnableSequence, RunnableParallel, RunnableLambda

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

prompt = PromptTemplate(
    template="write 1 interesting fact about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Make 1 question about {text}, so that my student can answer it",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = RunnableSequence(prompt, model, parser)

branch_chain = RunnableBranch(

    #here if function returns True, it will run the first chain, otherwise it will run the default chain
    (lambda x: len(x.split()) > 50, RunnableSequence(prompt2, model, parser)),

    #default chain, if the condition is not met
    RunnablePassthrough()
)

final_chain = RunnableSequence(chain, branch_chain)

result = final_chain.invoke({"topic": "icpc"})

print("Result:", result) 
