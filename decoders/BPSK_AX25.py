# TODO: Determine phase transitions

# Decoding script for BPSK AX.25
import numpy as np

def perform_decoding(arr):
    """Decoding script for BPSK AX.25

    Parameters
    ----------
    arr : np.array
        signal to decode

    Returns
    -------
    decoded_str : str
        Decoded signal string

    """
    # Get the signal 
    signal = arr
    
    # Initialize threshold
    threshold = 0.5
    
    # Initialize decoded string
    decoded_str = ""
    
    # Step through each bit in the signal
    for bit in signal:
        # Decode bit, using mean as reference
        bit_value = 0
        if (bit > threshold):
            bit_value = 1
        
        # Append bit_value (0 or 1) to decoded string
        decoded_str = decoded_str + str(bit_value)
        
    return decoded_str