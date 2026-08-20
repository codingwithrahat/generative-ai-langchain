from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ["HF_HOME"] = "E:/huggingface_cache"

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 100,
        "do_sample": True,
    }
)

model = ChatHuggingFace(llm=llm)

while True:
    s = input("Enter your message (type 'exit' to quit): ")

    if s == "exit":
            break

    result = model.invoke(s)

    print(result.content)

    
    #but there is no memory, so it can't remember previous converasations
