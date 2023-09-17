# TODO: Flesh out the functions in this script

import numpy as np

def BPSK31_decoder(rawdata, symrate=25):
    # TODO: Need more information on what "rawdata" will look like (sampling rate?)
    
    # Downsample the data to recover bits
    downsampled = rawdata[::symrate]
    
    # Convert bits to symbols
    symbols = np.array([1 if i > 0 else 0 for i in downsampled])
    
    # Return symbols
    return symbols