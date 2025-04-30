from fastapi import APIRouter, HTTPException
import speech_recognition as sr

router = APIRouter()

@router.get("/speech-to-text")
def recognize_speech_from_microphone():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Please say something...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = recognizer.listen(source)
            print("Audio captured")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Microphone error: {e}")

    try:
        text = recognizer.recognize_google(audio)
        return {"transcription": text}
    except sr.UnknownValueError:
        raise HTTPException(status_code=400, detail="Could not understand the audio.")
    except sr.RequestError as e:
        raise HTTPException(status_code=502, detail=f"Google Speech Recognition API error: {e}")
