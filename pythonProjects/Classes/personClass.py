class Person:
    def __init__(self, name, address, telNumber):
        self.__name = name
        self.__address = address
        self.__telNumber = telNumber
        
    def setName(self):
        self.__name = name
        
    def setAddress(self):
        self.__address = address
        
    def setTelNumber(self):
        self.__telNumber = telNumber
        
    def getName(self):
        return self.__name
    
    def getAddress(self):
        return self.__address
    
    def getTelNumber(self):
        return self.__telNumber