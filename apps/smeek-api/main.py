from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.coursecontents import llama3, get_yt_links
from app.chatbot import ask_anything
from app.quiz import extract_text_from_pdf, chunk_text, get_json
from app.flashcard import generate_flashcards

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/coursecontents/")
async def course_content(topic: str):
    topics = llama3(topic)
    links = get_yt_links(topics)
    content = [
        {"index": index + 1, "topic": topic, "link": link} 
        for index, (topic, link) in enumerate(zip(topics, links))
    ]
    return JSONResponse(content=content, media_type="application/json")

@app.get("/chatbot/")
async def chatbot_interaction(inp: str):
    response = ask_anything(inp)
    result = {"response": response}
    return JSONResponse(content=result, media_type="application/json")

@app.get("/quiz/")
async def quiz_from_pdf(file: UploadFile = File(...)):
    content = await file.read()
    with open(file.filename, 'wb') as f:
        f.write(content)
    text = extract_text_from_pdf(file.filename)
    chunks = chunk_text(text)
    quiz = []
    for chunk in chunks:
        quiz.append(get_json(chunk))
    return JSONResponse(content=quiz, media_type="application/json")

@app.get("/flashcards/")
async def flashcards_from_pdf(file: UploadFile = File(...)):
    content = await file.read()
    with open(file.filename, 'wb') as f:
        f.write(content)
    flashcards = generate_flashcards(file.filename)
    return JSONResponse(content=flashcards, media_type="application/json")
