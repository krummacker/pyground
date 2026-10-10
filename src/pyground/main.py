from .person import Person
from .vehicles import Car, Train

def main():
    x = Person("Dirk", 33, 'M')
    x.declare()

    y = Person("Methuselah", 1000, 'M')
    y.declare()

    z = Person("Fred", 50, 'M')
    z.declare()

    doerthe = Person("Dörthe", 40, 'F')
    doerthe.declare()

    x.shakehands(y)
    y.shakehands(z)
    z.shakehands(x)
    doerthe.shakehands(doerthe)

    a = Car("BMW", 250, x)
    a.accelerate()
    a.honk()

    b = Train("Adler", 30, doerthe)
    b.accelerate()
    b.signal()


if __name__ == "__main__":
    main()
