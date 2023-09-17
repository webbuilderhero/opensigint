#TODO: Change the frequency range to the frequency range of the tone Selcalls

# Import required libraries
import re
import array
import numpy as np


# Function to decode a Tone Selcall signal   
def decode_tone_selcall(signal):

    # Define the various tone frequencies used in Selcalls
    tones = [674.0, 719.9, 770.0, 821.9, 873.0, 924.9, 976.0, 1027.9]

    # Initialitizes an array to store decoded output
    output = []

    # Checks if signal is a numpy array
    if type(signal) == np.ndarray:
        
        # Iterate over signal
        for bit in signal:

        # Checks if the bit is a tone frequency
            if bit in tones:

                # Append the bit to the output
                output.append(bit)

    # Checks if signal is an array
    elif type(signal) == array:

        # Iterate over the signal
        for bit in signal:

            # Checks if the bit is a tone frequency 
            if bit in tones:

                # Append the bit to the output
                output.append(bit)

    # Checks if signal is a string
    elif type(signal) == str:

        # Iterate over the signal
        for bit in signal:

            # Checks if the bit is a tone frequency 
            if re.findall(r"[0-9]{3}.[0-9]", bit)in tones:

                # Append the bit to the output
                output.append(bit)

    # Convert the output array into a string
    output_string = "".join(output)

    return output_string