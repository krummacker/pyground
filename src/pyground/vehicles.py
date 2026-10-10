from .person import Person


class Vehicle:
    def __init__(self, name, maxspeed, driver):
        self.name = name
        self.maxspeed = maxspeed
        self.driver = driver

    def accelerate(self):
        if self.driver.gender == 'F':
            word = "her"
        else:
            word = "his"
        print(self.driver.name, "speeds up", word, self.name, "from zero to", self.maxspeed, "km/h.")


class Car(Vehicle):
    def honk(self):
        print("Honk!")


class Train(Vehicle):
    def signal(self):
        print("Choo choo!")
