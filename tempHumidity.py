#use with arduino program temperature_DH11.io
#DHT 11 black wire = pin A2
#DHT 11 white wire = 5V
#DHT 11 black wire = ground
#this homework is for Paul McWhorter's Using an Ardinuo with Python Lesson 7
#https://www.youtube.com/watch?v=kF6biceKwFY

import numpy as np                                      #import numpy library
import time                                             #import time library
import serial                                           #import serial library
from vpython import *                                   #import vpython library

tempF=0
humidity=0
boxX=2.55                                               #box width
boxY=1.55                                               #box height
boxZ=.1                                                 #box depth
textT='Temperature = '
textH='Humidity = '



arduinoData=serial.Serial('/dev/cu.usbmodem14201',115200)   #set port and baud
time.sleep(1)                                               #pause 1 second

#create box edges

#thermometer box edge
myCase=box(color=color.white,                           #color
    size=vector(boxX,boxY,boxZ),                        #size
    pos=vector(0,boxY/1.5-.02,-boxZ))                   #position
#humidity box edge
myCase=box(color=color.white,                           #color
    size=vector(boxX,boxY,boxZ),                        #size
    pos=vector(0,(boxY/1.5-.02)-2,-boxZ))               #position

#create boxes
boxX=2.5                                                #box width
boxY=1.5                                                #box height
boxZ=.1                                                 #box depth
#thermometer box
myCase=box(size=vector(boxX,boxY,boxZ),                 #box size
    pos=vector(0,boxY/1.5,-boxZ),                       #box position
    texture=textures.metal)                             #box texture
#humidity box
myCase=box(size=vector(boxX,boxY,boxZ),                 #box size
    pos=vector(0,(boxY/1.5)-2,-boxZ),                   #box position
    texture=textures.metal),                            #box texture



#set up arrow hub objects
hubL=.02                                                #hub length
hubR=.05                                                #hub radius
#thermometer hub
myhub=cylinder(color=color.red,                         #create arrow hub
    radius=hubR,
    length=hubL,
    pos=vector(0,.5,0),
    axis=vector(0,0,1))                                 #rotate in z
#humidity hub
myhub=cylinder(color=color.red,                         #create arrow hub
    radius=hubR,
    length=hubL,
    pos=vector(0,-1.5,0),
    axis=vector(0,0,1))                                 #rotate in z

#set up arrow objects
arrowLength=1                                           #arrow length
arrowWidth=.02                                          #arrow width
#thermometer arrow
tempArrow=arrow(pos=vector(0,.5,0),                     #arrow position
    Length=arrowLength,                                 #create arrow
    shaftwidth=arrowWidth,
    color=color.red,                                    #color
    round=True)                                         #make arrow round instead of square
#humidity arrow
humidArrow=arrow(pos=vector(0,-1.5,0),                  #arrow position
    Length=arrowLength,                                 #create arrow
    shaftwidth=arrowWidth,
    color=color.red,                                    #color
    round=True)                                         #make arrow round instead of square

##set up ticks
tickStart = 5*np.pi/6                                   #tick starting position = 5pi/6
tickEnd = np.pi/6                                       #tick ending position = pi/6
tickL=.1                                                #tick length
tickW=.01                                               #tick width
tickH=.01                                               #tick height

#thermometer major ticks
for theta in np.linspace(tickStart, tickEnd, 11):       #create 6 major ticks (0-10)
    tickMajor = box(color=color.black,                  #color
        pos=vector(arrowLength*np.cos(theta),           #position
        arrowLength*np.sin(theta)+.5,0),                   
        size=vector(tickL,tickW,tickH),                 #size
        axis=vector(arrowLength*np.cos(theta),          #direction
        arrowLength*np.sin(theta),0))                   
#thermometer minor ticks
for theta in np.linspace(tickStart, tickEnd, 51):       #create 26 minor ticks (0-100)
    tickMajor = box(color=color.black,                  #color
        pos=vector(arrowLength*np.cos(theta),           #position
        arrowLength*np.sin(theta)+.5,0),
        size=vector(tickL/2,tickW/2,tickH/2),           #size
        axis=vector(arrowLength*np.cos(theta),          #direction
        arrowLength*np.sin(theta),0))
