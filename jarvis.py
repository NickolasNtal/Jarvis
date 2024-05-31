import pyttsx3
import speech_recognition as sr
import datetime as dt
import wikipedia as wk
import webbrowser as wb
import os
import smtplib
import subprocess as sub
from playsound import playsound as sound
import urllib.parse
from customtkinter import *
from PIL import Image as IMG
import random
import jokes, settings



class AI:
    def __init__(self):
        self.speak("Tell me your name")
        user = self.takeCommand()
        self.codeName, self.name, self.age = settings.details(user)
        self.engine = pyttsx3.init("sapi5")
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty("voices", self.voices[0].id)
        self.root = CTk()
        h, x = 500, 500
        self.root.geometry(f"{h}x{x}")
        self.root.title("J.A.R.V.I.S.")
        self.root.iconbitmap("Images\\chip.ico")

    def changeImg(self):
        pass

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def wishMe(self):
        hour = int(dt.datetime.now().hour)
        if hour >= 0 and hour < 12:
            self.speak(f"Good Morning {self.name}")

        elif hour >= 12 and hour < 18:
            self.speak(f"Good Afternoon {self.name}")

        else:
            self.speak(f"Good Evening {self.name}")

        self.speak("How may I help you?")

    def takeCommand():
        r = sr.Recognizer()
        mic = sr.Microphone()

        with mic as source:
            #jarvisSpeech.config(text="Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            #jarvisSpeech.config(text="Recognizing")
            query = r.recognize_google(audio, language="en-in")

            #userSpeech.config(text=query)
            f = open("Scripts/UserQuests.txt", "a")
            f.write(f"{dt.datetime.now()} {query} \n")
            f.close()

        except Exception as e:
            #jarvisSpeech.config(text="Say that again please...")
            return "None"
        return query

    def sendEmail(to, content):
        server = smtplib.SMTP("smtp.gmail.com, 587")
        server.ehlo()
        server.starttls()
        server.login("nickolasdalianis@gmail.com", "password")
        server.sendmail("nickolasdalianis@gmai.com", to, content)
        server.close()

    def openOperaGX(url):
        operaGxPath = "C:\\Users\\nicko\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
        sub.Popen([operaGxPath, url])

    def searchOperaGX(searchTerm):
        base_url = "https://www.google.com/search?q="
        search_query = urllib.parse.quote(searchTerm)
        search_url = base_url + search_query
        opera_gx_path = "C:\\Users\\nicko\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
        sub.Popen([opera_gx_path, search_url])

    def giveDetUsers(self):
        self.speak("Give the name wou want me to have")
        codeName = self.takeCommand()
        self.speak("Give your name")
        name = self.takeCommand()
        self.speak("Give your age")
        age = self.takeCommand()
        settings.NewUser(codeName, name, age)


