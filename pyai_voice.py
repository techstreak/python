#pip install pyttsx3
#pip install SpeechRecognition

# Import the required libraries
import speech_recognition as sr
import pyttsx3

# Initialize the SpeechRecognizer and Text-to-Speech engine
r = sr.Recognizer()  # SpeechRecognizer object for speech recognition
e = pyttsx3.init()   # Text-to-Speech engine for converting text to speech

# Adjust the speaking rate of the Text-to-Speech engine
rate = e.getProperty('rate')
e.setProperty('rate', rate - 30)  # Reduce the speaking rate by 30%

# Function to convert text to speech
def SpeakText(text):
    e.say(text)     # Feed the text to the Text-to-Speech engine
    e.runAndWait()  # Wait for the speech to finish before proceeding

# Infinite loop for the program to listen for user input continuously
while True:
    try:
        print("Listening...")  # Indicate that the program is listening for user input

        # Use the microphone as the source for audio input
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)  # Adjust for ambient noise

            # Listen for user input and set a timeout of 1 second
            audio = r.listen(source, timeout=1)
            print("Recognizing...")  # Indicate that the program is recognizing speech

            # Use Google's Speech Recognition to convert audio to text
            user_input = r.recognize_google(audio).lower()

            print("You said:", user_input)  # Print the recognized user input
            SpeakText(user_input)  # Speak back the user input

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occurred")