#humidity major ticks
for theta in np.linspace(tickStart, tickEnd, 11):       #create 6 major ticks (0-10)
    tickMajor = box(color=color.black,                  #color
        pos=vector(arrowLength*np.cos(theta),           #position
        arrowLength*np.sin(theta)-1.5,0),                   
        size=vector(tickL,tickW,tickH),                 #size
        axis=vector(arrowLength*np.cos(theta),          #direction
        arrowLength*np.sin(theta),0))
#humidity minor ticks
for theta in np.linspace(tickStart, tickEnd, 51):       #create 26 minor ticks (0-100)
    tickMajor = box(color=color.black,                  #color
        pos=vector(arrowLength*np.cos(theta),           #position
        arrowLength*np.sin(theta)-1.5,0),
        size=vector(tickL/2,tickW/2,tickH/2),           #size
        axis=vector(arrowLength*np.cos(theta),          #direction
        arrowLength*np.sin(theta),0))   


#initialize labels but don't display as values aren't yet determined
#also, weird error appears if this section is located just above main program section
#i think it has something to do with the label object
lablT=label(pos=vector(0,.35,0),text=textT,visible=False,box=False,opacity=0,color=color.black)     
lablH=label(pos=vector(0,-1.65,0),text=textH,visible=False,box=False,opacity=0,color=color.black)   

##meter labels
cnt = 0
labf=1.1                                                #constant to offset labels
#thermometer meter label
for theta in np.linspace(tickStart, tickEnd, 11):       #create 6 major ticks (0-5)
    label = text(text=str(cnt),
        color=color.black,                              #color
        pos=vector(labf*arrowLength*np.cos(theta),      #position
        labf*arrowLength*np.sin(theta)+.5,0),
        height=.075,                                    #label size
        align='center',                                 #center the labels
        axis=vector(arrowLength*np.cos(theta-np.pi/2),  #direction
        arrowLength*np.sin(theta-np.pi/2),0))                                   
    cnt=cnt+10                                          #increment counter

#humidity meter label
cnt = 0
for theta in np.linspace(tickStart, tickEnd, 11):       #create 6 major ticks (0-5)
    label = text(text=str(cnt),
        color=color.black,                              #color
        pos=vector(labf*arrowLength*np.cos(theta),      #position
        (labf*arrowLength*np.sin(theta))-1.5,0),
        height=.075,                                    #label size
        align='center',                                 #center the labels
        axis=vector(arrowLength*np.cos(theta-np.pi/2),  #direction
        arrowLength*np.sin(theta-np.pi/2),0))                                   
    cnt=cnt+10                                          #increment counter

##################
## main program ##
##################

#main program
while True:                                             #begin infinite loop
    while (arduinoData.inWaiting()==0):                 #if no data available
        pass                                            #loop until data appears
    dataPacket=arduinoData.readline()                   #data is available, read it
    dataPacket=str(dataPacket, 'utf-8')                 #convert data to string
    dataPacket=dataPacket.strip('\r\n')                 #strip out \r and \n
    splitPacket=dataPacket.split(",")                   #convert string to integer array removing separators
    tempF=10*float(splitPacket[0])                      #convert 1st array value to float & multiply by 10 to display properly on meter     
    humidity=10*float(splitPacket[1])                   #convert 2nd array value to float & multiply by 10 to display properly on meter
    
    #set temperature arrow
    theta=-2*np.pi/3069*tempF+5*np.pi/6                 #formula to get angle of line of potVal voltage
    tempArrow.axis=vector(arrowLength*np.cos(theta),    #point the arrow
        arrowLength*np.sin(theta),0)
    
    #set humidity arrow
    theta=-2*np.pi/3069*humidity+5*np.pi/6              #formula to get angle of line of potVal voltage
    humidArrow.axis=vector(arrowLength*np.cos(theta),   #point the arrow
        arrowLength*np.sin(theta),0)
    
    tempS=str(float(splitPacket[0]))                    #convert 1st array value to string
    humS=str(float(splitPacket[1]))                     #convert 2nd array value to string
    lablT.text='Temperature = ' + tempS                 #new temperature label
    lablT.visible=True                                  #display temperature label
    lablH.text='Humidity = ' + humS                     #new humidity label
    lablH.visible=True                                  #display humidity label