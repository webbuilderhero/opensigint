# TODO: Test script

# This script is a decoder for DSP-QUICK II. 

#import necessary libraries
import signal
import time
import numpy as np

#Define necessary functions

def decode_signal(fft, fs, W):
    """
    Args:
        fft : fft of the signal
        fs : sampling frequency
        W : Window size
    Returns:
        message : decoded message
    """  
    
    #convert from fft to time domain by applying inverse fft
    time_data = np.fft.ifft(fft)
    
    #perform downsampling to get frequency in the range of DSP-QUICK II
    downsample_factor = int(np.power(2,W)) #Coefficient set by window size W 
    time_data = time_data[::downsample_factor] 
    
    # Get approximate symbol rate
    symbol_rate = 1/((fs/downsample_factor)/W)
    
    # Apply Root-raised cosine filter with default roll-off factor 
    # to get better result
    from scipy import signal
    b = signal.firwin(numtaps=31, cutoff=symbol_rate, 
                      window = 'blackman',
                      fs=fs/downsample_factor)
    filtered_signal = signal.lfilter(b, [1], time_data)
    
    # Get decimation value 
    decimation = int(round(1500/symbol_rate))
    
    # Decimate signal to get 1600Hz audio frequency 
    filtered_signal = filtered_signal[::decimation]
    
    # Define symbols to be used for decoding
    symbols = { 1 + 1j : '0', 
                1 - 1j : '1', 
                -1 + 1j : '2',  
                -1 - 1j : '3' }
   
    # Threshold for selecting particular symbol    
    threshold = 0.5
    
    # Decode the message
    message = ''
    for sample in filtered_signal