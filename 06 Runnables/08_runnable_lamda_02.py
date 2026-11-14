from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableParallel, RunnableLambda

load_dotenv()

prompt = PromptTemplate(
    template="write 1 interesting facts about {topic}",
    input_variables=["topic"]
)

model= ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

def word_counter(text):
    return len(text.split())

parser = StrOutputParser()

facts_chian1 = RunnableSequence(prompt, model, parser)


parallel_chain = RunnableParallel({
    'facts' : RunnablePassthrough(),
    'word_count' : RunnableLambda(word_counter)
})

final_chain = RunnableSequence(facts_chian1, parallel_chain)

result = final_chain.invoke({"topic": "icpc"})

print("facts:", result['facts'])  # Output: The generated fact about the topic

print("Word Count:", result['word_count'])  # Output: Number of words in the generated fact