#TODO: More research needed to understand for which frequency band this decoder is meant for.

#This script is a decoder for T-222, a RF signal intelligence decoder.

import numpy as np
import matplotlib.pyplot as plt

#Function to decode a T-222 signal:
def t222_decoder(signal_input):
    #TODO: More research needed to find out the length of the frame that we have to decode
    #Extract each bit of the frame
    signal_bits = []
    for bit in range(len(signal_input)):
        signal_bits.append(signal_input[bit])
    
    #Decode the binary strings
    binary_string = ''
    for bit in signal_bits:
        binary_string += str(bit)
    decoded_message = ''
    for i in range(0, len(binary_string), 8):
        decoded_message += chr(int(binary_string[i:i+8], 2))

    return decoded_message