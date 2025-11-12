# pip install nltk pyttsx3
# py -m nltk.downloader popular 
# pip install gTTS
from gtts import gTTS
import nltk

nltk.download('punkt')
text = "Hello, My name is John."
tts = gTTS(text)
tts.save("output.mp3")
print("Speech saved as output.mp3")