from fastapi import APIRouter
import openai
import sounddevice as sd
from scipy.io.wavfile import write
import tempfile
import os

router = APIRouter()

openai.api_key = os.getenv("API_KEY")
client = openai.OpenAI(api_key=openai.api_key)

KEYWORDS = ["search", "cancel", "open", "hello"]

def record_audio(duration=5, fs=16000):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    write(temp_file.name, fs, audio)
    print(f"Saved audio to {temp_file.name}")
    return temp_file.name

def transcribe_with_openai(audio_path):
    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcript.text

def search_keywords(transcription, keywords):
    found = [kw for kw in keywords if kw.lower() in transcription.lower()]
    return found

@router.post("/audio/search")
def run_audio_search():
    audio_file = record_audio()
    try:
        transcription = transcribe_with_openai(audio_file)
        found = search_keywords(transcription, KEYWORDS)
    finally:
        os.remove(audio_file)

    return {
        "transcription": transcription,
        "keywords_found": found
    }
