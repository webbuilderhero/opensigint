"""Decoder for R-101-5

# TODO: Determine signal strength
"""

import numpy as np

def decode_R101_5(signal):
    """Decodes the signal for R-101-5"""
    decoded_output = list()

    # parse in signal data
    data_stream = signal.split('\n')

    # extract data from data
    for line in data_stream:
        frequency = line[0]
        amplitude = line[1]

        decoded_output.append({'frequency': frequency, 'amplitude': amplitude})

    return decoded_output