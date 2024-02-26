import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

# Initialize the recognizer
listener = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Use the desired voice index

# Greet the user
engine.say("Greetings, how can I assist you today?")
engine.runAndWait()

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            print("You said:", command)

            if "who are you" in command:
                engine.say("I am your voice-controlled assistant.")
                engine.runAndWait()

            elif "play" in command:
                query = command.replace("play", "")
                pywhatkit.playonyt(query)
                engine.say("Playing " + query)
                engine.runAndWait()

            elif "time" in command:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                engine.say("The current time is " + current_time)
                engine.runAndWait()

            elif "find" in command:
                search_query = command.replace("find", "")
                search_result = wikipedia.summary(search_query, 1)
                engine.say(search_result)
                engine.runAndWait()

            elif "exit" in command:
                engine.say("Exiting the program. Goodbye!")
                engine.runAndWait()
                break

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except Exception as e:
        print("Something went wrong: ", str(e))
