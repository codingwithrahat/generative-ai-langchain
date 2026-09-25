from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import streamlit as st

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

st.header("My ChatBot")

user_input = st.text_input("Enter Your Prompt Here")

if st.button("Submit"):
    result = model.invoke(user_input)
    st.write(result.content)    