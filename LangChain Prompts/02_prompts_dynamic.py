from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

import streamlit as st
from langchain_core.prompts import PromptTemplate


load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


st.header("Programming Tutor ChatBot")


#this is just for ui
subject = st.selectbox(
    "Select Subject",
    [
        "C++",
        "Python",
        "Java",
        "Database",
        "Operating System",
        "Computer Networks"
    ]
)

difficulty = st.selectbox(
    "Select Difficulty",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

response_type = st.selectbox(
    "Response Type",
    [
        "Explain",
        "Give Example",
        "Give Hint",
        "Step-by-Step Solution",
        "Short Answer"
    ]
)


question = st.text_input(
    "Your Question",
    placeholder="e.g. What is a pointer in C++?"
)


template = PromptTemplate(
    template="""
    You are a helpful programming tutor.

    Subject: {subject}
    Difficulty: {difficulty}
    Response Type: {response_type}

    Student Question: {question}

    Response type rules:

    - Explain:
      Explain the concept clearly with simple intuition.

    - Give Example:
      Explain the concept and provide a simple example.

    - Give Hint:
      Give only hints and guidance.
      Do not provide the complete solution.

    - Step-by-Step Solution:
      Explain the solution step by step.

    - Short Answer:
      Give a concise and direct answer.
      Avoid unnecessary explanation.
    """,

    input_variables=[
        "subject",
        "difficulty",
        "response_type",
        "question"
    ]
)

#here we fill the template with the user inputs and generate the final prompt to send to the model.
prompt = template.invoke({
    'subject':subject,
    'difficulty':difficulty,
    'response_type':response_type,
    'question':question
})

if st.button("Ask AI"):

        result = model.invoke(prompt)

        st.write(result.content)

