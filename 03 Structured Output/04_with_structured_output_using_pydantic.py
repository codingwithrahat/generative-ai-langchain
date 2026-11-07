from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Literal, Annotated, Optional
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)   

class response_schema(BaseModel):

    key_themes: list[str] = Field(description="A list of key themes or topics discussed in the review")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg", "neg"] = Field(description="The sentiment of the review, can be anything like negative, positive, neutral etc.")
    pros: Optional[list[str]] = Field(default=None, description="A list of pros mentioned in the review")
    cons: Optional[list[str]] = Field(default=None, description="A list of cons mentioned in the review")

structured_response = model.with_structured_output(response_schema)

response = structured_response.invoke(
    """I recently bought the ASUS Vivobook 15 for my daily programming and university work, and overall, I am quite satisfied with it.

    The Intel Core i5 processor handles my coding tasks, multitasking, and browsing smoothly. I can run VS Code, a browser with multiple tabs, and other applications without noticeable lag. The 512GB SSD also makes booting and opening applications very fast.

    However, the 8GB RAM feels limiting when I run heavier applications or multiple development tools simultaneously. I wish ASUS had provided 16GB RAM by default. The display is decent for everyday use, but the color accuracy could be better. The keyboard is comfortable for long coding sessions, which is a big plus for me.

    Battery life is acceptable for regular university use, but it could be improved. The build quality is good considering the price, and the laptop is lightweight enough to carry around.

    Pros:
    Good performance for programming and everyday tasks
    Fast 512GB SSD
    Comfortable keyboard
    Lightweight and portable design

    Cons:
    8GB RAM is limiting for heavy multitasking
    Average display color accuracy
    Battery life could be better

    Review by a Computer Science Student
    """
)


print("Structured response:", response.model_dump()) #convert the pydantic model to a dictionary using model_dump() method 