if __name__ == "__main__":
    AI = AI()
    img = IMG.open("`Images\\speaker.png`")
    imgLbl = CTkLabel(AI.root, image=CTkImage(light_image=img, dark_image=img)).pack()
    jarvisSpeech = CTkLabel(AI.root, text="").pack(side="bottom")
    userSpeech = CTkLabel(AI.root, text="").pack(side="bottom")
    AdInput = CTkEntry(AI.root).pack(side="bottom")

    AI.wishMe()
    while True:
        query = AI.takeCommand().lower()

    if "wikipedia" in query:
        #jarvisSpeech.config(text="Search Wikipedia")
        AI.speak("Search Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wk.summary(query, sentences = 2)
        #jarvisSpeech.config(text="According to wikipedia")
        AI.speak("According to wikipedia")
        #jarvisSpeech.config(text=results)
        AI.speak(results)

    elif "open on browser" in query:
        AI.speak("Opening...")
        if "youtube" in query:
            #jarvisSpeech.config(text="Opening YouTuBe")
            AI.speak("Youtube")
            openOperaGX("youtube.com")
        elif "facebook" in query:
            #jarvisSpeech.config(text="Opening FaceBook")
            AI.speak("Facebook")
            openOperaGX("facebook.com")
        elif "instagram" in query:
            #jarvisSpeech.config(text="Opening Instagram")
            AI.speak("Instagram")
            openOperaGX("instagram.com")
        elif "gmail" in query:
            #jarvisSpeech.config(text="Opening Gmail")
            AI.speak("Gmail")
            openOperaGX("gmail.com")
        elif "pinterest" in query:
            #jarvisSpeech.config(text="Opening Pinterest")
            AI.speak("Pinterest")
            openOperaGX("pinterest.com")
        elif "tiktok" in query:
            #jarvisSpeech.config(text="Opening TikTok")
            AI.speak("TikTok")
            openOperaGX("tiktok.com")
        elif "twitch" in query:
            #jarvisSpeech.config(text="Opening Twitch")
            AI.speak("Twitch")
            openOperaGX("twitch.com")

    elif "New tab" in query:
        #jarvisSpeech.config(text="Making New Tab")
        AI.speak("Making New Tab")
        if "search" in query:
            search = query[6:len(query)]
            searchOperaGX(search)

    elif "play music" in query:
        musicDir = "D:\\Users\\User\\Music"
        songs = os.listdir(musicDir)
        #jarvisSpeech.config(text=f"Playing {songs}")
        AI.speak(f"Playing {songs}")
        print(songs)
        os.startfile(os.path.join(musicDir, songs[0]))

    elif "the date" in query:
        strDate = dt.datetime.now().strftime("%Y-%m-%d")
        #jarvisSpeech.config(text=f"Sir, the date is {strDate}")
        AI.speak(f"Sir, the date is {strDate}")

    elif "the time" in query:
        strTime = dt.datetime.now().strftime("%H-%M-%S")
        #jarvisSpeech.config(text=f"Sir, the time is {strTime}")
        AI.speak(f"Sir, the time is {strTime}")

    elif "open VSCode" in query:
        pathCode = "D:\\Program Files\\VSCode-win32-x64-1.89.0\\Code.exe"
        #jarvisSpeech.config(text="Opening VSCode")
        AI.speak("Opening VSCode")
        os.startfile(pathCode)

    elif "email to" in query:
        try:
            AI.speak("What should I say?")
            content = AI.takeCommand()
            #jarvisSpeech.config(text="Type the email address to:")
            AI.speak("Type the email address to")
            to = AdInput.get()
            AI.sendEmail(to, content)
            AI.speak("Email has been sent!")
        except Exception as e:
            print(e)
            AI.speak("Sorry Sir. I am not able to sent this email")

    elif "open file" in query:
        file = query[9:len(query)]
        pathFile = "D:\\Users\\User\\Desktop\\" + file
        os.startfile(pathFile)

    elif "stop" in query:
        AI.speak("Goodbye Sir")
        print("Goodbye Sir")
        exit()

    elif "I feel unhappy" in query or "i feel sad" in query:
        AI.speak("Let me cheer you up... With, a, joke")
        AI.speak(jokes.joke)
        time.sleep(1.5)
        AI.speak(jokes.answer)

    elif "New user" in query:
        AI.speak("Setting new user...")
        settings.NewUser()

    elif "Change name" in query:
        AI.speak("Changing name...")
        settings.changeName(AI.takeCommand())

    elif "change code name" in query:
        AI.speak("Changing code name...")
        settings.changeCodeName(AI.takeCommand())    

    elif "change age" in query:           
        AI.speak("Changing age...")
        settings.changeAge(AI.takeCommand())

    elif "Add more details about me" in query:
        AI.speak("Adding more details about you...")
        uDone = AI.takeCommand()
        while "That's it" not in uDone or "Enough" not in uDone or "Stop" not in uDone or "stop" not in uDone:
            settings.addMore(uDone)
            uDone = AI.takeCommand()

    AI.mainloop()