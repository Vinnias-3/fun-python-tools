import pyttsx3
engine=pyttsx3.init()
msg=input("enter text to speak:")
speed=int(input("speed (100-300):"))

engine.setProperty("rate",speed)
engine.say(msg)
engine.runAndWait()