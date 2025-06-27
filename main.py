import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer= sr.Recognizer()
engine= pyttsx3.init()
newsapi= "your_api_key"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def speak_old(text):
    gtts=gTTS(text)
    gtts.save("temp.mp3")

    # Initialize the mixer and Pygame
    pygame.init()
    pygame.mixer.init()

    # Load your MP3 file
    pygame.mixer.music.load("temp.mp3")

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running while music plays
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiprocess(command):
    client = OpenAI(
    api_key="your_api_key"
    )

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "system", "content": "You are a virtual assistant Nova skilled in general tasks like Alexa and Google. Give short responses"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song= c.lower().split(" ")[1]
        link= musiclibrary.music(song)
        webbrowser.open(link)
    elif "news" in c.lower():
        r= requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code==200:
            data=r.json()
            articles= data.get('articles',[])
            for article in articles:
                speak(article['title'])
    else :
        #let OpenAI handle the requests
        output= aiprocess(c)
        speak(output)


if __name__ == "__main__":
    speak("Initializing Nova")
    while True:
        #Listen for the wake word "Nova"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recognising...")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word= r.recognize_google(audio)
            if word.lower()=="nova":
                speak("Ya")
                #Listen for command
                with sr.Microphone() as source:
                    print("Nova Active!")
                    audio = r.listen(source,timeout=2,phrase_time_limit=1)
                    command= r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))