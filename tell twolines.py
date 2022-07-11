import pyttsx3
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',170)
engine.setProperty('volume',8.0)

def speak(string):
    engine.say(string);
    engine.runAndWait();


lines=''' Hello,I am a speaker I want to tell about our {country}.
             Our {country} is the best. '''
def speakandprintlines():
    dictionary=dict()
    addKeywithvalue('country',dictionary)
    finallines=lines.format(**dictionary)
    print(finallines)
    speak(finallines)

def addKeywithvalue(key,dictionary):
    pok="Enter the  name of : "+key+" : "
    value=input(pok).strip()
    dictionary[key]=value

speakandprintlines()