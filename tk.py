from Tkinter import *
import os

#attendance.py Integrity! Offsite 11:30 Pings 40 50 17

master = Tk()

status = Entry(master)
status.pack()
returntime = Entry(master)
returntime.pack()
info = Entry(master)
info.pack()
studentname = Entry(master)
studentname.pack()

def callback():
	output = str(status.get()) + " " + str(returntime.get()) + " " + str(info.get()) + " " + str(studentname.get())
	print(output)
	os.system("speak.py " + "'I think you said'" + output)
	os.system("attendance.py " + "Bravery! " + output)
	master.destroy()

b = Button(master, text="Submit", width=10, command=callback)
b.pack()

mainloop()
status = Entry(master, width=50)
status.pack()