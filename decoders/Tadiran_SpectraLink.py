# TODO: Include necessary imports/libraries

import numpy as np
import pandas as pd
import scipy
import scipy.signal as signal

# Function: decoder_tadiran_spectralink
# Parameters: 
# sample - a list of voltage values corresponding to a RF signal
# fs - sample rate of the signal 

# Purpose: Decodes a signal that has been sampled

def decoder_tadiran_spectralink(sample, fs):
 
    sample_length = len(sample) # Get the sample length
    start_pos  = 0 # Initialize starting position
    end_pos = 0 # Initialize ending position
    start_list = [] # Initialize a list to store starting positions
    end_list = [] # Initialize a list to store ending positions
    rf_signal_list = [] # Initialize a list to store all decoded signals
 
    # Iterate through sample to find start and end position of samples
    for i in range(sample_length-1):
 
        # Detect a start signal
        if sample[i] < 0 and sample[i+1] > 0:
            start_pos = i
 
        # Detect an end signal
        elif sample[i] > 0 and sample[i+1] < 0:
            end_pos = i+1
 
        # if start and end positions have been found append to list
        if start_pos != 0 and end_pos != 0:
            start_list.append(start_pos)
            end_list.append(end_pos)
            start_pos = 0
            end_pos = 0
 
    # Iterate through start and end position to detect impulses 
    for i in range(len(start_list)):
        impulse = sample[start_list[i]:end_list[i]] # get current impulse
    
        # Apply a bandpass filter to filter out noise and unwanted signals
        b, a = signal.butter(2, [float(10e3)/fs/2.0, float(200e3)/fs/2.0], 'bandpass')