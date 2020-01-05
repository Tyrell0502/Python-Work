#tyrell.brantley
#started the program off by getting the inputs from the user
def getName():
    name = input('Enter your name: ')
    return name

def getScore():
    score = input('Enter your golf score: ')
    while score < 0:
        print('This is not a valid score, try again.')
        score = input('Enter your golf score: ')
        return score
#I then saved both the score and the name to the file golf.txt    
def saveFile(name, score):
    userFile = open('golf.txt', 'w')
    userFile.write(name, score)
    userFile.close()
#I then read the contents of the file that just had the name and
#score saved to it    
def readFile():
    userFile = open('golf.txt', 'r')
    line = userFile.readline()
    while line != '':
        print(line.rstrip('/n'))

def main():
    import time
    name = getName()
    score = getScore()
    saveFile(name, score)
    readFile()
    time.sleep(3)
main()
        