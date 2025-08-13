#Robo Speaker
import win32com.client 
print(f"Welcome to the Robo Speaker version 1.1")
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.speak("Enter what you want me to speak: ")
while True:
    text = input("Enter the text: ").lower()
    if text == "stop":
        speaker.Speak("Bye Bye sir")  
        break
    speaker.Speak(text)