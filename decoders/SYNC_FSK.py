"""
SigInt: SYNC FSK Decoder

TODO:
- Come up with algorithm for discerning symbols
- Figure out timing 
- Signal processing to amplify FSK

"""

# import necessary libraries
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# define constants
SYNC_CODES = {0 : [1, 1, 0, 0],    # change accordingly to what the sync codes are
              1 : [1, 0, 0, 1]}

# function to perform FSK decoding
def sync_fsk_decoder(input_signal):
    '''
    This function will decode an FSK signal assuming a SYNC code i.e. different code for a 0 and 1.
    
    Parameters
    ----------
    input_signal : 1D-array
        The input RF signal
        
    Returns
    -------
    encoded_data : list
        List of decoded symbols
    '''
        
    # initialize the decoded_data list
    decoded_data = []
    
    # TODO: Add signal processing methods to amplify FSK component
    
    # TODO: Implement algorithm for timing and sampling
    
    # Create a sliding window (or use scipy window) to sample the signal
    for i in range(len(input_signal)):
        sample_window = input_signal[i:i+4]
        
        # check if it matches with any of sync codes
        for key, code in SYNC_CODES.items():
            if list(sample_window) == code:
                decoded_data.append(key)
                break
    
    return decoded_data