from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

model2 = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite"
)

prompt1 = PromptTemplate(
    template="generate a sort notes from the following text: {text}",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template="generate 5 sort questions from the following text: {text}",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="merge the provided notes and questions into a single document: {notes} and {questions}",
    input_variables=["notes", "questions"]
)

parser = StrOutputParser()


#parallel chain
parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'questions': prompt2 | model2 | parser
})

# merge_chain = prompt3 | model1 | parser

# chain = parallel_chain | merge_chain

chain = parallel_chain | prompt3 | model1 | parser

result = chain.invoke({"text": """
The International Collegiate Programming Contest (ICPC) is a multi-tier,
team-based competition among universities from around the world.
It is considered one of the most prestigious programming competitions in the world.
The contest is sponsored by IBM and has been held annually since 1970.
Teams of three students work together to solve complex algorithmic problems within a set time limit.
The competition emphasizes teamwork, problem-solving skills, and efficient coding practices.
ICPC has a rich history of producing top-tier programmers who go on to have successful careers in the tech industry.
"""})

print(result)

chain.get_graph().print_ascii()