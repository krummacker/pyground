import pytest

from pyground.person import Person
from pyground.vehicles import Car, Train, Vehicle


def test_vehicle_stores_driver_and_attributes():
    driver = Person("Dana", 35, "F")
    vehicle = Vehicle("Sedan", 140, driver)

    assert vehicle.name == "Sedan"
    assert vehicle.maxspeed == 140
    assert vehicle.driver is driver


@pytest.mark.parametrize(
    ("driver_name", "driver_gender", "vehicle_name", "maxspeed", "expected"),
    [
        ("Dana", "F", "Sedan", 140, "Dana speeds up her Sedan from zero to 140 km/h.\n"),
        ("Sam", "M", "Truck", 90, "Sam speeds up his Truck from zero to 90 km/h.\n"),
    ],
)
def test_vehicle_accelerate_uses_pronoun_matching_driver_gender(
    capsys, driver_name, driver_gender, vehicle_name, maxspeed, expected
):
    driver = Person(driver_name, 40, driver_gender)
    vehicle = Vehicle(vehicle_name, maxspeed, driver)

    vehicle.accelerate()

    captured = capsys.readouterr()
    assert captured.out == expected


def test_car_honk_prints_honk_message(capsys):
    car = Car("Sedan", 120, Person("Dana", 33, "F"))

    car.honk()

    captured = capsys.readouterr()
    assert captured.out == "Honk!\n"


def test_train_signal_prints_train_message(capsys):
    train = Train("Express", 180, Person("Leo", 41, "M"))

    train.signal()

    captured = capsys.readouterr()
    assert captured.out == "Choo choo!\n"
