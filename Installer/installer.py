import os
import sys

args = sys.argv
count = len(args)
i = 0

def run():
    if(count == 3):
        os.system('python ' + args[2])
    elif(count == 4):
        os.system('python ' + args[3])
    else:
        print("ERROR: Unsupported number of files")
        helper()

def runB():

    print("Running both programs...")
    os.system('python 1-3.py')
    os.system('python 2-4.py')

def test():
    print("Testing mode: \n")
    for i in range(count):
      print("arg[" + str(i) +"]: " + args[i])

def helper():
    print("Help: \n")
    print("This is a quick little program that allows the user to quickly and easily run the preloaded python programs \n")
    print("Allowed options: \n")
    print("-h [ --help ] displays this help prompt \n")
    print("-r [ -- run ] arg *arg runs the code that you've typed in \n")
    print("-rb [ --run both ] runs both programs \n")
    print("-t [ --test ] shows the cmd line args (for testing purposes only) \n")


def menu():
    if(args[1] == "-rb"):
        runB()
    elif(args[1] == "-r"):
        run()
    elif(args[1] == "-t"):
        test()
    else:
        helper()

if __name__ == "__main__":
    #Cannot use switch-case in Python 

    #Either the user has just called the program or they have entered in args
    if(count == 1):
        helper()
    else:
        menu()


