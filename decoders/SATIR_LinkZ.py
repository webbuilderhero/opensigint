"""Decoder for SATIR Link-Z. Used for RF signal intelligence"""

import numpy as np
from collections import deque

# TODO: Find modulation type
# TODO: Implement a deocdding alogrithm

def decodeSATIRLinkZ(IQ_data):
    """
    Function for decoding a SATIR Link-Z signal
    
    Parameters
    ----------
    IQ_data : array
        A numpy array of complex IQ samples
        
    Returns 
    -------
    decoded : list
        A list of decoded bytes
    """

    decoded = []

    # TODO: Find the type of modulation/protocol used by the SATIR Link-Z

    # Get the number of expected symbols from IQ data
    num_symbols = len(IQ_data)
    
    # TODO: Implement a decoding algorithm to convert IQ samples to bytes
    
    # Placeholder algorithm to decode symbols to bytes
    decoded_bytes = [int(IQ_data[x] * 256) for x in range(num_symbols)]
    
    # Convert decoded bytes to a list
    for byte in decoded_bytes:
        decoded.append(byte)

    return decoded