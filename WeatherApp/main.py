import requests
import json
import win32com.client as wincom
import time

speak = wincom.Dispatch("SAPI.SpVoice")
while True:
    city = input("Enter city name : ")

    if city == "q":
        speak.Speak("Bye bye friends")
        break

    url = f"https://api.weatherapi.com/v1/current.json?key=62e8fca7fd45408db87142136231804&q={city}"

    r = requests.get(url)
    wdict = json.loads(r.text)
    temp = wdict["current"]["temp_c"]
    stat = wdict["location"]["region"]
    ctry = wdict["location"]["country"]
    windspeed = wdict["current"]["wind_kph"]
    humidity = wdict["current"]["humidity"]
    fl = wdict["current"]["feelslike_c"]

    print(temp, "degrees")
    say = f"Current wather in {city} {stat} {ctry} is {temp} degrees"
    speak.Speak(say)
    time.sleep(0.5)

    print(windspeed, "km/h")
    say = f"The wind is blowing at {windspeed} kilometer per hour"
    speak.Speak(say)
    time.sleep(0.5)

    print(humidity,"%")
    say = f"humidity is {humidity} percent"
    speak.Speak(say)
    time.sleep(0.5)

    print(fl, "degrees")
    say = f"It feels like {fl} degrees"
    speak.Speak(say)
