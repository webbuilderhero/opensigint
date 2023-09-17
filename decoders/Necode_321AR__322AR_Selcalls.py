'''
# TODO: Fill in with Python code for decoding Necode 321AR & 322AR Selcalls
 
# Imports
import numpy as np
 
# Necode 321AR & 322AR Selcalls Decoder
def decode_necodeselcall(signal):
    """
    Function to decode Necode 321AR & 322AR Selcalls.
    
    Args:
        signal (numpy.ndarray): The raw signal as a numpy array.
    
    Returns:
        tuple (string, float): The decoded selcall and signal strength.
    """
    # Check input signal type
    assert type(signal) == np.ndarray
    # Process signal, determine selcall, and return value
    # TODO:
    decoded_selcall = "" # Your code here for decoding
    signal_strength = 0.0 # Your code here for signal strength
    return (decoded_selcall, signal_strength)