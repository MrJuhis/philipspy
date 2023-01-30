import cv2
import time
import numpy as np
import handtrackingmodule as htm
import math
from threading import Thread
import threading
from hue_api import HueApi

def StartTracking():
	global clamped
	clamped = 256


	wCam, hCam = 640, 480

	hue = HueApi()
	hue.load_existing("hue.txt")

	lights = hue.fetch_lights()
	hue.filter_lights(indices=[1])

	cap = cv2.VideoCapture(1)
	cap.set(3, wCam)
	cap.set(4, hCam)
	pTime = 0
	updateThreadRunning = 0
	exit_event = threading.Event()
	global Killed
	Killed = 0

	detector = htm.handDetector(detectionCon=0.8)

	def updateHueBright():
		counts = 121
		for x in range(counts):
			time.sleep(0.1)
			hue.set_brightness(clamped)
			print(clamped)
			if x == 120:
				exit_event.set()
				global Killed
				Killed = 1
				

	updateThread = Thread(target=updateHueBright)

	while True:
		if Killed == 1:
			break
			Killed = 0
		else:
			success, img = cap.read()
			img = detector.findHands(img)
			lmList = detector.findPosition(img, draw=False)
			if len(lmList) !=0:
				
				x1, y1 = lmList[4][1],lmList[4][2]
				x2, y2 = lmList[8][1],lmList[8][2]
				
				
				cv2.circle(img, (x1,y1), 15, (255,0,255), cv2.FILLED)
				cv2.circle(img, (x2,y2), 15, (255,0,255), cv2.FILLED)
				cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
				
				length = math.hypot(x2 - x1, y2 - y1)
				clamped = sorted((0, length, 256))[1]
				#print(clamped)
				if updateThreadRunning == 0:
					try:
						updateThread.start()
						updateThreadRunning = 1
					except (KeyboardInterrupt, SystemExit):
						break
			
			cv2.imshow("Img", img)
			cv2.waitKey(1)

		