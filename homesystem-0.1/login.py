#!/usr/bin/env python

from tkinter import *
import os
import sys
from PIL import Image
import json

#Zmienne globalne----------------------------

global loga
import Adafruit_DHT
fileon="lighton.gif"
fileoff="lightoff.gif"

temp = 0

imageOn="gateOpen.jpg"
imageOff="gateClose.jpg"

gateOn = 'getOn.py'
gateOf = 'getOff.py'

creds = 'tempfile.temp'
filem = 'ledOn.py'
filen = 'ledOff.py'
filem1='kitchenOn.py'
filen1='kitchenOff.py'


def signup():
    global pwordE
    global roots
    global nameE

    roots= Tk()
    roots.title("Signup")
    instruction = Label(roots, text='Please Enter new Credidentials\n')
    instruction.grid(row=0, column=0, sticky=E)

    nameL = Label(roots, text="New Username: ")
    pwordL = Label(roots, text="New Password: ")
    nameL.grid(row=1, column=0, sticky=W)
    pwordL.grid(row=2, column=0, sticky=W)

    nameE = Entry(roots)
    pwordE = Entry(roots, show='*')
    nameE.grid(row=1, column=1)
    pwordE.grid(row=2, column=1)

    buttonSignup = Button(roots, text="Signup", command=FSsignup)
    buttonSignup.grid(columnspan = 2, sticky=W)
    roots.mainloop()

def FSsignup():
    with open(creds, 'w') as f:
        f.write(nameE.get())
        f.write('\n')
        f.write(pwordE.get())
        f.close()

    roots.destroy()
    Login()

def Login():
    global pwordEL
    global nameEL
    global rootA
    global log
    global loga
    global photo
    global gateImg

    rootA= Tk()
    rootA.title('Login')
    


    titleL = Label(rootA, text='Home Systems\n', fg="green", font=(35))
    titleL.grid(row=0, columnspan=2)

    instruction = Label(rootA, text='Please login\n')
    instruction.grid(row=1, sticky=W)

    nameL= Label(rootA, text='Username: ')
    pwordL = Label(rootA, text='Password: ')
    nameL.grid(row=2, sticky=W)
    pwordL.grid(row=3, sticky=W)

    nameEL = Entry(rootA)
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=2, column=1)
    pwordEL.grid(row=3, column=1)

    loginB = Button(rootA, text='Login', command=Checklog)
    loginB.grid(columnspan=2, sticky=W)

    
    
    rmuser = Button(rootA, text="Delete User", command=Delusr)
    rmuser.grid(columnspan=2, sticky=W)

    quitB = Button(rootA, text="Quit",fg="red", command=QuitLog)
    quitB.grid(columnspan=2, sticky=W)

def Checklog():
    global log
    with open(creds) as f:
        data = f.readlines()
        usname = data[0].rstrip()
        pword = data[1].rstrip()

        if nameEL.get() == usname and pwordEL.get() == pword:
            rootA.destroy()
            Panel()
          
        else:
            log = Tk()
            log.title('False')
            log.geometry('150x50')
            rl = Label(log, text='\n[+] Invalid Login or Password')
            rl.pack()
            log.mainloop()


def Delusr():
    os.remove(creds)
    rootA.destroy()
    signup()

