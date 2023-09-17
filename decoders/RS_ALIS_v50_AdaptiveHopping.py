#TODO: Identify the type of data output

#Decoder for R&S ALIS v50 Adaptive+Hopping

#Define libraries/modules
import numpy as np
from scipy.signal import hilbert
import matplotlib.pyplot as plt

#Define function to demodulate the data
def demodulate(data, baud, oversample):
    '''Demodulates the data based on incoming baud rate and oversampling ratio
     
    Arguments:
    data -- array of received samples
    baud -- baud rate, i.e. number of samples per symbol
    oversample -- ratio of samples per symbol
     
    Outputs:
    samples_demodulated -- array of demodulated samples'''
    
    samples_demodulated = []
    for i in range(int(oversample*baud)):
        samples_demodulated.append(np.mean(data[i::int(oversample*baud)]))
    return samples_demodulated

#Define function to decode the data
def decode(data, baud, rise_threshold, fall_threshold):
    '''Decodes the data based on incoming baud rate and thresholds
     
    Arguments:
    data -- array of demodulated samples
    baud -- baud rate, i.e. number of samples per symbol
    rise_threshold -- upper threshold
    fall_threshold -- lower threshold
     
    Outputs:
    symbols -- array of decoded symbols'''
    symbols = []
    sample_count = 1
    prev_val = 0
    for sample in data:
        if sample_count < baud:
            if sample > rise_threshold and prev_val == 0:
                symbols.append(1)
            elif sample < fall_threshold and prev_val == 0:
                symbols.append(0)
            prev_val = sample
            sample_count += 1
        else:
            sample_count = 1
            prev_val = sample
    return symbols

#Define function to apply the hilbert transform
def hilbert_transform