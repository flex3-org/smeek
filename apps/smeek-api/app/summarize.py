import yt_dlp
import numpy as np
import librosa
import requests
import re
import json
import torch
import os
from transformers import pipeline

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
    audio, sr = librosa.load(audio_path, sr=16000)  # Whisper expects 16kHz sampling rate
    
    # Load the Whisper model
    device = 0 if torch.cuda.is_available() else -1  # Use GPU if available, otherwise use CPU
    transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base", device=device)
    
    # Process audio array with Whisper
    result = transcriber({"array": audio, "sampling_rate": sr})
    
    return result['text']

# Function to summarize text using Llama3 from Ollama
def llama3_summarize(text):
    url = "http://localhost:11434/api/chat"  # Replace with the correct URL

    prompt = f"""
    You are an agent that takes transcript of a video and then write everything explained in the video in proper format by mentioning all important points.
    here is the transcript:
    {text}
    """
    
    data = {
        "model": "llama3",
        "temperature": 0.0,
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
    response_json = response.json()
    summary = response_json.get("message", {}).get("content", "")

    return summary

# Main function to summarize a YouTube video
def summarize_youtube_video(youtube_url):
    audio_path = "temp_audio.wav"
    
    # Download audio from YouTube video
    download_audio(youtube_url, audio_path)
    print("Audio downloaded")

    # Convert audio to text
    text = audio_to_text_whisper(audio_path)
    print("Converted from audio to text")
    # print(text)

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
