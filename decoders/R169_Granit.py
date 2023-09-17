# TODO: Find out what the exact frequency of the signal is 

#!/usr/bin/env python3

# This script decodes R-169 Granit RF signal intelligence

import numpy as np
from scipy.io import wavfile

def decode_R169Granit():
    # read in the signal data
    f = open('rf_signal.data', 'r')
    data = f.readlines()
    f.close()

    # iterate through the data stream and convert to floating point numbers
    signal_data = []
    for d in data:
        signal_data.append(float(d))
    
    # decode the signal using the appropriate algorithm for R-169 Granit
    decoded_data = []
    for i in range(0,len(signal_data)-1):
        #decode signal_data with appropriate algorithm here       
        decoded_data.append(decoded_data) #replace decoded_data with appropriate decodings
    
    # write decode data into a wav file
    sample_rate = 12000  # sample rate of the signal
    wavfile.write('decoded_signal.wav', sample_rate, np.asarray(decoded_data))

if __name__ == '__main__':
    decode_R169Granit()