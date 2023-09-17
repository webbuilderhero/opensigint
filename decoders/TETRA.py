# TODO: Make sure this decoder works with sigint framework.

# Import necessary libraries
import numpy as np

# Define a function to decode TETRA signals
def decode_tetra(arg):
    '''Function to decode TETRA signal'''
    # Initialize the decoder
    decoder = np.zeros_like(arg)
    
    # Use signal processing operations to decode the signal
    numSamp = arg.size
    for i in range(numSamp):
        if arg[i] > 0:
            decoder[i] = 1
        else:
            decoder[i] = 0
    
    # Return the decoded signal
    return decoder