import pytest

from pyground.functions import fibonacci, hof, pi, sqr


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, []),
        (1, []),
        (2, [1, 1]),
        (10, [1, 1, 2, 3, 5, 8]),
    ],
)
def test_fibonacci_returns_values_lt_n(n, expected):
    assert fibonacci(n) == expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (0, 1),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 3),
    ],
)
def test_hof_returns_expected_values(value, expected):
    assert hof(value) == expected


@pytest.mark.parametrize(
    ("operand", "expected"),
    [
        (4, 16),
        (-3, 9),
        (2.5, 6.25),
    ],
)
def test_sqr_returns_square_of_operand(operand, expected):
    assert sqr(operand) == expected


def test_pi_returns_approximation_of_pi():
    assert pi(1000000) == pytest.approx(3.141592653589793, abs=1e-8)


@pytest.mark.parametrize("depth", [0, 3])
def test_pi_rejects_depth_below_minimum(depth):
    with pytest.raises(ValueError, match="depth must be at least 4"):
        pi(depth)
