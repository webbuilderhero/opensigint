""" RF Decoder for Sigint framework 
@todo: Figure out exact details for T-206MT WESNA
"""

import scipy as sp
import numpy as np 

#Define constants 
SAMPLE_FREQ = 512 #Sample frequency 
FREQ_START = 256 #Frequency Start
FREQ_END = 284 #Frequency End 

#Define functions 
# Take in array of complex samples and decode
def t206mt_wesna_decoder(samples):
    
    # Initialize output
    output = []
 
    # Check for valid input
    if(samples.size != SAMPLE_FREQ):
        return output
 
    # Sum all points within frequency range
    sig_sum_real = 0.0
    sig_sum_img  = 0.0
    for i in range(FREQ_START, FREQ_END):
        sig_sum_real += samples[i].real
        sig_sum_img  += samples[i].img

    # Calculate angle 
    angle = np.arctan2(sig_sum_img, sig_sum_real)

    # Different message types are a fixed number of degrees away from the start
    if (angle > 0 and angle < np.pi/4):
        output.append("Message Type 1")

    elif (angle > np.pi/4 and angle < np.pi/2):
        output.append("Message Type 2")

    elif (angle > np.pi/2 and angle < np.pi*3/4):
        output.append("Message Type 3")

    else:
        output.append("Message Type 4")
        
    # Return output
    return output