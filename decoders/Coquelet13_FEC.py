# TODO: Decode Coquelet-13 FEC

"""
This script will decode the Coquelet-13 Forward Error Correction (FEC). 
The FEC is a form of error-correction coding that adds redundant information to a signal to allow it to be transmitted reliably and accurately.

The script takes as input a signal that has been encoded with the Coquelet-13 FEC and outputs an error-free version of the signal.
"""

def decodeCoquelet13FEC(signal):
    # Calculate the number of parity bits
    parity_bits = 13

    # Check to make sure the signal is the correct length 
    if len(signal) % (parity_bits + 1) != 0:
        # Signal is not the correct length
        return None

    # Initialize the decoded signal list
    decoded_signal = []

    # Iterate through the signal one bit at a time
    for i in range(0, len(signal), parity_bits + 1):
        # Obtain the index of the data bit 
        bit_index = i + parity_bits

        # Check if the parity bits match the data bit
        matched_parity_bits = True
        for j in range(0, parity_bits):
            if signal[i + j] != signal[bit_index]:
                matched_parity_bits = False
                break

        # If the parity bits match the data bit, it is error free
        if matched_parity_bits:
            decoded_signal.append(signal[bit_index])

    return decoded_signal