def Panel():
    global loga
    global photo
    loga= Tk()
    loga.title('Control Panel')
    loga.geometry('600x600+0+0')
    loga.configure(background='SteelBlue1')
    Tops = Frame(loga, width = 600 ,bg="SteelBlue1", relief=SUNKEN)
    Tops.pack(side=TOP)
    titleLog= Label(Tops, bg="SteelBlue1",font=('arial',50,'bold italic'), text="Home System", fg="snow", bd=10 , anchor='w')
    titleLog.grid(row=0, column=0, columnspan=2)
    photo = PhotoImage(file='lightoff1.gif')
    
    #Function of buttons
    def BedroomOn():
        global photo
        photo = PhotoImage(file="lighton.gif")
        labely.config(image=photo)
        exec(open(filem).read())
        
    def BedroomOf():
        global photo
        photo = PhotoImage(file="lightoff.gif")
        labely.config(image=photo)
        exec(open(filen).read())

    def KitchenOn():
        global img
        img= PhotoImage(file="lighton1.gif")
        labely1.config(image=img)
        exec(open(filem1).read())
        
    def KitchenOf():
        global img
        img= PhotoImage(file="lightoff1.gif")
        labely1.config(image=img)
        exec(open(filen1).read())

    def GateOn():
        global gateImg
        gateImg = PhotoImage(file="gateOpen.gif")
        gateLab.config(image=gateImg)#zmiana wstawionego zdjecia
        exec(open(gateOn).read())#wykonanie pliku

    def GateOff():
        global gateImg
        gateImg = PhotoImage(file="gateClose.gif")
        gateLab.config(image=gateImg)
        exec(open(gateOf).read())
    
    
    #Bedroom
    Room1= Frame(loga,bg="LightSkyBlue1", bd=1, relief=SUNKEN, width=240, height=200)
    Room1.pack(side=LEFT, fill='both',  pady=10, padx=10)
    Label(Room1, bg="LightSkyBlue1", text='Bedroom\n', font=(20)).grid(row=0, column=1, columnspan=2)

    
    photo = PhotoImage(file="lightoff.gif")
    labely = Label(Room1, image= photo)
    labely.grid(row=2, column=1, columnspan=2)
    
    Button(Room1, text='Light ON', command=BedroomOn, fg='green').grid(row=3,column=1)
    Button(Room1, text='Light OFF', command=BedroomOf, fg='red').grid(row=3, column=2)
    Label(Room1,bg="LightSkyBlue1", text=' \n').grid(row=4,columnspan=2)
    humidity, temperature = Adafruit_DHT.read_retry(22, 4)
    temp = "Temperature = %.1f*C" %(temperature)
    humi= "Humidity = %.1f "%(humidity)
    sensor1=Label(Room1, bg="LightSkyBlue1", text=str(temp), fg="black", font="24")
    sensor1.grid(row=5, column=1, columnspan=2)
    sensor2 = Label(Room1,bg="LightSkyBlue1",  text=str(humi),fg="black", font="24")
    sensor2.grid(row=6, column=1, columnspan=2)
    
    #Kitchen
    
    Kitchen= Frame(loga,bg="LightSkyBlue1", bd=1, relief=SUNKEN, width=240, height=200)
    Kitchen.pack(side=LEFT, fill='both',pady=10)
    Label(Kitchen, bg="LightSkyBlue1", text='Kitchen\n', font=(20)).grid(row=0, column=1, columnspan=2)

    global img
    img= PhotoImage(file='lightoff1.gif')
    labely1 = Label(Kitchen, image= img)
    labely1.grid(row=2, column=1, columnspan=2)
    
    Button(Kitchen, text='Light ON', command=KitchenOn, fg='green').grid(row=3,column=1)
    Button(Kitchen, text='Light OFF', command=KitchenOf, fg='red').grid(row=3, column=2)
    Label(Kitchen,bg="LightSkyBlue1", text=' \n').grid(row=4,columnspan=2)
    humidity, temperature = Adafruit_DHT.read_retry(22, 4)
    temp = "Temperature = %.1f*C" %(temperature)
    humi= "Humidity = %.1f "%(humidity)
    sensor3=Label(Kitchen, bg="LightSkyBlue1", text=str(temp), fg="black", font="24")
    sensor3.grid(row=5, column=1, columnspan=2)
    sensor4 = Label(Kitchen,bg="LightSkyBlue1",  text=str(humi),fg="black", font="24")
    sensor4.grid(row=6, column=1, columnspan=2)

    #Gate

    Gate= Frame(loga,bg="LightSkyBlue1", bd=1, relief=SUNKEN, width=240, height=200)
    Gate.pack(side=LEFT, fill='both',pady=10,padx=10)
    Label(Gate, bg="LightSkyBlue1", text='Gate\n', font=(20)).grid(row=0, column=1, columnspan=2)

    global gateImg
    gateImg= PhotoImage(file='gateClose.gif')
    gateLab= Label(Gate, image= gateImg)
    gateLab.grid(row=2, column=1, columnspan=2)

    Button(Gate, text='Open', command=GateOn, fg='green').grid(row=3,column=1, padx=5)
    Button(Gate, text='Close', command=GateOff, fg='red').grid(row=3, column=2, padx=5)

    def Sensor():
        global temp 
        humidity, temperature = Adafruit_DHT.read_retry(22, 4)
        temp = "Temperature = %.1f*C" %(temperature)
        humi= "Humidity = %.1f "%(humidity)
        sensor1.config(text=str(temp))
        sensor2.config(text=str(humi))
        sensor3.config(text=str(temp))
        sensor4.config(text=str(humi))
        loga.after(3000,Sensor)
                         
    loga.after(3000,Sensor)       
    loga.mainloop()


def QuitLog():
    rootA.destroy()
    loga.destroy()
    exec(open(filen).read())
    

if os.path.isfile(creds):
    Login()
else:
    signup()


    
