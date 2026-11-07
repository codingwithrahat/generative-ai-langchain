from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model =  ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)   

#schema
schema = [
    ResponseSchema(name="fact_1", description="fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="fact 3 about the topic")
]


parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="give me 3 fact about {topic} {format_instruction}",
    input_variables=['topic'],
    partial_variables={"format_instruction" : parser.get_format_instructions()}

)

chain = template | model | parser

# prompt = template.invoke({'topic': 'ICPC'})

# result = model.invoke(prompt)

# final_result = parser.parse(result.text)

final_result = chain.invoke({'topic': 'ICPC'})

print(final_result)



#a issue is that we can't data type validation in the structured output parser. For example if we want to get a number as output but the model gives a string then it will not raise any error. It will just give the string as output.