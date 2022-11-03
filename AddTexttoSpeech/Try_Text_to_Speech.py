from gtts import gTTS
import os  ## allows you to play the mp3 file

def text_to_speech(message):
    language = "en"  ## use english
    speech = gTTS(text = message, lang = language, slow = False)
    speech.save("testmessage.mp3")  ##save sound to file
    os.system("testmessage.mp3")

text_to_speech("This is a test")