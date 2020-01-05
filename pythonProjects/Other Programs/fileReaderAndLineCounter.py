#tyrell.brantley001@albright.edu
#gets a file from the user
def getFile():
    userFileName = input('Enter the name of the file: ')
    userFile = open('userFileName', 'r')
    return userFile
#reads the numbers from the file and keeps an accumulator to see how many items are in the file
def readFile(userFile):
    accumulator = 0
    line = userFile.readline()
    while line != '':
        print(line.rstrip('/n'))
        accumulator += 1
    print('This file has', accumulator, 'amount of items')
    
def main():
    import time
    userFile = getFile()
    readFile(userFile)
    time.sleep(3)
    
main()