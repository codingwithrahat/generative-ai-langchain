from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model =  ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)   

parser = JsonOutputParser()


#here we are using the parser.get_format_instructions() to get the format instructions for the output parser.
#partial variables cause it not set in runtime

template = PromptTemplate(
    template="give me the name, age and city of a frictional person {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction" : parser.get_format_instructions()}

)

# prompt = template.invoke({})

prompt = template.format() 

# both template.invoke({}) and template.format() will give the same output
# but template.format() is used to get the final propmt in string format

print("Prompt:", prompt)


result = model.invoke(prompt)

print("Result:", result.content[0]['text']) #raw llm outpur in json format
print("Result using text attribute:", result.text) #both result.text and result.content[0]['text'] will give the same output

final_result = parser.parse(result.content[0]['text']) #convert the text output to a dictionary using the parse method of the JsonOutputParser

print("Final Result:", final_result) #dictonary formate