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
    template="give me 5 fact about icpc {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction" : parser.get_format_instructions()}

)

# Here we don't define a specific JSON schema.
# The LLM generates a JSON structure based on the prompt.


chain = template | model | parser

result = chain.invoke({})

print("Final Result:", result) 