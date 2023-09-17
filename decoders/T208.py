'''
#TODO: Add functions to decode signal for further details

import numpy as np

def signal_decoder(signal):
    #This function will decode a T-208 signal, an analog/digital multichannel communication format
    
    # Step 1: Separate signal into two components
    low_values, high_values = np.split(signal, [len(signal)//2])
    
    # Step 2: Get the byte length of the signal
    signal_binary = bin(int.from_bytes(low_values, byteorder='big'))[2:] + bin(int.from_bytes(high_values, byteorder='big'))[2:]
    
    # Return the converted binary data
    return signal_binary