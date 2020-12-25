import webbrowser

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from playsound import playsound
from datetime import date

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
   engine.say(text)
   engine.runAndWait()

   def wishMe():
       hour = datetime.datetime.now().hour
       if hour >= 0 and hour < 12:
           talk("Hello,Good Morning")
           print("Hello,Good Morning")
       elif hour >= 12 and hour < 18:
           talk("Hello,Good Afternoon")
           print("Hello,Good Afternoon")
       else:
           talk("Hello,Good Evening")
           print("Hello,Good Evening")


def take_command():
    try:
        with sr.Microphone() as source:
             print('listening...')
             voice=listener.listen(source)
             command = listener.recognize_google(voice)
             command= command.lower()
             if 'alexa' in command:
                 command = command.replace('alexa','')
                 print(command)
    except:
        pass
    return command


def run_alexa ():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is' , '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry i have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with your wifi')
    elif 'do you love me' in command:
        talk('I love you as a sister')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'which language were you made' in command:
        talk('I was made in python i guess')
    elif ' what can you do' in command:
        talk('I can say jokes also I can also answer to your questions')
    elif 'recommend me some places to visit' in command:
        talk('I would recommend you visit India Australia,France,Canada and USA')
    elif 'who made you' in command:
        talk('I was made by a teenager named Rahul and i guess he is smart')
    elif 'what is your name' in command:
        talk('My Actual Name is Strex')
    elif 'change your voice' in command:
        talk('Sorry its not available now')
    elif 'open google' in command:
        talk('opening google')
        webbrowser.open_new_tab("google.com")

    elif 'open instagram' in command:
        webbrowser.open_new("instagram.com")
        talk('opening now itself')

    elif 'open facebook' in command:
        webbrowser.open_new("facebook.com")
        talk('opening facebook')

    elif 'open snapchat' in command:
        webbrowser.open_new("snapchat.com")
        talk('opening snapchat')

    elif 'who made ai' in  command:
        talk('Herbert Simon and Allen Newell in 1955')
        print("Herbert Simon and Allen Newell in 1955")

    elif 'developed you' in command:
        webbrowser.open_new_tab("https://cartoonloverz992.wixsite.com/incentive")
        talk('Incentive Studio developed me and was made by rahul and i was made to help you')

    elif 'who are your competitors' in  command:
        talk('My competitors are Amazon Alexa,Google Assistant,Samsung Bixby and Cortana')
        talk('My competitors are Amazon Alexa,Google Assistant,Samsung Bixby and Cortana')
        print("My competitors are Amazon Alexa,Google Assistant,Samsung Bixby,Siri and Cortana")


    else:
        talk('Sorry could you  please repeat that again.')





run_alexa()