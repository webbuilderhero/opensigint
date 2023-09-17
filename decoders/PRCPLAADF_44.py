# TODO: Find a good Gardner decoder for PLAADF 4+4

"""
A decoder for PLAADF 4+4 RF signal intelligence

This decoder will take in an array of radio frequency (RF) data,
and decode it to its payload using the PLAADF 4+4 format.

PLAADF 4+4 format is a three-bit phase shift, alternating between 0 degrees and 90 degrees along with an 8-bit data field per bit period, and this decoder will use this format to decode the data field of an RF signal.

Input:
    - rf_data: An array of integers representing the radio frequency data.

Return:
    - decoded_data: An array of bytes decoded from the RF data using the PLAADF 4+4format.

"""

import numpy as np


def paaadf_decoder(rf_data):
    # Initialize decoded data
    decoded_data = []

    # Get size of the rf_data array
    n = len(rf_data)

    # Make a copy of the array and change it to numpy array 
    # for easier manipulation
    rf_data_copy = np.asarray(rf_data)

    # Iterate through all the elements of the array
    for i in range(0, n):
        # Initialize counter
        cnt = 0

        # Check the neighborhood of each element
        for j in range(i-3, i+3):
            # Make sure to take wrap-arounds into account
            if j < 0:
                if rf_data_copy[n + j] == rf_data_copy[i]:
                    cnt += 1
            elif j > n - 1:
                if rf_data_copy[j - n] == rf_data_copy[i]:
                    cnt += 1
            else:
                if rf_data_copy[j] == rf_data_copy[i]:
                    cnt += 1

        # If the counter is even then assign a zero
        if cnt % 2 == 0:
            decoded_data.append(0)
        #