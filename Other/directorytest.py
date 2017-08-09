import os

dir_name = os.path.dirname(os.path.realpath(__file__))
print (dir_name)

f = "Hello.txt"
fpath = os.system((dir_name) + ("\\") + (f))
r = open(fpath, 'r')