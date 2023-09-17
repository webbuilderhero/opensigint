"""
This is a decoder script for facsimile transmissions over RF signal intelligence.

#TODO - Add functionality to detect and store the signal duration and size for each pulse.

import numpy as np

def decodeFacsimile(signal):
    # Store the signal properties
    duration = []
    size = []
    
    # Decode the signal using FAX 60-90-120-240 LPM
    for i in range(len(signal)-1):
        currentVal = signal[i]
        nextVal = signal[i+1]
        
        # Store the signal duration and size
        duration.append(np.abs(currentVal - nextVal))
        size.append(np.sign(currentVal-nextVal))
        
    # Interpret the facsimile signal using the Pulse Representation
    # Pulse Width:
    #   0.6 = 0 pulses
    #   0.9 = 1 pulses 
    #   1.2 = 2 pulses
    #   2.4 = 3 pulses
    # Pulse Magnitude:
    #   Positive = '1' bit
    #   Negative = '0' bit
    
    # Initialize output list
    output_bits = []
    
    for j in range(len(duration)):
        
        if duration[j] == 0.6:
            output_bits.append('0')
        elif duration[j] == 0.9:
            output_bits.append('1')
        elif duration[j] == 1.2:
            output_bits.append('2')
        elif duration[j] == 2.4:
            output_bits.append('3')
            
        if size[j] == 1:
            output_bits.append('1')
        elif size[j] == -1:
            output_bits.append('0')
            
    # Accuracy check
    accuracy = 0
    
    for k in range(len(output_bits)):
        if output_bits[k] == signal[k]:
            accuracy += 1
            
    accuracy = accuracy / len(output_bits) * 100
    
    return