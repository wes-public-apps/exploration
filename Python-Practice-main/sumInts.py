# Wesley Murray
# 2/9/2020
# This script is meant to sum a range of numbers

#import libraries
import sys

#globals
START = 0
STOP = 0

#validate command line args
def commandLineArgValidation():
    global START,STOP

    #check for two arguments
    if(len(sys.argv)!=3):
        return "Error: Provide exacly two arguments."

    #validate arg type
    try:
        START = int(sys.argv[1])
        STOP = int(sys.argv[2])
    except ValueError:
        return "Error: The provided arguments are not integers."

    #validate order
    if(START>STOP):
        temp = START
        START = STOP
        STOP = temp

    return None

#sum a range of numbers
def summer(start,stop):
    return sum(range(start,stop+1))

#run function
def main():
    global START,STOP
    
    output=commandLineArgValidation()
    if(output==None):
        print("Start: "+str(START),"Stop: "+str(STOP),"Sum: "+str(summer(START,STOP)))
    else:
        print(output)

main()