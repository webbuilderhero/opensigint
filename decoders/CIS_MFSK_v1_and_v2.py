"""
# TODO:
1. Add more complete documentation for this script.

2. Implement the frame-detection, error-correction and decoding algorithms for the two versions of CIS MFSK.
"""

import numpy as np

def mfsk_decoder_v1(raw_signal):
    """
    Decode a given CIS MFSK v1 encoded signal.
    
    Parameters:
    raw_signal (numpy array): raw signal to decode
    
    Returns:
    decoded_signal (string): decoded text
    """
    # Perform frame-detection and error-correction
    # TODO
    
    # Decode signal
    # TODO

    # Return decoded signal
    return decoded_signal
 

def mfsk_decoder_v2(raw_signal):
    """
    Decode a given CIS MFSK v2 encoded signal.
    
    Parameters:
    raw_signal (numpy array): raw signal to decode
    
    Returns:
    decoded_signal (string): decoded text
    """
    # Perform frame-detection and error-correction
    # TODO
    
    # Decode signal
    # TODO

    # Return decoded signal
    return decoded_signal

def decode_cis_mfsk(raw_signal):
    """
    Decode the given CIS MFSK encoded signal, identifying if it is MFSK v1 or v2.
    
    Parameters:
    raw_signal (numpy array): raw signal to decode
    
    Returns:
    decoded_signal (string): decoded text
    """
    # Determine if signal is MFSK v1 or v2
    # TODO
    
    if version == 1:
        decoded_signal = mfsk_decoder_v1(raw_signal)
    elif version == 2:
        decoded_signal = mfsk_decoder_v2(raw_signal)
    else:
        raise ValueError("Unknown MFSK version for decoding.")