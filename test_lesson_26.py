from lesson_26 import divide_foo
import pytest


@pytest.mark.parametrize(
    ("a", "b", "expected"), [(10, 2, 5), (20, 2, 10), (-10, -2, 5)]
)
def test_positiv_divide_foo(a: int, b: int, expected: float):
    assert divide_foo(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected_exception"), [(10, 0, ZeroDivisionError), ("20", 2, ValueError), (-10, "-2", ValueError)]
)
def test_exceptions_divide_foo(a, b, expected_exception):
    with pytest.raises(expected_exception):
        divide_foo(a, b)
