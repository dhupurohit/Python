import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")
print("Welcome to robo speaker.\nIt was created by Dhruvita.\n")
while True:
    a = input("Enter what you want to say : ")
    # a = "Hello how are you i am fine"
    if a == "bye":
        speak.Speak("Bye bye friends")
        break
    text = a
    speak.Speak(text)
