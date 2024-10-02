from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.coursecontents import get_content, get_yt_links
# from app.chatbot import get_chatbot_response, ChatInput
# from app.quiz import extract_text_from_pdf, chunk_text, get_json
# from app.flashcard import generate_flashcards
# from app.summarize import summarize_youtube_video

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
    topics = get_content(topic)
    links = get_yt_links(topics)
    content = [{
        "index": index + 1,
        "topic": topic,
        "link": link
    } for index, (topic, link) in enumerate(zip(topics, links))]
    return JSONResponse(content=content, media_type="application/json")


# @app.post("/chat/")
# async def chat_endpoint(chat_input: ChatInput):
#     response = get_chatbot_response(chat_input.user_input)
#     return JSONResponse(content={"response": response}, media_type="application/json")

# @app.post("/quiz/")
# async def quiz_from_pdf(file: UploadFile = File(...)):
#     content = await file.read()
#     with open(file.filename, 'wb') as f:
#         f.write(content)
#     text = extract_text_from_pdf(file.filename)
#     chunks = chunk_text(text)
#     quiz = []
#     for chunk in chunks:
#         quiz.append(get_json(chunk))
#     return JSONResponse(content=quiz, media_type="application/json")

# @app.post("/flashcards/")
# async def flashcards_from_pdf(file: UploadFile = File(...)):
#     content = await file.read()
#     with open(file.filename, 'wb') as f:
#         f.write(content)
#     flashcards = generate_flashcards(file.filename)
#     return JSONResponse(content=flashcards, media_type="application/json")

# @app.get("/summary/")
# async def summary(url: str):
#     summary = summarize_youtube_video(url)
#     return JSONResponse(content={"response": summary}, media_type="application/json")
