from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model =  ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)   

parser = JsonOutputParser()


template = PromptTemplate(
    template="give me the name, age and city of a frictional person {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction" : parser.get_format_instructions()}

)

#here we are using the chain to create a pipeline of the prompt template, model and the output parser.
#first template will generate the prompt, then the model will generate the output and then the output parser will parse the output to a dictionary format.

chain = template | model | parser

result = chain.invoke({})

print("Final Result:", result) 