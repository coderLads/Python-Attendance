# Python-Attendance
Library for using the pscs attendance system via python and via microphone

#Requires:#
Python 2.7+
fuzzywuzzy
speechrecongnition
selenium
pyttyx
pywin32

#Files include:#
attendance.py - uses command line arguments to open a selenium browser instance and sign people in and out.
gui.py - A simple python UI that uses attendance.py
nl.py - Converts a full sentence to passable command line arguments for attendance.py
speak.py - Speaks any string passed to it as command line arguments.
microphone_recognition.py - Recognises what is spoken, and passes that to nl.py

Right now, you can either use the GUI, or you can run microphone_recognition.py and speak a sentence.
For example:
*Milo is going offsite to Eastern Cafe and will be back at 2:30*
Make sure that all important words are included in your sentence, including status, student names, and any additional information that might be required.

You also may call attendance.py using the command line.
For example:
*attendance.py Integrity! Offsite 11:30 Pings Milo*