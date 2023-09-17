# TODO: add function to handle decoding of tones longer than 12 bits

#import necessary libraries
import numpy as np
from scipy import signal

def zvei3_decoder(x):
    '''
    Decodes ZVEI3 Tones
    
    Parameters:
    x: input signal in the form of a numpy array 
    
    Returns:
    decoded_digits: a list of decoded ZVEI3 tones. Blank list if no valid ZVEI3 tone could be found.
    '''
	
    #shifts signal by 45 samples for filtering
    x_shifted = np.roll(x, 45)
    
    #low pass filter
    b, a = signal.butter(3, 0.25)
    x_filtered = signal.lfilter(b, a, x_shifted)
    
    #initialize parameters for loop
    decoded_digits = []
    sample_index = 0
    full_cycle = 400
    
    while sample_index + full_cycle < len(x):
        #create array of 12 samples for a full tone cycle to check for the highest peak
        sample_array = x_filtered[sample_index:sample_index + full_cycle]
        #find index of peak
        peak_index = np.argmax(sample_array)
        #calculate frequency of peak
        peak_frequency = peak_index/full_cycle * 19200
        #check if peak frequency is in valid tone range
        if peak_frequency >= 814 and peak_frequency <= 2009:
            #calculate digit from tone
            digit = int((peak_frequency - 814) / (19200 / 12))
            #add digit to list
            decoded_digits.append(digit)
            #add length of tone to sample index
            sample_index += full_cycle
        else:
            #add one sample to the sample index 
            sample_index += 1
            
    return decoded_digits