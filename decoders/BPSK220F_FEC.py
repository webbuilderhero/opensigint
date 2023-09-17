#TODO: Implement FEC decoding
#TODO: See relevant RFCs for details on BPSK220F signal

import numpy as np

def BPSK220Fdecode(signal_data):
    """
    Decodes BPSK220F signals

    Args:
        signal_data: The raw data from the RF signal in an
        array.

    Returns:
        decoded_data: The decoded signal from the given RF signal 
        data.
    """

    # TODO: Implement FEC decoding
    
    # Initialize the decoded signal data
    decoded_data = []
    
    # Iterate through the signal data and decode
    for chunk in signal_data:
        # TODO: Find algorithm to decode BPSK220F signal
        decoded_chunk = algo(chunk)
        decoded_data.append(decoded_chunk)
    
    return decoded_data