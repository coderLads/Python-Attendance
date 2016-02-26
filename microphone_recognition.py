import speech_recognition as sr
import os
import sys

r = sr.Recognizer()
r.energy_threshold = 600
r.pause_threshold = 0.8
r.dynamic_energy_threshold = True
#while true:
with sr.Microphone(device_index = None, sample_rate = 16000, chunk_size = 1024) as source:
    print("Say something!")
    audio = r.listen(source)
try:
	output = r.recognize_google(audio)
	print("I think you said: " + r.recognize_google(audio))
	outputstr = "I think you said"
	os.system("speak.py " + "'I think you said'" + output)
except sr.UnknownValueError:
	print("I don't know what that was, please try again")
	os.system("speak.py " + "'I don't know what that was, please try again'")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
	
#os.system("attendance.py " + "Bravery! " + output)
#os.system('speak.py + "'output'"')
os.system("nl.py " + output)