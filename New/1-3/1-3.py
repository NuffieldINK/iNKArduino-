import serial
import pyglet
import time 

# If you get an error about Serial - make sure the USB is plugged in all the way 
#Connects to the port/Opens it 
ser =  serial.Serial("COM6", 9600)
time.sleep(1)

#Initialises the players and then queues the audio for both 
player1 = pyglet.media.Player()
player2 = pyglet.media.Player()

player1.queue(pyglet.media.load('1.wav', streaming=False))
player2.queue(pyglet.media.load('3.wav', streaming = False))


def sensor1(data):
    #If this number is between the range it will play the audio otherwise it will pause it
    if data > S1Low and data < S1High:
        player1.play()

    else:
        player1.pause()
        
  
def sensor2(data):

    #If this number is between the range it will play the audio otherwise it will pause it
    if data > S2Low and data < S2High:
        player2.play()
    else:
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


S1Low = 0
S1High = 0
S2Low = 0
S2High = 0
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

S2Low = Calibration()
S2High = Calibration()

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

