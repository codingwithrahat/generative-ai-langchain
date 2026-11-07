from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Literal, Annotated, Optional
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)   

# schema
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}

structured_response = model.with_structured_output(json_schema)

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

    Review by Mohammad Rahat Hossan
    """
)


print("Structured response:", response) 


