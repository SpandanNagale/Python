import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

def speak(audio):
 engine.say(audio)
 engine.runAndWait()

def greet():
  speak("Hhey!!")
  hour=int(datetime.datetime.now().hour)
  if hour>6 and hour<12:
    speak("good morning")
  elif hour>12 and hour<15:
    speak('Good afternoon')
  elif hour>15 and hour<18:
    speak("Good evening")
  else:
    speak('good night')
  speak("I am villain , I am here to help you")

def command():
  r=sr.Recognizer()
  with sr.Microphone() as source:
    print("listening.....")
    r.pause_threshold = .8
    audio=r.listen(source)
    r.energy_threshold=600
    # r.adjust_for_ambient_noise(source,duration=0.2)
  
  try:
    print("recognizing...")
    query= r.recognize_google(audio, language='en-in')
    print("user said:",query)
  except Exception as e:
     print("say that again")
     return "none"
  return query

greet()

query=command().lower()
 
if "wikipedia" in query:
   speak('searching wikipedia')
   query=query.replace("wikipedia","")
   result=wikipedia.summary(query,sentences=2)
   print(result)
   speak(result)
elif "open youtube" in query:
  webbrowser.open("youtube.com")
elif "open special" in query:
  webbrowser.open("https://www.damplips.com/.com")
elif "play music" in query:
  music_list="D:\\songs"
  songs=os.listdir(music_list)
  i=random.randint(0,130)
  os.startfile(os.path.join(music_list ,songs[i]))
elif "want to watch anime" in query:
  webbrowser.open("https://hianime.to/")
elif "open chatgpt" in query:
  webbrowser.open("https://chat.openai.com/")
elif "anime please" in query:
  anime="D:\\Anime"
  s=os.listdir(anime)
  i=random.randint(0,11)
  os.startfile(os.path.join(anime ,s[i]))