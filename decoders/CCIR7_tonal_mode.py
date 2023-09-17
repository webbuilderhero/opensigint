"""
SIGINT DECODER: CCIR-7 TONAL MODE
Author: 
Date: 

#!/usr/bin/env python3

# TODO: Import necessary libraries
import math

# TODO: Define any constants
PI2 = math.pi * 2 # represents 2*PI
T_OFFSET = 0.0     # time offset
T_LIMIT = 1.0      # time limit

def decode_ccir_7_tone(data):
    """
    Decodes the CCIR-7 Tone mode signal in the received data and
    returns the decoded signal in form of ascii
    
    Parameters:
        data : received signal data 

    Returns:
        ascii_string : decoded ascii string 
    """
    ascii_string = ""
    # TODO: Implement main logic
    # 1.Check if the tone is in the required range
    # 2.Detect the first and last zero crossings
    # 3.Calculate frequency and duty cycle from the zero crossings 
    # 4.Look up the numbers from the lookup table
    # 5. Extract the four most probable symbols  
    # 6. Choose the maximum frequency 
    # 7. Convert the frequency to number
    # 8. Append the character to the asci characters string
    
    return ascii_string

if __name__ == "__main__":
    # TODO: Input and preprocessing
    
    # TODO: Get decoded signal 
    decoded_signal = decode_ccir_7_tone(data)

    # TODO: Post-processing and Output