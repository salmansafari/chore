#pip install SpeechRecognition pydub
import speech_recognition as sr

wav_file = "output.wav"

r = sr.Recognizer()
with sr.AudioFile(wav_file) as source:
    audio = r.record(source)
    text = r.recognize_google(audio)
    print(text)
