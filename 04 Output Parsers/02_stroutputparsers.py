from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

template = PromptTemplate(
    template="write a detailed description about {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="write a 5 line summary about the following {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

#here chain is used to create a pipeline
#parser is used to parse only the output text from the response,
#as like result.content[0]['text'] which is a list of dictionaries and we access the first dictionary and then access the 'text' key to get the generated text.

chain = template | model | parser | template2 | model | parser

#parser pass the text from the previous step to the next step in the chain, so that we can get the final output text from the last step in the chain.

result = chain.invoke({"topic": "icpc"})

print("Result:", result)