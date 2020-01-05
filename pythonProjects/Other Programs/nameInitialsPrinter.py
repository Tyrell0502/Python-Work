def getFirstName():
    firstName = []
    userFirstName = input('Enter your first name: ')
    firstName.append(userFirstName)
    return firstName

def getMiddleName():
    middleName = []
    userMiddleName = input('Enter your middle name: ')
    middleName.append(userMiddleName)
    return middleName

def getLastName():
    lastName = []
    userLastName = input('Enter your last name: ')
    lastName.append(userLastName)
    return lastName

def printInitials(firstName, middleName, lastName):
    print(firstName[:1], middleName[:1], lastName[:1])
    
def main():
    firstName = getFirstName()
    middleName = getMiddleName()
    lastName = getLastName()
    printInitials(firstName, middleName, lastName)
    
main()
    
