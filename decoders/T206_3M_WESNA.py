# TODO: Figure out how to decode the WESNA message

# RF SIGINT Decoder for T-206 3M WESNA

# Import libraries
import numpy as np 
import pandas as pd

# Define RF SIGINT Decoder Function
def rf_sigint_decoder(message):
    """
    Take in a RF message encoded using the T-206 3M WESNA signal standard, and decode it.
    
    Parameters
    ----------
    message : str
        An encoded RF message.
        
    Returns
    -------
    decoded_msg : str
        The decoded message.
    """
    
    # Initialize empty output strings
    decoded_msg = ""
    current_char = ""
    
    # Calculate length of message
    num_bits = int(len(message) / 2)
    
    # Initialize data frame to store each bit pattern
    bit_patterns = pd.DataFrame(np.ones(shape=(num_bits, 2)), columns=["first_bit", "second_bit"])
    
    # Parse out bits into data frame
    for bit in range(num_bits):
        bit_patterns.iat[bit, 0] = message[2 * bit]
        bit_patterns.iat[bit, 1] = message[2 * bit + 1]
    
    # Map message bits to the corresponding characters according to the T-206 3M WESNA signal standard
    for i in range(num_bits):
        if bit_patterns.iat[i, 0] == 'T' and bit_patterns.iat[i, 1] == 'M':
            current_char = 'a'
        elif bit_patterns.iat[i, 0] == 'T' and bit_patterns.iat[i, 1] == 'N':
            current_char = 'b'
        elif bit_patterns.iat[i, 0] == 'T' and bit_patterns.iat[i, 1] == 'K':
            current_char = 'c'
        elif bit_patterns.iat[i, 0] ==