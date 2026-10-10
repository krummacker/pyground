class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def declare(self):
        print("My name is", self.name, "and I am", self.age, "years old.")

    def shakehands(self, other):
        if self == other:
            print("I am shaking hands with myself, says " + self.name + ".")
        else:
            print("Hello", other.name + ",", "I am", self.name + ".", "How are you?")
