#TODO: find information pertinent to the decoding of ZVEI2 Tone system

#Create decoder script for ZVEI2 Tone System
#importing necessary libraries
import pandas as pd
import numpy as np
import scipy as sp

#defining function
def decode_ZVEI2(tone):
    '''
    Function to decode a ZVEI2 Tone signal
    
    Tone should be a 1D array or a single value with 4 tones
    '''
    # Create dictionary to convert tones to numbers
    tone_dict={440: '0', 540: '1', 600: '2', 640: '3'}
    
    # Create empty variable to store the decoded signal
    decoded_signal = ''
    
    # Loop over the individual tones in the input
    for t in tone:
        # Convert the tone to a string
        tone_str = str(t)
        # Check if tone is a valid ZVEI2 tone
        if tone_str in tone_dict.keys():
            # Append the decoded number to the decoded signal
            decoded_signal += tone_dict[tone_str]
        else:
            # Throw error if tone is not a valid ZVEI2 tone
            raise ValueError('{} is not a valid ZVEI2 Tone'.format(t))
        
    # Return decoded signal
    return decoded_signal