import openai
import speech_recognition as sr
import pyttsx3

# OpenAI API key
api_key = ""

# Initialize the OpenAI API client
openai.api_key = api_key

# Initialize the recognizer
listener = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # Use the desired voice index

# Function to create chatbot response
def create_ghost_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are your personal AI assistant named Ghost."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]

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

            # Pass the voice command to the chatbot
            response = create_ghost_response(command)

            # Speak the response using text-to-speech
            engine.say(response)
            engine.runAndWait()

            if "exit" in command:
                engine.say("Exiting the program. Goodbye!")
                engine.runAndWait()
                break

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except Exception as e:
        print("Something went wrong: ", str(e))
