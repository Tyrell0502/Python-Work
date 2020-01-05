#tyrell.brantley001@albright.edu
#ask the user for 2 integers
def getNumber():
    try:
        numberOne = int(input('Enter the first number: '))
    except ValueError:
        print('This is not an interger! Try again.')
        numberOne = int(input('Enter the first number: '))
    else:
        return numberOne
    
def getNumberTwo():
    try:
        numberTwo = int(input('Enter the second number: '))
    except ValueError:
        print('This is not an interger! Try again.')
        numberTwo = int(input('Enter the second number: '))
    else:
        return numberTwo

#print the larger value
def compareNumbers(numberOne, numberTwo):
    print(max(numberOne, numberTwo))
    print('This is the larger number of the two')
    
def main():
    import time
    numberOne = getNumber()
    numberTwo = getNumberTwo()
    compareNumbers(numberOne, numberTwo)
    time.sleep(5)
    
main()