import pymupdf  # PyMuPDF
import requests
import ast
import json
import ollama
import re

# Step 1: Extract Text from PDF
def extract_text_from_pdf(pdf_path):
    doc = pymupdf.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Step 2: Chunk the Text Manually
def chunk_text(text, max_length=500):
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        if current_length + len(word) <= max_length:
            current_chunk.append(word)
            current_length += len(word) + 1
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = len(word) + 1

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks



def get_json(flashcards):
    output_temp = """
        {
                "question": "What is the primary difference between classical and quantum computers?",
                "type": "multiple_choice",
                "options": (
                    "A quantum computer uses bits.",
                    "A classical computer uses qubits.",
                    "A quantum computer uses qubits.",
                    "A classical computer uses photons."
                ),
                "correct_answer": "A quantum computer uses qubits."
            }
"""
    prompt = f"""
    Understand this content: {flashcards}
    you should give me a question, four options and out of the four options only one answers the question correctly.
    
    OUTPUT MUST BE in following format:
    {output_temp}
    """
    response = ollama.chat(model='llama3', messages=[
    {
        'role': 'user',
        'content': prompt,
    },
    ])
    ans = response['message']['content']
    pattern = re.compile(r'"(\w+)":\s*("(?:[^"\\]|\\.)*?"|\(.*?\))', re.DOTALL)

    # Find all key-value pairs
    matches = pattern.findall(ans)

    # Initialize the dictionary
    result_dict = {}

    for key, value in matches:
        # Handle options separately
        if key == 'options':
            # Remove parentheses and split by comma
            value = value.strip('()').split(',\n')
            # Remove extra spaces and quotes
            value = [option.strip().strip('"') for option in value]
        else:
            # Remove quotes from other values
            value = value.strip('"')
        result_dict[key] = value

    # Print the resulting dictionary or convert to JSON
    return result_dict




# text = extract_text_from_pdf("example.pdf")
# chunks = chunk_text(text)
# quiz = []
# for chunk in chunks:
#     quiz.append(get_json(chunk))

# # print(quiz)
# print(type(quiz))
# json_data = json.dumps(quiz)
# print(type(json_data))

