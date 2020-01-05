#importing car class so that i can use it in the program
import car
#creating an instance of the class and returning it
def createCar():
    myCar = car.Car('Buick', '1996')
    return myCar
#accelerating the car and printing out the speed of the car
def accelerateCar(myCar):
    for num in range(5):
        print('The car is accelerating..')
        myCar.accelerate()
        print('Your speed is', myCar.getSpeed())
#breaking the car and printing out the speed of the car        
def brakeCar(myCar):
    for num in range(5):
        print('The car is breaking..')
        myCar.brake()
        print('Your speed is', myCar.getSpeed())
        
def main():
    import time
    myCar = createCar()
    accelerateCar(myCar)
    brakeCar(myCar)
    time.sleep(3)
    
main()
    