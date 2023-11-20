

#Importing The necessary modules

import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia
listner=aa.Recognizer()
machine= pyttsx3.init()

def talk(text):
    machine.say(text)

    machine.runAndWait()
def input_instruction():

    try:
        with aa.Microphone(device_index = 0) as source:
            print("Listening: ")
            print(aa.Microphone.list_microphone_names())
            listner.adjust_for_ambient_noise(source)
            audio=listner.listen(source,timeout=5)

        instruction=listner.recognize_google(audio)
        instruction=instruction.lower()

        if "eirene" in instruction:
            instruction=instruction.replace("eirene","")
            print(instruction)

        return instruction

    except aa.WaitTimeoutError:
        print("Time Out Waiting for Speedch input")
    except aa.UnknownValueError:
        print("Unable to recognize speech")
    except aa.RequestError as e:
        print("Error in request to speech recognition service {0}".format(e))



def talk_eirene():
    instruction=input_instruction()
    print(instruction)
    if "play" in instruction:
        song=str(instruction).replace('play','')
        talk("playing"+song)

        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        time=datetime.datetime.now().strftime('%I: %M%p')
        talk('Current time'+time)

    elif  'date' in instruction:
        date=datetime.datetime.now().strftime('%d /%m/%Y')

        talk("Today's date: "+ date )

    elif 'how are you' in instruction:
        talk("I'm Fine how about you!")

    elif "who created you" in instruction:
        print ( "I'm Created by Alex Christian MY Majesty, I'm Created by Him, his personal assitant!" )
        talk("I'm Created by Alex Christian MY Majesty, I'm Created by Him, his personal assitant!")


    elif "tell me about yourself" in instruction:
        print ("I'm Eeriene Which means hope it is a hebrew word taken from bible. And Alex Gave me name Eeirene which means hope"
            "My speciality is I can start a youtube videos, I can represent you any wikipedia information you ask." )

        talk("I'm Eeriene Which means hope it is a hebrew word taken from bible. And Alex Gave me name Eeirene which means hope. My speciality is I can start a youtube videos, I can represent you any wikipedia information you ask.")

    elif 'who is' or 'which is' or 'How is' or'why is' in instruction:
        human=instruction.replace('who is','')
        info=wikipedia.summary(human, 1)
        print(info)
        talk(info)
    else:
        talk("Can you repeat once again, I didn't hear properly")

talk_eirene()