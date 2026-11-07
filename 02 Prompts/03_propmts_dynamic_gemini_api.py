from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt


load_dotenv()


# Model selection
model_name = st.selectbox(
    "Select Model",
    [
        "gemini-3.5-flash-lite",
        "gemini-3.8-flash",
        "gemini-3.1-flash-lite"
    ]
)


# Create selected model
model = ChatGoogleGenerativeAI(
    model=model_name
)


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

template = load_prompt('programming_tutor_prompt_template.json')


if st.button("Ask AI"):

    #this is the new way to create a chain with the prompt template and the model. The chain will handle the prompt generation and model invocation.

    #here | is not bitwise or, it is a new operator introduced in langchain to create a chain with the prompt template and the model. The chain will handle the prompt generation and model invocation.

    chain = template | model

    result = chain.invoke({
        'subject':subject,
        'difficulty':difficulty,
        'response_type':response_type,
        'question':question
    })

    # st.write(result.content)

    st.write(result.content[0]["text"])

