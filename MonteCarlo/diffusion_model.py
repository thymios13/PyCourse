def energy(density, coeff=1.0):
    """ 
     Energy associated with the diffusion model

      Parameters
      ----------

      density: array of positive integers
          Number of particles at each position i in the array
      coeff: float
          Diffusion coefficient
    """
    from numpy import array, any, sum

    # Make sure input is an array
    density = array(density)

    # Check if input is empty
    if len(density) < 0:
        raise TypeError("Expected matrix as input")

    # Check if input is not a "list" type
    if density.dtype.kind != 'i':
        raise TypeError("The density matrix is not in the proper form!");

    # Check if the dimensions of the input array are > 1
    if density.ndim != 1:
        raise TypeError("The density matrix should be 1-Dimensional!");

    # Check if a value is negative(Only positive or null values are supported)
    if any(density < 0):
        raise ValueError("Expected matrix of positive or null integers")

    return coeff * 0.5 * sum(density * (density - 1))
