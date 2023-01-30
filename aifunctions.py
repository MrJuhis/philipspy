import pyttsx3 as tts
from hue_api import HueApi
from pylips import pylips
import subprocess
import gesturevolume
from threading import Thread
from youtubesearchpython import VideosSearch

##### HUE

hue = HueApi()
hue.load_existing("hue.txt")

lights = hue.fetch_lights()
#####

speaker = tts.init()
speaker.setProperty('rate', 150)
voices = speaker.getProperty("voices")
speaker.setProperty('voice', voices[0].id)

def greetingsfunc():
	global recognizer
	
	speaker.say("Hello Juha!")
	speaker.runAndWait()

def exitingfunc():
	global recognizer
	speaker.say("Not gonna miss you Juha. Just a joke. Have fun.")
	speaker.runAndWait()
	
def swearingfunc():
	global recognizer
	
	speaker.say("Yeah fuck you too.")
	speaker.runAndWait()

def togglelightfunc():
	global recognizer
	
	speaker.say("Toggling your room lights.")
	hue.toggle_on(indices=[1])
	speaker.runAndWait()

def adjustlightsfunc():
	global recognizer
	speaker.say("Here you go. Adjust your lights.")
	speaker.runAndWait()
	gesturevolume.StartTracking()
	speaker.say("Lights adjusted.")
	speaker.runAndWait()
	
def togglefanfunc():
	global recognizer
	
	speaker.say("Toggling your fan.")
	hue.toggle_on(indices=[8])
	speaker.runAndWait()	
	
def toggletvfunc():
	global recognizer
	
	subprocess.call("python3 pylips/pylips.py --command standby")
	speaker.say("Toggling your TV.")
	speaker.runAndWait()	

def tv_volumedown():
	global recognizer

	subprocess.call("python3 pylips/pylips.py --command volume_down")
	speaker.say("Toggling TV's volume down.")
	speaker.runAndWait()	

def tv_volumeup():
	global recognizer

	subprocess.call("python3 pylips/pylips.py --command volume_up")
	speaker.say("Toggling TV's volume up.")
	speaker.runAndWait()		