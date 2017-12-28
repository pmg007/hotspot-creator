from tkinter import *
from os import system as cmd



a=Tk()
a.title("Hotspot Creator")
def initialize():
	hotspotname = e1.get()
	if e2.get()==e3.get():
		password=e2.get()
		cmd('netsh wlan set hostednetwork mode=allow ssid={} key={}'.format(hotspotname,password))
		cmd('netsh wlan start hostednetwork')
	else:
		'None'

def stop():
	cmd('netsh wlan stop hostednetwork')


Label(a,text="Enter Details:").grid(row=0)
Label(a,text="enter SSID(i.e. hotspot's name):").grid(row=1)
Label(a,text="Password:").grid(row=2)
Label(a,text="Confirm Password:").grid(row=3)
e1=Entry(a)
e2=Entry(a,show="*")
e3=Entry(a,show="*")
e1.grid(row=1,column=1)
e2.grid(row=2,column=1)
e3.grid(row=3,column=1)
button1 = Button(a,text="Initialize",command=initialize).grid(row=4, column=0)
button2 = Button(a,text="Stop",command=stop).grid(row=4,column=1)
a.mainloop()