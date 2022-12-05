import speech_recognition as sr
import pywhatkit
import datetime
from gtts import gTTS
import os
   
listener= sr.Recognizer()
TMP_FILE = "./tts_File"
marche=True


def gtts(phrase_to_read):
	tts = gTTS(text=phrase_to_read, lang="fr")
	tts.save(TMP_FILE + ".mp3")
	os.system("mpg321 -q {}{}".format(TMP_FILE, ".mp3"))

def lancer_assistant(command):
    print(command)
    if 'recherche' in command:
        titre=command.replace('recherche','')
        pywhatkit.playonyt(titre)
    elif 'heure' in command:
        heure=datetime.datetime.now().strftime('%H:%M')
        gtts('il est'+heure)
    else:
        gtts('je ne comprends pas')
        ecouter()

def ecouter():

    # ici on utilise la micro comme source
    with sr.Microphone() as source:
        gtts('Que puis-je faire pour vous ?')
        # sert a générer une voix 
        voix=listener.listen(source)
        # interprète la voix avec google en français
        command=listener.recognize_google(voix, language='fr-FR')
        lancer_assistant(command)

gtts("Bonjour, si vous voulez démarrer l'application dite, 'assistant' ")   

while marche : 

    with sr.Microphone() as source:
        voix=listener.listen(source)
        command=listener.recognize_google(voix, language='fr-FR')
        if 'assistant' in command:
            ecouter()
            
    