from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field 

load_dotenv()

model =  ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)   

#base model for the output parser
class person(BaseModel):
    name: str = Field(description="name of the person")
    age: int = Field(gt=18,description="age of the person")
    city: str = Field(description="city of the person")

parser = PydanticOutputParser(pydantic_object=person)

template = PromptTemplate(
    template="give me data of a frcitional person {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction" : parser.get_format_instructions()}

)

# prompt = template.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.text)

chain = template | model | parser

final_result = chain.invoke({})

print(final_result)

