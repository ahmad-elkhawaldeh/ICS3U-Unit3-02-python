# !/user/bin/env python3

# created by: Ahmad El-khawaldeh
# created on: Nov 2020
#  this program checks if u got the right random number 

import constants

def main():
    # this function checks if the random number is 5 

    # input
    random_number = int(input("enter a number from 1 to 9:")) 
   
    #process 
    if random_number == constants.RANDOM_NUMBER:
        #output
        print("")
        print(" Correct  ")

if __name__ == "__main__":
    main()
