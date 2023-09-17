# TODO: Calibration setup

import struct
import numpy as np

# This function will decode data from the Selex H700 module
def decode_Selex_H700(data):
    # Parse raw data into numpy array
    data = np.fromstring(data, dtype=np.int8)

    # TODO: Calculate the size of the header
    header_size = 0

    # Parse header information
    header_data = data[:header_size] # TODO: Add header fields
    # TODO: Process header data

    # Calculate the length of the payload
    payload_len = len(data) - header_size

    # Parse payload data
    payload_data = data[header_size:]

    # TODO: Decode payload data
    decoded_data = None # TODO: Add decoded data

    # Return decoded data
    return decoded_data