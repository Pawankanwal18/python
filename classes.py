#class is a blueprint of an object
#class is a user defined data type

class Car:
    def __init__(self):
        self.speed = 0

    def start(self):
        print("car started")

    def stop(self):
        print("car stooped")

your_car = Car()
your_car.start()
your_car.stop()

