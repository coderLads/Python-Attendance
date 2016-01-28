import Tkinter
import Image 
import ImageTk
from Tkinter import Tk
from Tkinter import *
import os

#attendance.py Integrity! Offsite 11:30 Pings 40 50 17

master = Tk()
master.title("PyAttendance Gui")

master.minsize(width=300, height=100)
master.maxsize(width=1000, height=1000)

canvas = Canvas(width = 300, height = 100)
canvas.pack(expand = YES, fill = BOTH)
image = ImageTk.PhotoImage(file = "logo.gif")
canvas.create_image(20, 5, image = image, anchor = NW)

StatusLabel = Label(canvas, text="Status Name:")
StatusLabel.grid(row=0,column=0)
StatusLabel.pack()

status = Entry(canvas)
status.grid(row=0,column=1)
status.pack()

ReturnLabel = Label(canvas, text="Return Time:")
ReturnLabel.grid(row=1,column=0)
ReturnLabel.pack()

returntime = Entry(canvas)
returntime.grid(row=1,column=1)
returntime.pack()

InfoLabel = Label(canvas, text="Other Info:")
InfoLabel.grid(row=2,column=0)
InfoLabel.pack()

info = Entry(canvas)
info.grid(row=2,column=1)
info.pack()

NameLabel = Label(canvas, text="Student Name:")
NameLabel.grid(row=3,column=0)
NameLabel.pack()

studentname = Entry(canvas)
studentname.grid(row=3,column=1)
studentname.pack()

def callback():
	output = str(status.get()) + " " + str(returntime.get()) + " " + str(info.get()) + " " + str(studentname.get())
	print(output)
	os.system("speak.py " + "'I think you said'" + output)
	os.system("attendance.py " + "Bravery! " + output)
	master.destroy()

b = Button(canvas, text="Go!", width=10, command=callback)
b.pack(pady=10)

mainloop()