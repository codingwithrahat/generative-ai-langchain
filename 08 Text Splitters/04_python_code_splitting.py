from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """


class stu:

    def __init__(self, name):
        self.name = name
    
    def wel(self):
        print("Hello", self.name)

    def ask(self):              #use self, otherwise 
        print("Any Question?")  #it is treated as a function not class method
        


s1 = stu("Rahat")

s1.wel()
s1.ask()


"""


splitters = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=280,
    chunk_overlap=0
)

chunks = splitters.split_text(text)

print("number of chunks: ", len(chunks))

for i in chunks:
    print("-------------------")
    print(i)

