from diffusion_model import energy
from monteCarlo import update_density
from nose.tools import assert_equal

def test_energy():

    # Test if the output is as expected
    assert_equal(energy([1,2,3,4]), 10)

    # Test if the input contains a float number
    assert_equal(energy([1,2.0,3,4]), 10)

    # Test if the input contains a negative number
    assert_equal(energy([1,2,-3,4]), 10)

    # Test if the input is rubbish (e.g string)
    assert_equal(energy([1,2,'abc',4]), 10)

def test_update_density():

    # Test if the input is nothing
    assert_equal(update_density([]), 10)
