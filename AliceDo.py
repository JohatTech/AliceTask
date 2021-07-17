import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import requests
from PyDictionary import PyDictionary
from pynput.keyboard import Controller as key_controller
import random
import string
import sys
#help create the GUI
import tkinter as tk
#pick the apps
from  tkinter import filedialog, Text

def take_command():
    # initializing speech_recognition
    r = sr.Recognizer()
    # opening physical microphone of computer
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        print('Listening')
        r.pause_threshold = 0.9
        # storing audio/sound to audio variable
        audio = r.listen(source)
        try:
            print("Recognizing")
            # Recognizing audio using google api
            query = r.recognize_google(audio)
        except Exception as e:
            print(e)
            print("Say that again sir")
            # returning none if there are errors
            return "None"
    # returning audio as text
    import time
    time.sleep(0.1)
    return query

    # this part is for hold exception if the machine can't listening

#function for speak using the getter method of pyttsx3
def speak(audio):
    engine = pyttsx3.init()
    # getter method(gets the current value
    # of engine property)
    voices = engine.getProperty('voices')

    # setter method .[0]=male voice and
    # [1]=female voice in set Property.
    engine.setProperty('voice', voices[0].id)

    # Method for the speaking of the the assistant
    engine.say(audio)

    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()
def your_password():
    window = tk.Tk()
    # function for ccreate the password
    def password():
        Password_length = 18
        Password_character = string.digits + string.ascii_letters + string.punctuation
        Password_character = list(Password_character)
        password1 = random.choices(Password_character, k=Password_length)
        password1 = ''.join(password1)
        return password1
        print(password1)
    # function for print the password
    entry_password = tk.Entry(window, text='', font=("helvetica", 24))
    entry_password.pack()
    def get_password():
        print(password())
        entry_password.insert(0, password())
        # function for copy the password
    def copy_button():
        window.clipboard_clear()
        window.clipboard_append(password())
    button2 = tk.Button(window, text="copy", command=copy_button)
    button2.pack()
    window.mainloop()
#function for tell the day
def tellTime_day():
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1
    x = datetime.datetime.now()
    # this line tells us about the number
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    # This method will give the time
    time = str(datetime.datetime.now())
    # the time will be displayed like
    # this "2020-06-05 17:50:14.582630"
    # nd then after slicing we can get time
    print(time)
    hour = time[11:13]
    min = time[14:16]
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("Today is " + day_of_the_week + x.strftime("%d")+"of" + x.strftime("%B") + "of " + x.strftime("%y"))
#function for sutdown the computer
def shutdown():
    speak("do you want to shutdown the computer doctor")
    answer = take_command().lower()
    if "yes" in answer:
        os.system("shutdown/s/t 1")
#give the definition of a word asked
def definition():
    dictionary = PyDictionary()
    speak("give me the word")
    take_command()
    word = take_command().lower()
    meaning = dictionary.meaning(word)
    speak(meaning)
#function for say good morning
def Hello():
    #take the current hour and convert to a integer to compare more easy in the if statements
    current_hour = int(datetime.datetime.now().strftime('%H'))
    if current_hour < 12:
        speak('Good morning, doc what do you want to do')
    if 12 <= current_hour < 18:
        speak('Good afternoon, doc what do you want to do')
    if 18 <=current_hour:
        speak('Good Evening, doc what do you want to do')

#function for open the browser
def open_browser():
    webbrowser.open('https://www.youtube.com/')
#this function give us the weather
def give_weather():
    weather_key = os.environ["Weather"]
    # location from user
    location = 'panama'
    # URL
    api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + weather_key
    # HTTP request
    r = requests.get(api_link)
    # convert the data in 'r' into dictionary
    data = r.json()
    if (data["cod"] == "404"):
        print(f"Invalid city: {location}\nEnter valid city")
        exit()
    else:
        temp = data["main"]["temp"]
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        speed = data["wind"]["speed"]
        descr = data["weather"][0]["description"]
    speak(f"  Scenerio : {descr}")
    speak(f"  Temperature : {temp}")
    speak(f"  Pressure : {pressure}")
    speak(f"  Speed : {speed}")
def aliceDo():
    activation = take_command().lower()
    if "alice wake up" in activation:
        while(True):
            Hello()
            question = take_command().lower()
            if "tell me the day" in question:
                tellTime_day()
            elif "open youtube" in question:
                open_browser()
            elif "give me the weather" in question:
                give_weather()
            elif "give me a password" in question:
                your_password()
            elif "definiton" in question:
                definition()
            elif "shutdown the computer" in question:
                shutdown()
            elif "create agenda" in question:
                typer()
            elif "it's over " in question:
                exit()
keyboard = key_controller()
def typer():
    while(True):
        words = take_command().lower()
        for x in words:
            keyboard.type(x)
aliceDo()