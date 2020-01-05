def getFile():
    userFileName = input('Enter the name of the file: ')
    userFile = open('userFileName', 'r')
    return userFile

def addNumbers(userFile):
    sum = 0
    line = int(userFile.readline())
    while line != '':
        print(line.rstrip('/n'))
        sum += line
    print('The sum of these numbers are', sum)
        
def main():
    import time
    userFile = getFile()
    addNumbers(userFile)
    time.sleep(3)
        
main()