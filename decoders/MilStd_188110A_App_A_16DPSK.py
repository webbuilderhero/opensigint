"""Decoder for Mil-Std 188-110A App A 16DPSK Signal

# TODO: Research what 16DPSK is and figure out what's needed to decode it

import numpy as np

def dpsk_decode(signal):
    """Decoder for 16DPSK
    Params:
    signal (ndarray): Complex array of sample amplitudes
    
    Returns:
    data (ndarray): Complex numbers representing symbols of data
    """

    data = np.zeros(len(signal), dtype='complex128')

    # TODO: Research how to decode 16DPSK
    # Return blank array for now
    return data