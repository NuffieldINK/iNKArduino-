import serial
import pyglet
import time


#Extra vars
S1High = 0
S1Low = 0
inp = 0

def sensor1(data):
    #If this number is between the range it will play the audio otherwise it will pause it
    if data > S1Low and data < S1High:
        player1.play()

    else:
        player1.pause()


def sensor2(data):
    #If this number is between the range it will play the audio otherwise it will pause it
    if(data == 2000):
        player2.play()
    elif(data == 3000):
        player2.pause()

def search(data):

    #Searches the line and looks for the prefixes and then splits the data up which then goes to the relevant functions
    print(data)
    if data.find('S3') >= 0:
        info = int(data.split(':') [1])
        sensor1(info)
    elif data.find('S4') >= 0:
        info = int(data.split(':') [1])
        sensor2(info)
    else:
        print("Failure")

#Calibration module - Reads in the calibration files and inputs them into variables
def Calibration(i):
    f = open("Sen3.txt", 'r')
    line = f.readlines()
    value = line[i].strip('\n')
    value = int(value)
    print(value)
    f.close()

    return(value)

if __name__ == '__main__':

    # If you get an error about Serial - make sure the USB is plugged in all the way
    #Connects to the port/Opens it
    ser =  serial.Serial("COM3", 9600)
    time.sleep(1)

    #Initialises the players and then queues the audio for both
    player1 = pyglet.media.Player()
    player2 = pyglet.media.Player()

    player1.queue(pyglet.media.load('2.wav', streaming=False))
    player2.queue(pyglet.media.load('4-2.wav', streaming = False))

    #Runs the calibration for the sensor
    S1Low = Calibration(0)
    S1High = Calibration(2)

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
