import os
import google.generativeai as genai
from dotenv import load_dotenv
from youtubesearchpython import VideosSearch
import ast

# Load environment variables from .env file
load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])


def get_content(topic):
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
        "You are a course content creator that creates the list of topics a person needs to study to understand the given subject. You will give a python list as an output containing only the headings of the topic that are required to learn the subject. For example,\n        User: French\n        Assistant: [\n            \"French Alphabet and Pronunciation\",\n            \"Basic Greetings and Introductions\",\n            \"Numbers and Dates\",\n            \"Common Phrases and Expressions\",\n            \"French Grammar Basics\",\n            \"Nouns, Articles, and Gender\",\n            \"Pronouns (Subject, Object, Possessive)\",\n            \"Verbs: Present Tense (Regular and Irregular)\",\n            \"Adjectives and Adverbs\",\n            \"Prepositions and Conjunctions\",\n            \"Questions and Negations\",\n            \"Past Tense: Passé Composé and Imparfait\",\n            \"Future Tense and Conditional Mood\",\n            \"Imperative Mood\",\n            \"Vocabulary Building (Food, Travel, Family, etc.)\",\n            \"Listening and Speaking Practice\",\n            \"Reading Comprehension\",\n            \"Writing Practice (Emails, Letters, Essays)\",\n            \"Cultural Aspects (Customs, Traditions, Holidays)\",\n            \"French in Context (Conversations, Dialogues, Situational French)\"\n        ]\n        User: Python\n        Assistant: [\n            \"Introduction to Python\",\n            \"Setting Up the Python Environment\",\n            \"Python Syntax and Semantics\",\n            \"Variables and Data Types\",\n            \"Operators (Arithmetic, Logical, Comparison)\",\n            \"Control Structures (if, else, elif, loops)\",\n            \"Functions and Lambda Expressions\",\n            \"Lists, Tuples, and Dictionaries\",\n            \"String Manipulation\",\n            \"File Handling (Reading, Writing, Working with Files)\",\n            \"Error Handling and Exceptions\",\n            \"Modules and Packages\",\n            \"Object-Oriented Programming (OOP)\",\n            \"Classes and Objects\",\n            \"Inheritance, Polymorphism, Encapsulation\",\n            \"Working with Libraries (NumPy, Pandas, etc.)\",\n            \"Introduction to Web Development with Python (Flask, Django)\",\n            \"Introduction to Databases (SQLite, PostgreSQL)\",\n            \"APIs and RESTful Services\",\n            \"Testing and Debugging\",\n            \"Python for Data Science and Machine Learning\",\n            \"Best Practices and Code Optimization\",\n            \"Version Control with Git\"\n        ]",
    )

    chat_session = model.start_chat(history=[
        {
            "role": "user",
            "parts": [
                "Quantum Comupting",
            ],
        },
        {
            "role":
            "model",
            "parts": [
                "```python\n[\n    \"Introduction to Quantum Computing\",\n    \"Quantum Mechanics Basics\",\n    \"Qubits and Superposition\",\n    \"Entanglement and Quantum Correlations\",\n    \"Quantum Gates and Circuits\",\n    \"Quantum Algorithms (Deutsch-Jozsa, Shor's, Grover's)\",\n    \"Quantum Teleportation\",\n    \"Quantum Error Correction\",\n    \"Quantum Cryptography\",\n    \"Applications of Quantum Computing\",\n    \"Quantum Computing Platforms (Superconducting, Trapped Ions, etc.)\",\n    \"Quantum Programming Languages (Qiskit, Cirq)\",\n    \"The Future of Quantum Computing\"\n]\n```",
            ],
        },
    ])

    response = chat_session.send_message(topic)

    response = response.text

    start = response.find("[")
    end = response.rfind("]") + 1
    response = response[start:end]

    python_list = ast.literal_eval(response)

    return python_list


response = get_content("Theory of Computation")
print(type(response))


def get_yt_links(topics):
    links = []
    for t in topics:
        try:
            videosSearch = VideosSearch(t, limit=4)
        except:
            link_list = []
            links.append(link_list)
            continue
        link_list = []
        for i in range(4):
            try:
                link_list.append(videosSearch.result()['result'][i]['link'])
            except:
                pass
        links.append(link_list)

    return links


# topics = llama3("LLMOps")
# print("Topics: ", topics)
# print(type(topics))

# links = get_yt_links(topics)
# print("Links: ", links)
# print(type(links))
