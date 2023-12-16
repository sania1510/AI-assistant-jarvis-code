import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set voice properties 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Index 0 is often a male voice

# Function to speak text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet the user
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    
# Function to take voice input
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold=1
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio,language='en-in').lower()
            print(f"User: {command}")
        except sr.UnknownValueError:
            print("Say that again please...")
            command = take_command()

    return command

# Main function to execute commands
def main():
    greet()
    speak("Hello I am jarvis . how may I help you today")

    while True:
        command = take_command()

        if 'wikipedia' in command:
            speak("Searching Wikipedia...")
            query = command.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in command:
            webbrowser.open("https://www.youtube.com")
            speak("opening youtube")

        elif 'open google' in command:
            webbrowser.open("https://www.google.com")
            speak("opening google")

        elif 'open stack overflow' in command:
            webbrowser.open("https://stackoverflow.com")
            speak("opening open stack overflow")

        elif 'open pinterest' in command:
            webbrowser.open("https://in.pinterest.com/")
            speak("opening pinterest")

        elif 'play music' in command:
            music_dir = "C:\\Users\\hp\\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")

        elif 'who are you' in command:
            speak('I am jarvis . A built in voice assistant by you')

        elif 'hello jarvis' in command:
            speak('hello wassup , how may i help you')

        elif 'busy'in command:
            speak('no,I am always free for u . Tell me what i have to do')

        elif 'open vs code' in command:
            path="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
            speak("opening vs code")

        elif 'ok bye jarvis' in command:
            speak("ok bye")
            break
        else:
            speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    main()
