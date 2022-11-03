import nltk
import speech_recognition as sr
from gtts import gTTS
import os
import time

def point_dictionary(count):
    # point dictionary for player
    dictionary = {
        0: 10,
        1: 8,
        2: 6,
        3: 4,
        4: 2,
        5: 0
    }
    return dictionary[count]

def text_to_speech(message, message_id):
    language = "en"  # use english
    speech = gTTS(text=message, lang=language, slow=False)
    speech.save(message_id)  # save sound to file
    os.system(message_id)

user_points = 0
total_points = 0
score = 0

recognizer = sr.Recognizer()
# creation of speech recognizer
microphone = sr.Microphone(device_index=0)
# creation of microphone object to listen to speaker

user_name = input("Hello user what is your name?: ")

text_to_speech("Welcome " + user_name + " this is a speech recognition game!\n"
                               "For each word, you will have 5 tries and at end of the game\n"
                               "you will be graded on your performance.", "2.mp3")
time.sleep(10)

filehandle = open("test.txt")
# opening text file
text = filehandle.read()
filehandle.close()

words = nltk.word_tokenize(text)
# separating words in text file

text_to_speech("On each iteration please state the word on the console", "3.mp3")
time.sleep(10)
for i in words:
    # initial loop for words list
    index = 0
    # prompting of user
    print(i)

    while index < 5:
        # user gets 5 tries
        try:
            # try except block if program doesn't catch your voice
            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                # capturing speech

            if i == recognizer.recognize_google(audio):
                # comparing what was stated to what is at current index
                text_to_speech("Huzzah you said the correct word", "4.mp3")
                time.sleep(10)
                user_points += point_dictionary(index)
                total_points += 10
                break
            else:
                index += 1
                text_to_speech(f"Try again. You have {5 - index} tries left.\n", "5.mp3")
                time.sleep(10)
                for i in range(10, 0, -1):
                    print(f"In {i}")
                    time.sleep(1)

        except:
            raise Exception("make sure you state your word clearly. No points have been awarded.\n"
                            "Try again.")

        finally:
            if index == 5:
                # if user didnt state word correctly
                text_to_speech("To bad. You did not win any points.", "6.mp3")

            try:
                # incorporation of possible error if first try except block outputs 0 as score
                score = (user_points / total_points) * 100
            except:

                print(f"Good job. You got a {score}%")
                raise Exception("You can't divide zero by zero")

            finally:
                if i == len(words):
                    if score > 89:
                        print(f"Congrats " + user_name + f" you scored a {score}%")
                    elif score > 79 and score < 90:
                        print(f"You scored a {score}%")

                    elif score > 69 and score < 79:
                        print(f"You scored a {score}%")
                    else:
                        print(f"{score}% accuracy")