import pymupdf  # PyMuPDF
import re
import json
import ollama
import time

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
    prompt = f"""
    Take this flashcard content: {flashcards}
    you should give output only if the content seems important to know 
    and give me output in json format where there are two field for each, 'title' and 'description'.
    OUTPUT MUST BE in JSON
    """
    response = ollama.chat(model='llama3', messages=[
    {
        'role': 'user',
        'content': prompt,
    },
    ])
    ans = response['message']['content']
    regex_pattern = r'(\[\s*{.*?}\s*\])'
    matches = re.search(regex_pattern, ans, re.DOTALL)
    data = None
    # Get the matched list part
    if matches:
        extracted_list = matches.group(1)
        data = json.loads(extracted_list)
    else:
        pass
    return data




def generate_flashcards(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    print("text extracted")
    chunks = chunk_text(text, max_length=1000)
    print("Chunks created!")
    print(len(chunks))
    flashcards = []
    start = time.time()
    for chunk in chunks:
            summary = get_json(chunk)
            flashcards += (summary)
    end = time.time()
    print('Time taken', end-start)
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
# flashcards = generate_flashcards("example.pdf")
