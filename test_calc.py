import pytest
from calc import add, sub, mul, div, power
from contextlib import nullcontext
def test_add_none_typeerror():
    with pytest.raises(TypeError):
        add(None, None)


#test cases for addition
@pytest.mark.add
def test_add_pos():
    assert add(5,3)==8
def test_add_neg():
    assert add(-5,-1)==-6
def test_add_zer():
    assert add(0,0)==0
def test_add_posneg():
    assert add(5,-8)==-3
def test_add_negpos():
    assert add(5,-1)==4


# Test for subtraction
#using parametrize for code reuse
@pytest.mark.sub
@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (-5, -1, -4),
    (0, 0, 0),
    (5, -8, 13),
    (-5, 1, -6),
])
def test_sub(a, b, expected):
    assert sub(a, b) == expected

# Test for multiplication
@pytest.mark.mul
@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 15),
    (-5, -1, 5),
    (0, 0, 0),
    (5, -8, -40),
    (-5, 1, -5),
    (0, 5, 0),
    (0, -3, 0),
])
def test_mul(a, b, expected):
    assert mul(a, b) == expected

# Test for division
@pytest.mark.div
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (-10, -2, 5),
    (0, 1, 0),
    (10, -2, -5),
    (-10, 2, -5),
    (7, 2, 3.5),
])
def test_div(a, b, expected):
    assert div(a, b) == expected

# Test for divide by zero
def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(5, 0)

# Test for power
@pytest.mark.power
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (-2, 3, -8),
    (0, 0, 1),       # by convention
    (2, -2, 0.25),
    (-2, 2, 4),
    (5, 0, 1),
    (0, 5, 0),
])
def test_power(a, b, expected):
    assert power(a, b) == expected

#Handaling invalid numbers
#using fixtures
@pytest.mark.invalid
@pytest.mark.parametrize("func", [add, sub, mul, div, power])
@pytest.mark.parametrize("a, b", [
    ("5", "3"),
    (None, 3),
    (5, None),
    ([1], 2),
])
def test_invalid_inputs(func, a, b):
    with pytest.raises(TypeError):
        func(a, b)
"""
@pytest.mark.invalid
@pytest.mark.parametrize("a, b", [
    ("5", "3"),
    (None, 3),
    (5, None),
    ([1], 2),
])
def test_add_invalid(a, b):
    with pytest.raises(TypeError):
        add(a, b)
@pytest.mark.invalid
@pytest.mark.parametrize("a, b", [
    ("5", "3"),
    (None, 3),
    (5, None),
    ([1], 2),
])
def test_sub_invalid(a, b):
    with pytest.raises(TypeError):
        sub(a, b)

@pytest.mark.invalid
@pytest.mark.parametrize("a, b", [
    ("5", "3"),
    (None, 3),
    (5, None),
    ([1], 2),
])
def test_mul_invalid(a, b):
    with pytest.raises(TypeError):
        mul(a, b)

@pytest.mark.invalid
@pytest.mark.parametrize("a, b", [
    ("5", "3"),
    (None, 3),
    (5, None),
    ([1], 2),
])
def test_div_invalid(a, b):
    with pytest.raises(TypeError):
        div(a, b)

@pytest.mark.invalid
@pytest.mark.parametrize("a, b", [
    ("5", "3"),
    (None, 3),
    (5, None),
    ([1], 2),
])
def test_power_invalid(a, b):
    with pytest.raises(TypeError):
        power(a, b)


"""
