import socket
import sys  
 
host = '138.38.173.193'
port = 12345
 
# create socket
print('# Creating socket')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#print('# Getting remote IP address') 
remote_ip = socket.gethostbyname( host )

# Connect to remote server
s.connect((remote_ip , port))

# Receive data
print('# Receive data from server')
reply = s.recv(1024)
 
print (reply)

 