from langchain_core.runnables import RunnableLambda


def word_counter(text):
    return len(text.split())

runnable_word_counter = RunnableLambda(word_counter)

print(runnable_word_counter.invoke({"text": "Hello, world! This is a test."}))  # Output: 7

