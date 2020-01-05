import person

class Customer(person):
    def __init__(self, name, address, telNumber, customerNumber, mailingList):
        Person.__init__(self, name, address, telNumber)
        self.__customerNumber = customerNumber
        self.__mailingList = mailingList
        
    def customerMailingChoice(self):
        customerChoice = input('Would you like to be added to our mailing list? ')
        if customerChoice == 'yes':
            self.__mailingList = true
        else:
            self.__mailingList = false

               
    def setCustomerNumber(self):
        self.__customerNumber = customerNumber
        
    def getCustomerNumber(self):
        return self.__customerNumber
        
    