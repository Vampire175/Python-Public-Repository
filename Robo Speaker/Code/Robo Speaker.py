import win32com.client
from gtts import gTTS
import os
print('Made by Arjun Fanibahre')
while True:
    a = input("1) Male Voice\n2) Female Voice\nEnter the number (type 'exit' to close): ")
    if a.lower() == "exit":
        
        break
    
    b = input('What do you want to speak (type "exit" to close): ')
    if b.lower() == "exit":
        
        break

    if a == "1":
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(b)
    elif a == "2":
        speech = gTTS(b)
        speech.save('audio.mp3')
        os.system('start audio.mp3')
    else:
        print("Invalid option. Please choose 1 for Male Voice or 2 for Female Voice.")

