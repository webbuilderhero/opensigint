# TODO: Contact framework for info on signal intelligence to replace with below

import numpy as np 

# BPSK125 stands for Binary Phase Shift Keying with a 125 Hz modulation rate
# Definition of BPSK - Modulation technique in which digital information is encoded by varying the phase of a carrier wave. 

def BPSK125(input):  
    '''
    This function will decode a Binary Phase Shift Keying modulation technique with a 
    125 Hz frequency.
    
    input is a numpy array representing a signal
    output is the decoded signal
    '''
    
    # Initializing variables
    output = []
    bit_width = np.pi/(125*2) # The duration of one bit of the signal
    signal_width = bit_width/2 # The duration from the start/stop of the bit
    
    # To start the decoding, loop over the array
    for bit in range(0, len(input), bit_width):
        value = input[bit]
        # If the start of the bit is seen and its value is lower than the signal_width
        # then the corresponding bit is equal to 0
        if value < signal_width:
            output.append(0)
            
        # If the start of the bit is seen and its value is higher than the signal_width
        # then the corresponding bit is equal to 1
        else:
            output.append(1)
    
    # Return the decoded signal
    return np.array(output)