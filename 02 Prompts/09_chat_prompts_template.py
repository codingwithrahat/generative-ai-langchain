from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful {subject} tutor."),
    ( 'human', "Student Question: {question}"),
])

prompt = chat_template.invoke({
    'subject': 'programming',
    'question': 'What is a pointer in C++?'
})

print(prompt)