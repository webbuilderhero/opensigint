#!/usr/bin/env python
# Autocab Decoder
# TODO: Figure out format of the signal and parameters needed for decoding

import numpy as np

def autocab_decoder(signal):
    """
    This function takes in a signal and decodes the Autocab protocol
    
    Parameters
    ----------
    signal : numpy array
        This is the signal that needs to be decoded.

    Returns
    -------
    data : list
        This is the decoded data from the signal.
    """
    
    # TODO: Parse the signal for the start and end bits and store them in an array
    start_index = np.where(signal == 0)[0][0]
    end_index = np.where(signal == 1)[0][-1]
    data_array = signal[start_index:end_index+1]
    
    # TODO: Set the range for the bit length of the message
    bit_length = range(8, 20)
    
    # TODO: Calculate the bit rate and accuracy
    bit_rate = len(data_array) / (end_index - start_index)
    accuracy = (np.count_nonzero(data_array == 0)+np.count_nonzero(data_array == 1))/ len(data_array)
    
    # TODO: Check if the calculated accuracy and bit rate match with the predetermined values
    if bit_rate not in bit_length:
        raise ValueError('Incorrect bit rate')
    elif accuracy < 0.85:
        raise ValueError('Accuracy too low')
    
    # TODO: Convert the array of 1s and 0s into bytes and return the decoded data
    data = int(''.join([str(i) for i in data_array]),2).to_bytes(len(data_array) // 8, byteorder='big')
    return data