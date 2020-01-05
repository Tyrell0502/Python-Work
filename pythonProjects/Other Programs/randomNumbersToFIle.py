#tyrell.brantley001@albright.edu
def getFile():
    userFileName = input('Enter the name of the file: ')
    userFile = open('userFileName', 'w')
    return userFile
#writing the amount of random numbers the user wants to add to the file
def randomNumbers(userFile):
    import random
    amountOfNumbers = input('How many random numbers would you like to be added to this file? ')
    for range in (amountOfNumbers):
        userFile.write(random(500))
        
def main():
    import time
    userFile = getFile()
    randomNumbers(userFile)
    time.sleep(3)
main()