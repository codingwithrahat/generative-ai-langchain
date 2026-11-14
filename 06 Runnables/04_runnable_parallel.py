from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

prompt = PromptTemplate(
    template="generate a tweet about {topic}",
    input_variables=["topic"]      
)

prompt2 = PromptTemplate(
    template="generate a linkedin post about {topic}",
    input_variables=["topic"]
)

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

parser = StrOutputParser()

chain = RunnableParallel({
    'tweet' : RunnableSequence(prompt, model, parser),
    'linkedin' : RunnableSequence(prompt2, model, parser)
})

# both the chain will get the same topic icpc
# and will run in parallel and return the result as a list of two strings

result = chain.invoke({"topic": "icpc"})

print("Result:", result) #we get a dictionary with two keys tweet and linkedin and their respective values are the generated tweet and linkedin post


print("Tweet:", result['tweet']) #we get the tweet output


