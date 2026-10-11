# pyground

`pyground` is a small Python project for experimenting with classes, inheritance,
and pytest. It models people and vehicles and includes a command-line program that
demonstrates them.

## Requirements

- Python 3.15 or later
- pip

## Install

From the project directory, install the package and its test dependencies:

```sh
python -m pip install -e ".[test]"
```

## Run

Run the demo with the installed command:

```sh
pyground
```

Or run it as a Python module:

```sh
python -m pyground.main
```

The demo introduces several people, has them greet one another, and shows a car
and a train accelerating and making their respective sounds.

## Package contents

- `pyground.person.Person` stores a person's name, age, and gender; `declare()`
  prints an introduction and `shakehands(other)` prints a greeting.
- `pyground.vehicles.Vehicle` stores a vehicle's name, maximum speed, and driver.
  Its `accelerate()` method describes the driver speeding up the vehicle.
- `pyground.vehicles.Car` and `pyground.vehicles.Train` extend `Vehicle` with
  `honk()` and `signal()` methods.
- `pyground.main` assembles and runs the demonstration.

## Tests

Run the test suite from the project directory:

```sh
python -m pytest
```

The tests cover person greetings and vehicle behavior. The GitLab CI pipeline,
GitHub Actions workflow, and Bitbucket pipeline install the project with the
`test` extra and run pytest.
