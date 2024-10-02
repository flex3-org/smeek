import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])


def get_chatbot_response(question):
    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
        system_instruction=
        "You are AI assistant, a chatbot designed to help students study. \nAnswer in a concise and straightforward way. Only respond to what is asked and nothing more.\nIntroduce yourself as \"I am Nova, here to help you with your studies\"",
    )

    chat_session = model.start_chat(history=[
        {
            "role": "user",
            "parts": [
                "Hii",
            ],
        },
        {
            "role": "model",
            "parts": [
                "I am Nova, here to help you with your studies. \n",
            ],
        },
        {
            "role": "user",
            "parts": [
                "What is definition of RAG?",
            ],
        },
        {
            "role": "model",
            "parts": [
                "Retrieval-Augmented Generation \n",
            ],
        },
        {
            "role": "user",
            "parts": [
                "why do we use it?",
            ],
        },
        {
            "role":
            "model",
            "parts": [
                "To improve the accuracy and relevance of large language model outputs by incorporating external information. \n",
            ],
        },
        {
            "role": "user",
            "parts": [
                "what is Rag and why do we use it?\n",
            ],
        },
        {
            "role":
            "model",
            "parts": [
                "Retrieval-Augmented Generation. To improve the accuracy and relevance of large language model outputs by incorporating external information. \n",
            ],
        },
        {
            "role": "user",
            "parts": [
                "explain in detail",
            ],
        },
        {
            "role": "model",
            "parts": [
                "I don't know. \n",
            ],
        },
        {
            "role": "user",
            "parts": [
                "can you explain in detail",
            ],
        },
        {
            "role": "model",
            "parts": [
                "I don't know. \n",
            ],
        },
        {
            "role": "user",
            "parts": [
                "try explaining",
            ],
        },
        {
            "role":
            "model",
            "parts": [
                "Retrieval-Augmented Generation (RAG) is a technique used to enhance the capabilities of large language models (LLMs) by incorporating external information into their responses. \n\nHere's a breakdown:\n\n1. **Retrieval:**  RAG systems use a retrieval component to search a vast database of text and information. When a user asks a question, the system retrieves relevant documents or passages from this database.\n\n2. **Augmentation:** The retrieved information is then used to augment the LLM's input. This means that the LLM is not just relying on its internal knowledge but is also provided with external context.\n\n3. **Generation:** The LLM then generates a response based on both its internal knowledge and the retrieved information.\n\n**Why we use RAG:**\n\n* **Improved Accuracy:** RAG systems can access a wider range of information than LLMs alone, leading to more accurate and reliable answers.\n* **Enhanced Relevance:** By incorporating external context, RAG systems can provide responses that are more relevant to the user's query.\n* **Handling Factual Information:** LLMs are often trained on vast datasets of text, but they may not always have the most up-to-date or accurate information. RAG can help them access external sources to ensure they are providing factual answers.\n* **Domain Expertise:** RAG systems can be customized to specific domains by tailoring the retrieval database. This enables them to provide expert-level insights in various fields.\n\n**In essence, RAG combines the strengths of LLMs with the power of information retrieval to create more intelligent and informative language models.**\n",
            ],
        },
        {
            "role": "user",
            "parts": [
                "what are benefits of rag?\n",
            ],
        },
        {
            "role":
            "model",
            "parts": [
                "* Improved Accuracy\n* Enhanced Relevance\n* Handling Factual Information\n* Domain Expertise \n",
            ],
        },
    ])

    response = chat_session.send_message(question)

    return response.text
