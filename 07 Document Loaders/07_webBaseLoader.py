#it better for static web pages

from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://codingwithrahat.me/")

docs = loader.load()

print(len(docs))  # prints the number of documents loaded

print(docs[0].page_content)  # prints the content of the web page

# it take all the text form the html page



# we can pass a list of urls to the WebBaseLoader to load multiple web pages at once