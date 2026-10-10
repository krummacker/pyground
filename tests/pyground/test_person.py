import pytest

from pyground.person import Person


def test_person_stores_identity_details():
    person = Person("Alice", 30, "F")

    assert person.name == "Alice"
    assert person.age == 30
    assert person.gender == "F"


@pytest.mark.parametrize(
    ("name", "age", "gender", "expected"),
    [
        ("Alice", 30, "F", "My name is Alice and I am 30 years old.\n"),
        ("Bob", 25, "M", "My name is Bob and I am 25 years old.\n"),
    ],
)
def test_person_declare_prints_expected_message(capsys, name, age, gender, expected):
    person = Person(name, age, gender)

    person.declare()

    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize(
    ("self_name", "other_name", "expected"),
    [
        ("Alice", "Alice", "I am shaking hands with myself, says Alice.\n"),
        ("Alice", "Bob", "Hello Bob, I am Alice. How are you?\n"),
    ],
)
def test_person_shakehands_prints_expected_message(capsys, self_name, other_name, expected):
    self_person = Person(self_name, 30, "F")
    other_person = Person(other_name, 28, "M")

    self_person.shakehands(self_person if self_name == other_name else other_person)

    captured = capsys.readouterr()
    assert captured.out == expected
