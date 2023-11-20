import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

r = sr.Recognizer()

machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def get_instruction():
    try:
        with sr.Microphone(device_index=0) as source:
            print("listening")
            print(sr.Microphone.list_microphone_names())
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=5)
        instruction = r.recognize_google(audio)
        instruction = instruction.lower()
        if "jarvis" in instruction:
            instruction = instruction.replace('jarvis', "")
            print(instruction)
        return instruction
    except sr.WaitTimeoutError:
        print("Timeout waiting for speech input")
    except sr.UnknownValueError:
        print("Unable to recognize speech")
    except sr.RequestError as e:
        print("Error in request to speech recognition service; {0}".format(e))

def play_instruction():
    instruction = get_instruction()
    print(instruction)
    if instruction is not None and "play" in instruction:
        song = instruction.replace('play', "")
        talk("playing " + song)
        pywhatkit.playonyt(song)
    elif instruction is not None and 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time ' +  time)

play_instruction()