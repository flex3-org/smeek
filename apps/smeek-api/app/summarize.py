import yt_dlp
import numpy as np
import librosa
import torch
import os
from transformers import pipeline
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])


# Function to download audio from YouTube video
def download_audio(youtube_url, audio_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': audio_path,
        'noplaylist': True,
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])


# Function to convert audio to text using Whisper
def audio_to_text_whisper(audio_path):
    # Load audio file into a NumPy array
    audio, sr = librosa.load(audio_path,
                             sr=16000)  # Whisper expects 16kHz sampling rate

    # Load the Whisper model
    device = 0 if torch.cuda.is_available(
    ) else -1  # Use GPU if available, otherwise use CPU
    transcriber = pipeline("automatic-speech-recognition",
                           model="openai/whisper-base",
                           device=device,
                           return_timestamps=True)

    # Process audio array with Whisper
    result = transcriber({"array": audio, "sampling_rate": sr})

    return result['text']


# Function to summarize text using Llama3 from Ollama
def llama3_summarize(text):

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
        "You are an agent that takes transcript of a video and then write everything explained in the video in proper format by mentioning all important points.",
    )

    chat_session = model.start_chat(history=[])

    response = chat_session.send_message(text)

    return response.text


# Main function to summarize a YouTube video
def summarize_youtube_video(youtube_url):
    audio_path = "temp_audio.wav"

    # Download audio from YouTube video
    download_audio(youtube_url, audio_path)
    print("Audio downloaded")

    # Convert audio to text
    text = audio_to_text_whisper(audio_path)
    print("Converted from audio to text")
    print(text)

    if os.path.exists(audio_path):
        os.remove(audio_path)
        print(f"{audio_path} has been deleted.")
    else:
        print(f"{audio_path} does not exist.")

    # Summarize text using Llama3
    summary = llama3_summarize(text)
    print("Summarized")

    return summary


# # Example usage
# if __name__ == "__main__":
#     youtube_url = "https://www.youtube.com/watch?v=3-c4xJa7Flk&t=1466s"  # Replace with your YouTube video URL
#     summary = summarize_youtube_video(youtube_url)
#     print("Summary:", summary)
