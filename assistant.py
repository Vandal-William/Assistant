import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime
   
listener=sr.Recognizer()
engine=ttx.init()
voice=engine.getProperty('voices')
engine.setProperty('voice','french') 
marche=True

# fonction qui transforme le texte en parole et attend  
def parler(text):
    engine.say(text)
    engine.runAndWait()

def lancer_assistant(command):
    print(command)
    if 'recherche' in command:
        titre=command.replace('recherche','')
        pywhatkit.playonyt(titre)
    elif 'heure' in command:
        heure=datetime.datetime.now().strftime('%H:%M')
        print('il est'+' : '+heure)
    else:
        print('je ne comprends pas')

def ecouter():

    try:
        # ici on utilise la micro comme source
        with sr.Microphone() as source:
            print('Que puis-je faire pour vous ?')
            # sert a générer une voix 
            voix=listener.listen(source)
            # interprète la voix avec google en français
            command=listener.recognize_google(voix, language='fr-FR')
            lancer_assistant(command)
    except:
        pass
    return command

while marche : 

    with sr.Microphone() as source:
        voix=listener.listen(source)
        command=listener.recognize_google(voix, language='fr-FR')
        if 'assistant' in command:
            command=ecouter()
            
    