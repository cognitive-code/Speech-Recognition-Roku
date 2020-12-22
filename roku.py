from roku import Roku
import os
import speech_recognition as sr

voice = sr.Recognizer()

roku = Roku('') # insert IP here

home = ["go home", "home", "go to homescreen"]
right = ["move right", "right", "go right"]
left = ["go left", "left", "move left"]
select = ["enter", "select", "choose app"]
up = ["move up", "up", "go up"]
down = ["go down", "down", "move down"]

while True:
    with sr.Microphone() as source:
        audio = voice.listen(source)
        try:
            x = voice.recognize_google(audio)
            if x in home:
                roku.home()
            elif x in right:
                roku.right()
            elif x in left:
                roku.left()
            elif x in select:
                roku.select()
            elif x in up:
                roku.up()
            elif x in down:
                roku.down()

        except sr.UnknownValueError:
            os.system("espeak  'Sorry  I didnt hear you'")
