#creating the class
class Car:
#using the init method to initialize the data attributes that i
#will be using
    def __init__(self, make, yearModel):
        self.__make = make
        self.__yearModel = yearModel
        self.__speed = 0
#creating a method for the acceleration of the car        
    def accelerate(self):
        self.__speed += 5
#creating a method for the breaking of the car        
    def brake(self):
        self.__speed -= 5
#creating a method to return the speed of the car        
    def getSpeed(self):
        return self.__speed