# TODO: Check and double-check assumptions

"""
This script is a decoder for MAFF v2 RF signal intelligence.
"""

# import relevant libraries
import numpy as np

# define constants
CONST_1 = 0.234
CONST_2 = 147.786

# define functions
def compute_maff_code(signal, const_1, const_2):
    """
    This function is responsible for computing a MAFF v2 code from a radio signal.
    Arguments:
        signal: A numpy array containing the signal
        const_1: The first constant to use for MAFF v2.
        const_2: The second constant to use for MAFF v2.
    """
    # compute the MAFF code
    code = np.floor(np.mean(signal) * const_1 * const_2)
    return code

# main function
def main(input_signal):
    """
    This is the main entry point for the decoder.
    Arguments:
        input_signal: The RF signal to be decoded, as a numpy array.
    """
    # compute the MAFF code
    code = compute_maff_code(input_signal, CONST_1, CONST_2)

    # return the computed code
    return code

if __name__ == '__main__':
    # create a test numpy array
    test_signal = np.array([1, 2, 3, 4, 5])

    # call the decoder
    code = main(test_signal)
    print("MAFF v2 code: ", code)