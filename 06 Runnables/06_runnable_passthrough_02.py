from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableParallel

load_dotenv()

prompt = PromptTemplate(
    template="write 1 interesting facts about {topic}",
    input_variables=["topic"]
)

model= ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Make 1 question about {text}, so that my student can answer it",
    input_variables=["text"]
)

facts_chian1 = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'facts' : RunnablePassthrough(),
    'questions' : RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(facts_chian1, parallel_chain)

result = final_chain.invoke({"topic": "icpc"})

print("Result:", result) 