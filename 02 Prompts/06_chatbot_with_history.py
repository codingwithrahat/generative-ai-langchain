from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

chat_history = []

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    
    chat_history.append(user_input)

    result = model.invoke(chat_history)

    chat_history.append(result.content[0]['text'])

    print("AI: ", result.content[0]['text'])


print("\nChat history:", chat_history)