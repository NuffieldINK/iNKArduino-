import serial
import pyglet
import time 
import threading

# If you get an error about Serial - make sure the USB is plugged in all the way 
#Connects to the port/Opens it 
ser =  serial.Serial("COM3", 9600)
time.sleep(1)

#Initialises the players and then queues the audio for both 
player1 = pyglet.media.Player()
player2 = pyglet.media.Player()

player1.queue(pyglet.media.load('2.wav', streaming=False))
player2.queue(pyglet.media.load('4.wav', streaming = False))

def on_eos():
        player1.queue(pyglet.media.load('2.wav', streaming=False))


def sensor1(data):
    #If this number is between the range it will play the audio otherwise it will pause it
    if data > S1Low and data < S1High:
        player1.play()

    else:
        player1.pause()
        
    on_eos()
   


def sensor2(data):
    
    if(data == 2000):
        player2.play()
    elif(data == 3000):
        player2.pause()

def search(data):
    print(data)
    if data.find('S1') >= 0:
        info = int(data.split(':') [1])
        sensor1(info)
    elif data.find('S2') >= 0:
        info = int(data.split(':') [1])
        sensor2(info)
    else:
        print("Failure")    

#Extra vars 

S1High = 0
S1Low = 0
inp = 0
def Calibration():
    #To get the range it listens for the serial port, the first number from the serial is the low value
    inp = ser.readline().decode()
    print(inp)
    inp = int(inp.split(':') [1])
    print(inp)
    return inp



S1Low = Calibration()
S1High = Calibration()

#Waits for 5 seconds -- This is to stop the audio from playing straight away
time.sleep(5)

#While loop that does all the magic 
while True:
    #Reads the number from serial
    read = ser.readline().decode()
    search(read)

#Closes the port 
ser.close()

#Packages the audio player 
pyglet.app.run()

