
import speech_recognition as sr
from gtts import gTTS
import os

def text_to_speech(message):
    language = "en"  ## use english
    speech = gTTS(text = message, lang = language, slow = False)
    speech.save("testmessage.mp3")  ##save sound to file
    os.system("testmessage.mp3")

done = False
print(sr.__version__)
recognizer = sr.Recognizer()
#print(sr.Microphone.list_microphone_names())
mic = sr.Microphone(device_index=0)

# print("Say a word or phrase: ")
# with mic as source:
#      recognizer.adjust_for_ambient_noise(source)
#      audio = recognizer.listen(source)
# print(recognizer.recognize_google(audio))



while not done:
     try:
          print("Say a word or phrase: ")
          with mic as source:
               recognizer.adjust_for_ambient_noise(source)
               audio = recognizer.listen(source)

          word = recognizer.recognize_google(audio)
          print(word)
          word = "I heard " + word
          text_to_speech("hello world")
          done = True
     except sr.UnknownValueError:
          print("Try again")


