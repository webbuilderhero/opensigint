#todo create a class to standarize outputs from the decoder

"""
This script is designed to decode Akula-I RF signals for SIGINT purposes.
"""

import numpy as np
import scipy as sp

# Define constants used in decoding Akula-I
DEFAULT_PROTOCOL = "A-I"
MAX_SPECTRAL_SIZE = 1024
BASE_FREQUENCY = 40000
BW_DEVIATION = 3000

def read_spectrum(infile):
    """ Read spectrum from text file and return array containing data points"""
    data = []

    # Read file line by line
   with open(infile) as fh:
        for line in fh:
            line = line.strip()
            if line:
                data.append(line)
    
    # Convert data to numpy array
    data = np.asarray(data, dtype=np.float32)

    # Check if data fits the expected spectrum size
    if data.shape[0] > MAX_SPECTRAL_SIZE:
        raise ValueError("Spectral size is too large")

    return data


def decode_spectral_points(spectral_points):
    """ 
    Decode the spectral points of an Akula-I signal based on the prescribed protocol
    Returns decoded message in bit array
    """
    # Initialize empty array for decoded bits
    message_bits = np.zeros((MAX_SPECTRAL_SIZE, ), dtype=np.int8)

    # Iterate through spectral points
    for i in range(spectral_points.shape[0]):
        # Default to 0 if the point is lower than base frequency 
        if spectral_points[i] < (BASE_FREQUENCY - BW_DEVIATION):
            message_bits[i] = 0
        # Otherwise set the bit to 1
        else:
            message_bits[i] = 1

    return message_bits


def decode_akula_i(infile):
    """ 
    Decodes an Akula-I signal from an input file 
    Returns decoded message in bit array