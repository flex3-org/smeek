import pymupdf
import time
from dotenv import load_dotenv
import os
import google.generativeai as genai
import ast

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])


# Step 1: Extract Text from PDF
def extract_text_from_pdf(pdf_path):
    doc = pymupdf.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


# Step 2: Chunk the Text Manually
def chunk_text(text, max_length=5000):
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

    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
        system_instruction=
        "Take this given flashcard content\nyou should give output only if the content seems important to know \nand give me output in json format where there are two field for each, 'title' and 'description'.\nOUTPUT MUST BE in JSON",
    )

    chat_session = model.start_chat(history=[
        {
            "role":
            "user",
            "parts": [
                "about the structure of the DNA \"double helix\" by Watson & Crick and the development of DNA sequencing methods by Fredrick Sanger. II. The chemical basis of life. The biomolecules such as proteins that are present in living organisms are carbon-based compounds. Carbon is the third most abundant element in living organisms (relative abundance H > O > C > N > P > S). Fig. 1.1. shows the 29 elements found in living organisms. The most common ions are Ca+2, K+, Na+, Mg+2, and Cl-. The properties of biomolecules, such as shape and chemical reactivity, are best described by the discipline of organic chemistry. A. Representations of molecular structures. Your text will use skeletal, ball & stick, and space-filling models to show molecular structures. Therefore, you must be familiar with each of these types of representations. Skeletal and ball & stick models are good for showing the positions of nuclei in organic compounds. Space-filling models show van der Waals radii of the atoms in\n",
            ],
        },
        {
            "role":
            "model",
            "parts": [
                "```json\n[\n  {\n    \"title\": \"Structure of DNA\",\n    \"description\": \"The DNA double helix structure was discovered by Watson & Crick.\"\n  },\n  {\n    \"title\": \"DNA Sequencing\",\n    \"description\": \"Frederick Sanger developed methods for DNA sequencing.\"\n  },\n  {\n    \"title\": \"Chemical Basis of Life\",\n    \"description\": \"Biomolecules, like proteins, are carbon-based. Carbon is the third most abundant element in living organisms.\"\n  },\n  {\n    \"title\": \"Important Elements in Living Organisms\",\n    \"description\": \"Key elements include Hydrogen (H), Oxygen (O), Carbon (C), Nitrogen (N), Phosphorus (P), and Sulfur (S). Common ions are Ca+2, K+, Na+, Mg+2, and Cl-.\"\n  },\n  {\n    \"title\": \"Organic Chemistry and Biomolecules\",\n    \"description\": \"Organic chemistry helps describe the shape and reactivity of biomolecules.\"\n  },\n  {\n    \"title\": \"Molecular Structure Representations\",\n    \"description\": \"Skeletal, ball & stick, and space-filling models are used to represent molecules. Skeletal and ball & stick models are good for showing nuclei positions, while space-filling models show van der Waals radii.\"\n  }\n]\n```",
            ],
        },
    ])

    response = chat_session.send_message(flashcards)

    response = response.text

    start = response.find("[")
    end = response.rfind("]") + 1
    response = response[start:end]

    python_list = ast.literal_eval(response)

    return python_list


def generate_flashcards(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    print("text extracted")
    chunks = chunk_text(text, max_length=1000)
    print("Chunks created!")
    flashcards = []
    start = time.time()
    for chunk in chunks:
        summary = get_json(chunk)
        flashcards += (summary)
    end = time.time()
    print('Time taken', end - start)
    # ans = []
    # for n, i in enumerate(flashcards):
    #     try:
    #         res = {}
    #         res['title'] = i['title']
    #         res['desc'] = i['description']
    #         ans.append(res)
    #     except:
    #         pass

    return flashcards


# # testing...
flashcards = generate_flashcards("example.pdf")
