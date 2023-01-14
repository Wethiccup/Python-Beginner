from calculator import square

import pytest


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0
    
def test_str():  # Used to test a type of error that is expected
    with pytest.raises(TypeError):
        square("cat")


# use "pytest test_calculator.py" in terminal to see where it fails

# seperated into different tests to identify why and where it fails