import serial
import pygame
import time

#Variables
S1Low = 0
S1High = 0
inp = 0

#Need to create own timer class to make sure the audio will restart after 10 seconds of being out of range
class Timer:

    def __init__(self):

        self.elapsed = 0.0
        self.running = False
        self.last_start_time = None

    def start(self):

        if not self.running:
            self.running = True
            self.last_start_time = time.time()

    def reset(self):

        if self.running:
            self.elapsed = 0.0
            self.running = False
            self.last_start_time = None

    def get_elapsed(self):

        elapsed = self.elapsed

        if self.running:
            elapsed += time.time() - self.last_start_time
        return elapsed


#Sensor 1 code -  responsible for playing audio or not
def Sensor1(data):

    #If this number (data) is between the range it will play the audio otherwise it will pause it
    if data > S1Low and data < S1High:
        player1.unpause()
    else:
        player1.pause()

        #If the user is out of range for more than 10 seconds
        pygame.time.set_timer(S1_next, 10000)

#Sensor 2 code -  responsible for playing audio or not
def Sensor2(data):

    #If the pressure pad is pressed it will play the audio
    if data == 2000:
        player2.unpause()
    else:
        player2.pause()

        #If the user is out of range for more than 10 seconds
        pygame.time.set_timer(S1_next, 10000)


#Search - Decides whether Sensor1 or Sensor2 gets called
def Search(data):

    #Looks at data and chooses whether it belongs to S1 or S2
    if data.find('S1') >= 0:
        info = int(data.split(':')[1])
        Sensor1(info)
    elif data.find('S2') >= 0:
        info = int(data.split(':')[1])
        Sensor2(info)
    else:
        print("Failure")

#Callibration code - small but allows for reuse for all sesnors
def Calibration(i):

    f = open("Sen3.txt", 'r')
    line = f.readlines()
    value = line[i].strip('\n')
    value = int(value)
    print(value)
    f.close()

    return(value)

#Main
if __name__ == "__main__":

    # If you get an error about Serial - make sure the USB is plugged in all the way
    #Connects to the port/Opens it
    ser = serial.Serial("COM6", 9600)
    time.sleep(2)

    #Initialises the players and loads the players for them
    pygame.mixer.init()
    player1 = pygame.mixer.music
    player2 = pygame.mixer.music

    player1.load('2.wav')
    player2.load('4.wav')

    #Tricks the player into looping
    player1.play(-1)
    player1.pause()
    player2.play(-1)
    player2.pause()

    #Calibrates the two sensors
    S1Low = Calibration(0)
    S1High = Calibration(2)

    #Waits for 5 seconds -- This is to stop the audio from playing straight away
    time.sleep(5)

    while True:

        read = ser.readline().decode()
        Search(read)

    #Makes sure the script doesn't close while there is still audio playing
    while player1.get_busy() or player2.get_busy():
        pygame.time.Clock().tick(10)

    #Closes the port
    ser.close()
