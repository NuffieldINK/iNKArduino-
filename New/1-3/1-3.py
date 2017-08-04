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

#Queues each player 
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

#To do: Make into a single function -- pass the paths via a parameter
def CalibrationS1(i):

    f = open("Sen1.txt", 'r')
    line = f.readlines()
    value = line[i].strip('\n')
    value = int(value)
    print(value)
    f.close()

    return(value)
   
def CalibrationS2(i):

    f = open("Sen3.txt", 'r')
    line = f.readlines()
    value = line[i].strip('\n')
    value = int(value)
    print(value)
    f.close()
    
    return(value)

S1Low = CalibrationS1(0)
S1High = CalibrationS1(2)

S2Low = CalibrationS2(0)
S2High = CalibrationS2(2)

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

