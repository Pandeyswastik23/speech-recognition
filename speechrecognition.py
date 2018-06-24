import pyttsx3
import speech_recognition as sr
import pocketsphinx
import pyaudio
import random,os

engine = pyttsx3.init()
def listen():
     r=sr.Recognizer()
     r.energy_threshold = 4000



    
     with sr.Microphone() as source:
      a = r.listen(source)

try:

                return r.recognize_sphinx(a)

                except sr.UnknownValueError:
                    print('could not understand audio')

                except sr.RequestError as e:
                    print("Recog Error; (0)".format(e))

        
                return ""
    
def media():
    say('ok sir')
    say('starting all required applications')
    say('what do you want me to play for you')
    k = listen()
    say('ok sir' + k + 'for you')
    os.startfile('D:\SONGS\new songs\ellie goulding+k+.mp3')




def shutdown():
    say('understood sir')
    say('connecting to the command prompt')
    say('shutting down your laptop')
    os.system('shutdown -s')

def  gooffline():
    say('ok sir')
    say('disconnecting from server')
    say('closing all systems')
    say('going offline')
    quit()
    
def say(text):
   

    engine.say(text)
    engine.setProperty('rate',200)
    engine.runAndWait()
def online():
    say('ok sir')
    say('starting all system applications')
    say('installing all drivers')
    say('every driver is installed')
    say('every system is started')
    say('I am online sir')

def mainfunction():
    a = r.listen(source)
    user = r.recognize_sphinx(a)
    print(user)

    if user == "zarvis":
        online()
    elif user == "song":
        media()
    elif user == "down":
        gooffline()
    elif user == "shutdown":
        shutdown()

    elif user in ['hii','hey','how are you','whats going on']:
        d = random.choice([['hey','hii','I am good','its a busy day though sir'])
        speak(d)
        
        
    
say('welcome to the program of speech recognition')

if __name__ == "__main__":
    r=sr.Recognizer()
    r.energy_threshold = 4000
    with sr.Microphone() as source:
        while 1:
            mainfunction()
