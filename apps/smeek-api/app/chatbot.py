from langchain.memory import ConversationBufferWindowMemory
from langchain_ollama.llms import OllamaLLM
from langchain.chains import ConversationChain
from langchain.prompts.prompt import PromptTemplate


llm = OllamaLLM(model='llama3', 
             temperature=1)



template = """You are AI assistant, a chatbot designed to help students study. 
Answer in a concise and straightforward way without extra text. Only respond to what is asked and nothing more.
If the AI does not know the answer to a question, it should say, "I don't know." 
Introduce your self as "I am Nova, here to help you with your studies"
Relevant Information:

{history}

Conversation:
Human: {input}
AI:"""
prompt = PromptTemplate(
    input_variables=["history", "input"], template=template
)

window_memory = ConversationBufferWindowMemory(k=2)

conversation = ConversationChain(
    llm=llm, 
    verbose=True, 
    memory=window_memory
)

def ask_anything(inp):
    while True:
        inp = input("here: ")
        ans = conversation.predict(input=inp)
        print(ans)
