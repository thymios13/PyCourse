from diffusion_model import energy
from nose.tools import assert_equal
def test_energy():
  """ Optional description for nose reporting """
  assert_equal(energy([1,1],1.0), 0)
