from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableBranch, RunnableLambda

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)   

parser = StrOutputParser()

class FeedBack(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="The sentiment of the feedback text, either positive or negative."
    )

pydantic_parser = PydanticOutputParser(pydantic_object=FeedBack)

prompt1 = PromptTemplate(
    template="classify the sentiment of the following feedback text into postive or negative: {feedback} \n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": pydantic_parser.get_format_instructions()}
)

chain = prompt1 | model | pydantic_parser

# print(chain.invoke({"feedback": "I hate this product!"}).sentiment)  

prompt2 = PromptTemplate(
    template = "write a appropiate response to this postive feedback: {feedback} \n do not provide multiple options, just provide a single response",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template = "write a appropiate response to this negative feedback: {feedback} \n do not provide multiple options, just provide a single response",
    input_variables=["feedback"]
)   


branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "negative", prompt3 | model | parser),

    RunnableLambda(lambda x: "could not classify the feedback sentiment") 
)

final_chain = chain | branch_chain

print(final_chain.invoke({"feedback": "I hate this product!"})) 

final_chain.get_graph().print_ascii()