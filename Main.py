import pyttsx3
import wikipedia as wiki
from os import system, name
import subprocess as sp
wiki.set_lang("it")

def speak(text):
    engine = pyttsx3.init() # object creation

    """ RATE"""
    rate = engine.getProperty('rate')   # getting details of current speaking rate                     #printing current voice rate
    engine.setProperty('rate', 170)     # setting up new voice rate


    """VOLUME"""
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)                         #printing current volume level
    engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engine.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female
    print(text)
    engine.say(text)
    engine.runAndWait()

def start():
    tmp = sp.call('cls',shell=True)
    speak("Ciao io sono Serena e sono qui per aiutarti!")
    speak("Ecco alcune cose che puoi chiedermi:... Prova con il comando:... 'Serena cerca su wikipedia'")
    main()

def main():
    tmp = sp.call('cls',shell=True)
    a = str(input("Inserisci Comando: "))
    if (a.upper() == "SERENA CERCA SU WIKIPEDIA" or a.upper() == "CERCA SU WIKIPEDIA"):
        wikipedia_search()
    elif (a.upper() == "CHI SEI" or a.upper() == "CHI TI HA CREATO" or a.upper() == "PARLAMI DI TE" or a.upper() == "RACCONTAMI DI TE" or a.upper() == "CHI TI HA CREATO?" or a.upper() == "CHI SEI?"):
        about()
    elif (a.upper() == "CIAO" or a.upper() == "CIAO SERENA" or a.upper() == "CIAO SERE"):
            tmp = sp.call('cls',shell=True)
            speak("Ciao! :D")
            main()
    elif (a.upper() == "BUONGIORNO" or a.upper() == "BUONGIORNO SERENA" or a.upper() == "BUONGIORNO SERE"):
            tmp = sp.call('cls',shell=True)
            speak("Buongiorno :D")
            main()
    else:
        speak("Non ho capito, assicurati di aver scritto bene il messaggio!")
        main()

def wikipedia_search():
    tmp = sp.call('cls',shell=True)
    speak("Cosa devo cercare?")
    wikis = str(input("Cosa vuoi cercare su Wikipedia? "))
    try:
        wikipedia_found(wikis)
    except wiki.PageError(pageid=None, *args):
        speak("Non riesco a trovare quello che cerchi su Wikipedia...")
        speak("Vuoi cercare qualcos'altro?")
        b = str(input("Si/No ? "))
        if (b.upper() == "SI"):
            wikipedia_search()
        elif (b.upper() == "NO"):
            main()
        else:
            speak("Comando non valido, torno al menù!")
            main() ## TODO: # FIXME: ERROR FOR PAGE NOT FOUND NEEDS FIX

def wikipedia_found(wikisearch):
    tmp = sp.call('cls',shell=True)
    speak(wiki.summary(wikisearch, sentences=1, auto_suggest=True))
    speak("Vuoi cercare qualcos'altro?")
    b = str(input("Si/No ? "))
    if (b.upper() == "SI"):
        wikipedia_search()
    elif (b.upper() == "NO"):
        main()
    else:
        speak("Comando non valido, torno al menù!")
        main()
    main()

def about():
    tmp = sp.call('cls',shell=True)
    speak("Io Sono Serena e sono un intelligenza artificiale nata in Italia da Rasi Federico")
    main()

start()
