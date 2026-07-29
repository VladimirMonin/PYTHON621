from lesson_26 import divide_foo
import pytest

def test_positiv_divide_foo():
    assert divide_foo(12, 3) == 3.0
    assert divide_foo(10, 2) == 5.0
    assert divide_foo(9, 3) == 3.0
    


def test_zero_divide_foo():
    with pytest.raises(ZeroDivisionError):
        divide_foo(10, 0)
