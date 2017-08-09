#Calibration Python Script 
#Only calibrates one sensor per running
#PLEASE READ: Make sure to upload Arduino calibration.ino onto the board before running file
#After Calibration upload the correct .ino files to each board  

#Imports a load os libraries 
import serial 
import os
import time 

#Opens up the Serial connection 
ser = serial.Serial("COM6", 9600)

#Waits for the calibration to end 
time.sleep(5)

#Dictionary for the sensor data files 
senFile = {"1": "Sen1.txt", "2": "Sen2.txt", "3": "Sen3.txt"}

#Finds the directory of current file
dir_name = os.path.dirname(os.path.realpath(__file__))
arduino1 = "1-3.py"
arduino2 = "2-4.py"

#Asks the user which sensor they just calibrated 
response = input("Which sensor are you calibrating? Press 1 for Sensor 1, 2 for Sensor 2, 3 for Sensor 3: ")

#Changes where the sensor data goes 
if response == "3":
    fpath = os.path.join((dir_name) + ("\\"), senFile[response])
elif response == "1" or response == "2":
    fpath = os.path.join((dir_name) + ("\\"), senFile[response])
else:
    print("Failure")

#Opens up the file 
f = open(fpath, 'w')

#Inputs the data into the txt file 
for i in range(2):
    inp = ser.readline().decode()
    f.write(inp)

#Closes the file 
f.close()