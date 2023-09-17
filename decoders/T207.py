"""
T-207 Decoding Script 
Author: 

# TODO: 
#    - Implement error handling.

# Import modules
import numpy as np

# Define constants
MODCOD = [[1,1], [1,-1], [-1,-1], [-1,1]]

# Function to decode the signals
def decode(signal): 
    # Initialize variables
    decoded_signal = np.zeros(len(signal))
    carrier_idx = 0
    symbol_idx = 0
    modul_idx = 0

    # Decode the signal
    for k in range(len(signal)): 
        if (k % 2 == 0): 
            carrier_idx = signal[k] 
        else: 
            symbol_idx = signal[k]
            if (carrier_idx == 0): 
                decoded_signal[k-1] = MODCOD[symbol_idx][modul_idx]
            else: 
                decoded_signal[k-1] = MODCOD[symbol_idx][modul_idx] * (-1)
            modul_idx = (modul_idx + 1) % 2

    return decoded_signal