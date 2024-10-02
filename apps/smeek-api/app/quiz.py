import pymupdf
import re
import google.generativeai as genai
from dotenv import load_dotenv
import os

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


def get_json(quiz):

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
        "Understand the given content content\n you should give me a question, four options and out of the four options only one answers the question correctly.\n    \n    OUTPUT MUST BE in following format:\n\"question\": \"What is the primary difference between classical and quantum computers?\",\n                \"type\": \"multiple_choice\",\n                \"options\": (\n                    \"A quantum computer uses bits.\",\n                    \"A classical computer uses qubits.\",\n                    \"A quantum computer uses qubits.\",\n                    \"A classical computer uses photons.\"\n                ),\n                \"correct_answer\": \"A quantum computer uses qubits.\"",
    )

    chat_session = model.start_chat(history=[
        {
            "role":
            "user",
            "parts": [
                "principles of organic chemistry and other basic sciences. It is of no surprise that the first \"biochemists\" actually were organic chemists who specialized in the chemistry of compounds derived from living organisms. The text provides an historical overview of some of the key contributions of the early chemists, and of modern 20th century biochemists who have lead the discipline to where it is today. Research endeavors such as the human genome project ultimately owe their success to basic",
            ],
        },
        {
            "role":
            "model",
            "parts": [
                "\"question\": \"According to the text, what was the original profession of the first biochemists?\",\n                \"type\": \"multiple_choice\",\n                \"options\": (\n                    \"Physicists\",\n                    \"Biologists\",\n                    \"Organic Chemists\",\n                    \"Geneticists\"\n                ),\n                \"correct_answer\": \"Organic Chemists\" \n",
            ],
        },
    ])

    response = chat_session.send_message(quiz)
    if response._done:  # Ensure the response is done
        # Access the first candidate's content
        text_content = response._result.candidates[0].content.parts[0].text

        ans = text_content
        pattern = re.compile(r'"(\w+)":\s*("(?:[^"\\]|\\.)*?"|\(.*?\))',
                             re.DOTALL)

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
    else:
        raise ValueError("The response is not completed successfully.")


# text = extract_text_from_pdf("example.pdf")
# chunks = chunk_text(text)
# quiz = []
# print(get_json(chunks[1]))
# # for chunk in chunks:
# #     quiz.append(get_json(chunk))

# # # print(quiz)
# # print(type(quiz))
# # json_data = json.dumps(quiz)
# # print(type(json_data))
