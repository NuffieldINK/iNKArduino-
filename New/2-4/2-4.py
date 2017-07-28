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

player1.queue(pyglet.media.load('1.wav', streaming=False))
player2.queue(pyglet.media.load('3.wav', streaming = False))

def on_eos():
        player1.queue(pyglet.media.load('1.wav', streaming=False))

#Function that determines what happens after the timer finishes 
#At the moment this a tad bit broken - the audio when it gets replayed keeps skipping a lot 
def nxt():
    player1.queue(pyglet.media.load('3.wav', streaming=False))
    player1.next_source()

def sensor1(data):
    #Timer var
    t = threading.Timer(10.0, nxt)

    #If this number is between the range it will play the audio otherwise it will pause it
    if data > S1Low or data < High:
        player1.play()

    else:
        t.start()
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
        sensor1(data)
    elif data.find('S2') >= 0:
        info = int(data.split(':') [1])
        sensor2(data)
    else:
        print("Failure")    

#Extra vars 

High = 0
S1Low = 0

def Calibration():
    #To get the range it listens for the serial port, the first number from the serial is the low value
    S1Low = ser.readline().decode()
    S1Low = int(S1Low.split(':') [1])





Calibration()
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

