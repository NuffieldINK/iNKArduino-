import serial 
import os
import time 


ser = serial.Serial("COM6", 9600)
time.sleep(2)

senFile = {"1": "Sen1.txt", "2": "Sen2.txt", "3": "Sen3.txt"}
response = input("Which sensor are you callibrating? Press 1 for Sensor 1, 2 for Sensor 2, 3 for Sensor 3: ")

if response == "2":
    fpath = os.path.join("C:\\Users\\Impact\\Documents\\Temp\\iNKArduino\\New\\2-4\\", senFile[response])
elif response == "1" or response == "3":
    fpath = os.path.join("C:\\Users\\Impact\\Documents\\Temp\\iNKArduino\\New\\1-3\\", senFile[response])
else:
    print("Failure")
f = open(fpath, 'w')

for i in range(2):
    inp = ser.readline().decode()
    f.write(inp)

f.close()