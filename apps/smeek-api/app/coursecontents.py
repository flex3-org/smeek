import requests
import json
from youtubesearchpython import VideosSearch
import re

url = "http://localhost:11434/api/chat"

def llama3(topic):
    prompt = f"""
        You are a course content creator that creates the list of topics a person needs to study to understand the given subject. For example,
        User: French
        Assistant: [
            "French Alphabet and Pronunciation",
            "Basic Greetings and Introductions",
            "Numbers and Dates",
            "Common Phrases and Expressions",
            "French Grammar Basics",
            "Nouns, Articles, and Gender",
            "Pronouns (Subject, Object, Possessive)",
            "Verbs: Present Tense (Regular and Irregular)",
            "Adjectives and Adverbs",
            "Prepositions and Conjunctions",
            "Questions and Negations",
            "Past Tense: Passé Composé and Imparfait",
            "Future Tense and Conditional Mood",
            "Imperative Mood",
            "Vocabulary Building (Food, Travel, Family, etc.)",
            "Listening and Speaking Practice",
            "Reading Comprehension",
            "Writing Practice (Emails, Letters, Essays)",
            "Cultural Aspects (Customs, Traditions, Holidays)",
            "French in Context (Conversations, Dialogues, Situational French)"
        ]
        User: Python
        Assistant: [
            "Introduction to Python",
            "Setting Up the Python Environment",
            "Python Syntax and Semantics",
            "Variables and Data Types",
            "Operators (Arithmetic, Logical, Comparison)",
            "Control Structures (if, else, elif, loops)",
            "Functions and Lambda Expressions",
            "Lists, Tuples, and Dictionaries",
            "String Manipulation",
            "File Handling (Reading, Writing, Working with Files)",
            "Error Handling and Exceptions",
            "Modules and Packages",
            "Object-Oriented Programming (OOP)",
            "Classes and Objects",
            "Inheritance, Polymorphism, Encapsulation",
            "Working with Libraries (NumPy, Pandas, etc.)",
            "Introduction to Web Development with Python (Flask, Django)",
            "Introduction to Databases (SQLite, PostgreSQL)",
            "APIs and RESTful Services",
            "Testing and Debugging",
            "Python for Data Science and Machine Learning",
            "Best Practices and Code Optimization",
            "Version Control with Git"
        ]

        User: {topic}
        Assistant:
    """
    

    data = {
        "model": "llama3",
        "temperature":0.0,
        "messages": [
            {
                "role": "user",
                "content": prompt

            }
        ],
        "stream": False,
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=data)
    response = response.json()["message"]["content"]
    regex = r'"\s*(.*?)\s*"'
    matches = re.findall(regex, response)
    formatted_list = '[' + ', '.join(f'"{match}"' for match in matches) + ']'
    list_data = json.loads(formatted_list)
    return list_data



def get_yt_links(topics):
    links = []
    for t in topics:
        try:
            videosSearch = VideosSearch(t, limit = 4)
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

