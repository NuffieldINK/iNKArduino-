#DO NOT USE!
#PLEASE READ: This file is currently not being used for the project and will need many improvements
#A little program that will run a selection of programs

import os
import argparse



#Parses the arguments 
parser = argparse.ArgumentParser(description = 'A little program that will run a selection of programs')

#In this version, you want to either run both programs or only one of them hence why they are mutally exclusive 
group = parser.add_mutually_exclusive_group()

#Adds the arguments
group.add_argument('-rb', '--runboth', action = 'store_true', help = 'Runs both Arduino programs')
group.add_argument('-r', '--run', help='Runs one of the Arduino program that you specify after the flag')

#Parses in the actual arguments 
args = parser.parse_args()

#This function could be improved to be inclusive of python program (although it would be easier to just run it manually)

#Chooses which program should be run
def run():
    if args.run == "1-3.py":
        os.system('python C:\\Users\\Impact\\Documents\\Temp\\iNKArduino\\1-3.py')
    elif args.run == "2-4.py":
        os.system('python C:\\Users\\Impact\\Documents\\Temp\\iNKArduino\\2-4.py')
    else:
        print("ERROR: YOU HAVE NOT SELECTED A CORRECT FILE \n")

#Main    
if __name__ == "__main__":
    
    print("Running...")

    #Translates the arguments into actions 
    if args.run:
        run()
    elif args.runboth:
        os.system ('python C:\\Users\\Impact\\Documents\\Temp\\iNKArduino\\1-3.py')
        os.system ('python C:\\Users\\Impact\\Documents\\Temp\\iNKArduino\\2-4.py')
