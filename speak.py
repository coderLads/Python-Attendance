import pyttsx
import sys

speaktext = " "

for i in range(1,len(sys.argv)):
	speaktext = speaktext + " " + sys.argv[i]
	
engine = pyttsx.init()
engine.setProperty('voice', 1)
engine.say(speaktext)
engine.runAndWait()
