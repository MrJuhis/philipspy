from neuralintents import GenericAssistant
import speech_recognition
import sys
import aifunctions

recognizer = speech_recognition.Recognizer()

##### FUNCTIONS	

mappings = {
	'greeting': aifunctions.greetingsfunc,
	'exiting': aifunctions.exitingfunc,
	'swearing': aifunctions.swearingfunc,
	'togglelights': aifunctions.togglelightfunc,
	'adjustlights': aifunctions.adjustlightsfunc,
	'togglefan': aifunctions.togglefanfunc,
	'toggletv': aifunctions.toggletvfunc,
	'tv_tv_volumedown': aifunctions.tv_volumedown,
	'tv_tv_volumeup': aifunctions.tv_volumeup
}

###


assistant = GenericAssistant('intents.json', intent_methods=mappings)
#assistant.train_model()
#assistant.save_model()
assistant.load_model("assistant_model")

while True:

	try:
		with speech_recognition.Microphone() as mic:
		
			recognizer.adjust_for_ambient_noise(mic, duration=0.2)
			audio = recognizer.listen(mic)
			
			message = recognizer.recognize_google(audio)
			message = message.lower()
			
		assistant.request(message)
	except speech_recognition.UnknownValueError:
		recognizer = speech_recognition.Recognizer()