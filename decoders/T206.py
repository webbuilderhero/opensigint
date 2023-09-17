"""
# TODO: Flesh out script with connections to framework

# Decoder for T-206 Signal

# Defining modules for use in script
import numpy as np
import matplotlib.pyplot as plt

# Inputs
audio_input = [] # Audio Input 

# Processing
# 
# Run Audio Input through frequency filtering to isolate signal
freq_filtered = signal.lfilter(audio_input)

# Split filtered signal into multiple bands
band1, band2, band3 = np.array_split(filtered_signal, 3)

# Vin Code Decoding 
# 
# First Define Vin symbols
one = [True, False, False] # Symbol representing 1
zero = [False, True, False] # Symbol representing 0
marker = [True, True, False] # Symbol separating words

def decode_vin(freq_filtered):
    decoded_vin = [] # Output variable
    bands = np.array_split(freq_filtered, 3)
    
    # Iterate through frequency bands, building up VIN number
    for band in bands:
        if band == one:
            decoded_vin.append('1')
        elif band == zero:
            decoded_vin.append('0')
        elif band == marker:
            # Marker seen. Complete VIN from number and add to list
            vin_num = ''.join(decoded_vin)
            decoded_vin.append(vin_num)
    # Return 
    return decoded_vin 

# Connect to framework
decoded_vin = decode_vin(freq_filtered) # Use decode_vin function to decode Vin 
# Send decoded Vin number to framework