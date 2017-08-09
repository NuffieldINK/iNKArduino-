import socket
import os

dir_name = os.path.dirname(os.path.realpath(__file__))
arduino1 = "1-3.py"
arduino2 = "2-4.py"


host = "138.38.242.122"

s = socket.socket()
host = socket.gethostbyname(host)
port = 100
s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    print(("Got connection from ") + repr(addr[1]))
    os.system("python " + (dir_name) + ("\\") + (arduino1))
    c.close()
