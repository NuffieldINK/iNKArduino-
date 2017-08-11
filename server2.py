#This program creates a server on this computer
#PLEASE NOTE:
#--> Use this file (server2.py) on Sandbox
#--> To shut off server close the powershell --> Must be improved

#Importing Libraries
import socket
import os

#Finding the directory that this file is on
#Therefore the file you want to use must be in the same directory as server2.py
dir_name = os.path.dirname(os.path.realpath(__file__))
arduino1 = "1-3.py"
arduino2 = "2-4.py"

#This is the ip adress of this computer
#Improvements --> Finding the ip adress
host = "138.38.153.189"

#opens the socket/server
s = socket.socket()
#Returns the ip adress
host = socket.gethostbyname(host)
#Reserving a port
port = 200
#Host binding to this port
s.bind((host, port))
#Waits for connection from client
s.listen(5)

while True:
    #Accepts the connection request from the client
    c, addr = s.accept()
    print(("Got connection from ") + repr(addr[1]))
    #Opens python file, activating Arduino
    os.system("python " + (dir_name) + ("\\") + (arduino2))
    #Closes the connection
    c.close()
