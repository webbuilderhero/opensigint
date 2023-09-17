"""
This Python script provides a decoder for Tadiran AutoCall digital protocol signal intelligence (SIGINT). 

# TODO: Add imports for necessary libraries

# imports
import numpy as np
import struct

def decode_autocall(sigint):
    """
    decode_autocall(sigint) accepts a SIGINT signal and decodes the Tadiran AutoCall protocol

    Parameters
    ----------
    sigint : numpy.ndarray
        An array of complex numbers representing a SIGINT signal

    Returns 
    -------
    message : str 
        The decoded message 
    """

    # TODO: Check if input is valid 

    # Define symbols 
    symbols = {
        0: '000', 
        1: '001', 
        2: '010', 
        3: '011', 
        4: '100', 
        5: '101',
        6: '110',
        7: '111'
    }

    # TODO: Extract signal data from the array of complex numbers 
    signal = np.abs(sigint)

    # TODO: Define codewords 
    codewords = {
        '000': '0000', 
        '001': '0001', 
        '010': '0010', 
        '011': '0011', 
        '100': '0100', 
        '101': '0101',
        '110': '0110',
        '111': '0111', 
    }

    # TODO: Extract symbols from signal
    symbol_data = []
    for i in range(len(signal)): 
        # TODO: Get rid of noise
        if signal[i] > 0.5:
            # TODO: Calculate the symbol 
            if signal[i] < 0.75:
                symbol = 0 
            else:
                symbol = 1 

            symbol_data.append(symbol)

    # TODO: Convert symbols to binary string
    binary_string = ''
    for s in symbol_data:
            binary_string += symbols.get(s)