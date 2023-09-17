#TODO: figure out how to decode Generic Synchronous FM / PCM Direct FM

import pandas as pd
import numpy as np

def pcm_direct_decode_fm(data, sample_rate = 1000):
    """Decodes PCM/Direct FM signal
    Parameters
    ----------
    data : numpy array
        The data to be decoded
    sample_rate : int, optional
        Sample rate of data. Default is 1000
        
    Returns
    -------
    decoded_data : numpy array
        Decoded data
    """
    
    #Create a time sequence
    time_seq = np.arange(0, len(data)) / sample_rate
    period = 1/sample_rate
    
    phases = [] # create empty list for phase values
    
    #Loop through the data and compute the phase shift at each point
    for i in range(len(data)):
        #calculate phase shift from previous data point
        if i == 0:
            #for first data point, assume previous timestamp to be 0
            prev_phase = 0
        else:
            prev_phase = phases[i-1]
        
        #Calculate current phase from previous phase
        new_phase = prev_phase + (data[i] * period)
        phases.append(new_phase)
    
    #convert list of phases to numpy array
    phases = np.array(phases)
    
    #Calculate the sampled amplitudes by taking the inverse of Fourier transform
    decoded_data = np.fft.ifft(phases).real
    
    return decoded_data