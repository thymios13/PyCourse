from ..greengraph_main import myGreengraph
from ..geolocation import geolocate
from nose.tools import assert_raises

def test_myGreengraph_for_missed_input():
    with assert_raises(TypeError):
        myGreengraph("Athens",[])

def test_myGreengraph_for_a_number_input():
    with assert_raises(TypeError):
        myGreengraph([1],"Athens")

def test_myGreengraph_for_more_than_2_inputs():
    with assert_raises(TypeError):
        myGreengraph("London", "Paris", "Athens")

def test_myGreengraph_for_empty_input():
    with assert_raises(TypeError):
        myGreengraph([])

def test_geolocate_returning_wrong_output():
    with assert_raises(TypeError):
        geolocate("asdasasdadsdf")
