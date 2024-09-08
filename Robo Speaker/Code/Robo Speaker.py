import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True:
    a = input('What do you want to speak (type "exit" to close): ')
    if a.lower() == "exit":
        print("Exiting the program.\nMade by Vampire with ❤️")
        break
    speaker.Speak(a)
