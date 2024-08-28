from langchain.memory import ConversationBufferWindowMemory
from langchain_ollama.llms import OllamaLLM
from langchain.chains import ConversationChain
from langchain.prompts.prompt import PromptTemplate
from pydantic import BaseModel

# Chatbot setup
llm = OllamaLLM(model='llama3', temperature=1)

template = """You are AI assistant, a chatbot designed to help students study. 
Answer in a concise and straightforward way without extra text. Only respond to what is asked and nothing more.
If the AI does not know the answer to a question, it should say, "I don't know." 
Introduce yourself as "I am Nova, here to help you with your studies"
Relevant Information:

{history}

Conversation:
Human: {input}
AI:"""

prompt = PromptTemplate(input_variables=["history", "input"], template=template)

# Initialize conversation state
conversation_active = True

def create_conversation_chain():
    return ConversationChain(llm=llm, verbose=True, memory=ConversationBufferWindowMemory(k=2))

# Define the ConversationChain
conversation_chain = create_conversation_chain()

# Request and response model
class ChatInput(BaseModel):
    user_input: str

def get_chatbot_response(user_input: str) -> str:
    global conversation_active
    global conversation_chain

    # Check if the conversation should be ended
    if user_input.lower().strip() == "bye":
        conversation_active = False
        return "Goodbye! Have a great day!"

    # Start a new conversation if previous one ended
    if not conversation_active:
        conversation_active = True
        conversation_chain = create_conversation_chain()

    # Generate a response using the conversation chain
    return conversation_chain.predict(input=user_input)
