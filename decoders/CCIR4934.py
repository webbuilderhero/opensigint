# TODO: What does it mean when a signal has CCIR493-4

# Decoder for CCIR493-4
import numpy as np

def decode_CCIR493_4(signal):
    """
    Decodes a signal according to CCIR Recommendation 493-4
    
    Parameters:
        signal: a numpy array of the signal to be decoded
        
    Returns:
        A dictionary of the decoded signal
    """

    decoded_signal = {}
    # TODO: what all does this require?
    decoded_signal['call_sign'] = None
    decoded_signal['location'] = None
    decoded_signal['text'] = None

    # TODO: Write code to decode appropriate information from the signal
    # using CCIR Recommendation 493-4
    # ...
    
    return decoded_signal