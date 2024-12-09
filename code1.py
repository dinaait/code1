import speech_recognition as sr
from selenium import webdriver

class Voice:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.listenOnMic()

    def listenOnMic(self):
        while True:
            try:
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = self.recognizer.listen(source)
                    command = self.recognizer.recognize_google(audio).lower()
                    print(f"Command: {command}")
                    
                    if "search" in command:
                        search_query = command.split("search ", 1)[-1]
                        driver = webdriver.Chrome()
                        driver.get(f"https://www.google.com/search?q={search_query}")
                    
                    # Stop listening when 'stop' command is recognized
                    if "stop" in command:
                        print("Stopping the listening process.")
                        break  # This will break out of the while loop and stop listening
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print("Check your network connection please")

# Create an instance to start listening
listener = Voice()
