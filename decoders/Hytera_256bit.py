# TODO: facetune any parameters for a better fit for the specific signal.

import numpy as np

# Hytera 256-bit modulator functions

def hytera256(data):
    '''
    Takes in an input vector of length 256 and returns the modulated version for use in later decoding
    '''
    # Get vector length
    veclength = len(data)
    # Need a function that takes the input and runs a 256-bit modulator on it.
    modulator = hy_modulate_V3(data, veclength)
    # Now we need to extract the resulting signal information
    real = modulator.real
    imag = modulator.imag
    # Construct modulated form from real and imag parts
    mod_data = np.array([real+1j*imag])

    return mod_data

def hy_modulate_V1(data, veclength):
    '''This is the basic 256-bit modulator''' 
    modulated_data = 0

    for index in range(veclength): 
        c = 8.2
        b = 5
        modulated_data = modulated_data + (data[index] - c) * c**b

    return modulated_data

def hy_modulate_V2(data, veclength):
    '''This is another version of the modulator'''
    modulated_data = 0
    # Create the modulator vector
    modulator = np.array(list(map(lambda x: 4 * (1 - 0.137**x) / (2 * x), range(1, veclength + 1))))

    for index in range(veclength): 
        modulated_data = modulated_data + data[index] * modulator[index]

    return modulated_data

def hy_modulate_V3(data, veclength):
    '''This is a smarter version of the modulator'''
    modulated_data = 0
    # Create the modulator vector
    modulator = np.array([2 * (1 - 0.137**x) / (np.sinh(x) * x