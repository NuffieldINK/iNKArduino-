import serial
import pyglet
import time 
import threading

#If you get an error about Serial - make sure the USB is plugged in all the way 
#Connects to the port/Opens it 
ser =  serial.Serial("COM3", 9600)


#Initialises the player and then queues the audio
player = pyglet.media.Player()
player.queue(pyglet.media.load('3-2.wav', streaming=False))

def on_eos():
        player.queue(pyglet.media.load('3-2.wav', streaming=False))

#Function that determines what happens after the timer finishes 
#At the moment this a tad bit broken - the audio when it gets replayed keeps skipping a lot 
def nxt():
    player.queue(pyglet.media.load('3-2.wav', streaming=False))
    player.next_source()

def range():
    #Timer var
    t = threading.Timer(10.0, nxt)

    #If this number is between the range it will play the audio otherwise it will pause it
    if read > Low or read < High:
        player.play()

    else:
        t.start()
        player.pause()
        
    on_eos()

#Extra vars 
first = True
Low = 0
High = 0


#To get the range it listens for the serial port, the first number from the serial is the low value
while first == True:
  Low = int(ser.readline())
  first = False 

#Waits for 5 seconds -- This is to stop the audio from playing straight away
time.sleep(5)

#While loop that does all the magic 
while True:
    #Reads the number from serial
    read = int(ser.readline())
    range()

#Closes the port 
ser.close()

#Packages the audio player 
pyglet.app.run()
