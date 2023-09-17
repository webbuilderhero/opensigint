# To Do
# - Obtain more information about the AT-3014D to identify any other relevant functions
# - Investigate relevant libraries that can be used to decode and process RF signals

import struct
import binascii
import numpy as np

def decode_AT_3014D(signal_data):
    bitwise_data = []
    
    # Convert signal data to bitwise representation
    for sample in signal_data:
        bitwise_data.append(struct.unpack('>f', binascii.hexlify(sample))[0])
        
    decoded_data = []
    
    # Decode signal using relevant algorithms based on information from manufacturer
    for value in bitwise_data:
        decoded_data.append(value)
        
    # Pre-process signal to reduce noise
    decoded_data = np.array(decoded_data)
    filtered_data = np.absolute(decoded_data)
    
    return filtered_data