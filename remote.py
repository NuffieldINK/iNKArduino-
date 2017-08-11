#This is the client code that can connect to both servers
#Use this code on PC3 (Barebones)
#This a very basic version... but it works
#Importing libraries
import socket

#This is the ip adress of PC1 (Impact)
host1 = "138.38.242.122"
#Reserves a port
port1 = 100

#Searching for server from PC1
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Returns the ip adress
remote_ip1 = socket.gethostbyname(host1)
#Connects to the server running on PC1
s1.connect((remote_ip1, port1))


#This is the ip adress of PC2 (Sandbox)
host2 = "138.38.153.189"
#Reserves a port
port2 = 200

#Searching for server from PC2
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Returns the ip adress
remote_ip2 = socket.gethostbyname(host2)
#Connects to the server running on PC2
s2.connect((remote_ip2, port2))