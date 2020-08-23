# Voice To Text Converter Online
# Author: Raagul26
# Now Available in 6 languages
import speech_recognition as sr
import os
from time import sleep


# Function for small animation
def anim():
    print(" Please wait", end="")
    for i in range(5):
        sleep(0.5)
        print(".", end=" ")


# Function to clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Speech to text function
def speech(lang):
    try:
        with sr.Microphone() as source:
            print("\n Speak Anything :")
            audio = r.listen(source)
            r.adjust_for_ambient_noise(source)  # Removes noise
            try:
                anim()
                text = r.recognize_google(audio, language=lang)
                print("\n Audio: ", text)
                i = input("\n Do you want to save it in a file?(Y/N)")
                if i == "y" or i == "Y":
                    path = input(" Where to save the file (eg. rec.txt)?  ")
                    while os.path.exists(path):
                        print(" File already exists")
                        path = input(" Enter a new file: ")
                    else:
                        with open(path, "wb") as f:  # Stores as binary
                            f.write(text.encode('utf-8'))  # Encode the text to utf-8 format and then writes
                        print(" Text is saved in a file for your reference.")
            except UnicodeEncodeError:
                print(" Format not support")
            except sr.UnknownValueError:
                print("\n ***Audio Not Clear***\n")
            except sr.RequestError:
                print("\n ***Please Check Your Internet Connection***")
    except:
        print(" Turn on microphone access!!!")


# Audio to text function
def Audio(au):
    try:
        with sr.AudioFile(au) as source:
            audio = r1.record(source)
            try:
                anim()
                text = r1.recognize_google(audio)
                print("\n Audio: ", text)
                i = input("\n Do you want to save it in a file?(Y/N)")
                if i == "y" or i == "Y":
                    path = input(" Where to save the file (eg. rec.txt)?  ")
                    while os.path.exists(path):
                        print(" File already exists")
                        path = input(" Enter a new file: ")
                    else:
                        with open(path, "wb") as f:  # Stores as binary
                            f.write(text.encode('utf-8'))  # Encode the text to utf-8 format and then writes
                        print(" Text is saved in a file for your reference.")
            except UnicodeEncodeError:
                print(" Format not support")
            except sr.UnknownValueError:
                print("\n ***Audio Not Clear***\n")
            except sr.RequestError:
                print("\n ***Please Check Your Internet Connection***")
    except:
        print(' Plz enter a valid file name and extension')


# Function to implement speech to text
def speech_text():
    global r
    r = sr.Recognizer()
    print('''
      ____                       _       _____       _____         _   
     / ___| _ __   ___  ___  ___| |__   |_   _|__   |_   _|____  _| |_ 
     \___ \| '_ \ / _ \/ _ \/ __| '_ \    | |/ _ \    | |/ _ \ \/ / __|
      ___) | |_) |  __/  __/ (__| | | |   | | (_) |   | |  __/>  <| |_ 
     |____/| .__/ \___|\___|\___|_| |_|   |_|\___/    |_|\___/_/\_\\__|
           |_|                                                         
    ''')
    print("\n 1. Tamil\n 2. English\n 3. Malayalam\n 4. Telugu\n 5. Hindi\n 6. Kannada\n")
    choice = input("\n Choose Your Language: ")

    if choice == '1':
        speech(lang='ta-in')

    if choice == '2':
        speech(lang='en-in')

    if choice == '3':
        speech(lang='ml-in')

    if choice == '4':
        speech(lang='te-in')

    if choice == '5':
        speech(lang='hi-in')

    if choice == '6':
        speech(lang='kn-in')

    cont = input("\n Press enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to implement audio to text
def audio_text():
    global r1
    r1 = sr.Recognizer()
    print('''
         _             _ _         _____       _____         _   
        / \  _   _  __| (_) ___   |_   _|__   |_   _|____  _| |_ 
       / _ \| | | |/ _` | |/ _ \    | |/ _ \    | |/ _ \ \/ / __|
      / ___ \ |_| | (_| | | (_) |   | | (_) |   | |  __/>  <| |_ 
     /_/   \_\__,_|\__,_|_|\___/    |_|\___/    |_|\___/_/\_\\__|
    ''')
    au = input("\n Enter Audio file path: ")
    Audio(au)
    cont = input("\n Press enter to continue...")
    clear()


# Main function of program
def main():
    while True:
        print()
        print('''
    ██    ██  ██████        ████████ ███████ ██   ██
    ██    ██ ██    ██          ██    ██       ██ ██
    ██    ██ ██    ██  █████   ██    █████     ███ 
     ██  ██  ██    ██          ██    ██       ██ ██ 
      ████    ██████           ██    ███████ ██   ██                   
         
         Simple Online Voice To Text Converter''')
        print("\n 1.Voice(mic)\n 2.Audio File\n 3.Exit")
        ch = input("\n Enter your choice: ")
        if ch == '1':
            clear()
            speech_text()
        if ch == '2':
            clear()
            audio_text()
        if ch == '3':
            print(" ### Come back again ###")
            exit(0)


# Invoke main function
main()
