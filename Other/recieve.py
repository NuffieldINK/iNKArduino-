import serial
import pyglet
import time 




#If you get an error about Serial - make sure the USB is plugged in all the way 
ser =  serial.Serial("COM3", 9600)

#Extra vars 
first = True
Low = 0
High = 0


#Initliases the audio player and gets it to loop
snd = pyglet.media.load('3.wav')
looper = pyglet.media.SourceGroup(snd.audio_format, None)
looper.loop = True
looper.queue(snd)

player = pyglet.media.Player()
player.queue(looper)

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
    
    #If this number is between the range it will play the audio otherwise it will pause it
    if read > Low or read < High:
        player.play()
    else:
        player.pause()

#Closes the port 
ser.close()

#Packages the audio player 
pyglet.app.run()

