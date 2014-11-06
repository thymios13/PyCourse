from diffusion_model import energy
from monteCarlo import update_density
from nose.tools import assert_equal, assert_raises

def test_energy():
    # Test if the output is as expected
    assert_equal(energy([1,2,3,4]), 10)

def test_contains_float():
    # Test if the input contains a float number
    with assert_raises(TypeError):
        energy([1,2.0,3,4])

def test_contains_negative_number():
    # Test if the input contains a negative number
    with assert_raises(ValueError):
        energy([1,2,-3,4])

def test_contains_rubbish_input():
    # Test if the input is rubbish (e.g string)
    with assert_raises(TypeError):
        energy([1,2,'abc',4])

def test_update_density():
    # Test if the input is nothing
    with assert_raises(TypeError):
        update_density([])