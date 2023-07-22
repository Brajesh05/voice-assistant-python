import importlib
pyttsx3 = importlib.import_module('pyttsx3')
speech_recognition = importlib.import_module('speech_recognition')
sr= speech_recognition
import datetime
wikipedia= importlib.import_module('wikipedia')
wiki= wikipedia
import webbrowser
import os
 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")

    speak("i am here to follow your commands sir. please tell me what i can do for you")
def takecommand():
    '''it takes microphone input from the user and returns the string output 
    '''
    
    r = sr.Recognizer( )
    with sr.Microphone() as source:
        print("pls say ...")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("understanding...") 
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query 

if __name__ == "__main__":
    speak("hello welcome to world of voice command , i am your assistant at service")
    wishMe()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 10)
            speak("according to wikipedia")
            speak(results)
        elif 'open youtube'in query:
            webbrowser.open("youtube.com")
        elif 'open google'in query:
            webbrowser.open("google.com")
        elif 'open gmail'in query:
            webbrowser.open("gmail.com")
        elif 'open stackoverflow 'in query:
            webbrowser.open("https://stackoverflow.com/")
        elif 'open songs'in query:
            webbrowser.open("https://wynk.in/music/package/new-hindi-songs/bb_1404393019358")
        elif 'the time' in query:
            strtime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strtime}")


    