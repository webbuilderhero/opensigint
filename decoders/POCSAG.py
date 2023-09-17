'''
#!/usr/bin/python3
# TO-DO: Write functions to decode POCSAG

#importing relevant libraries
import numpy as np
from scipy import signal

def decode_POCSAG(signal):
    """
    Function to decode POCSAG signal
    input signal should be in array format

    Parameters:
    signal (array): Input signal

    Returns:
    decoded_message (string): Decoded Message

    @author:
    Debolina Dey, 06/05/2020
    """

    # TO-DO: Define code rate, symbol rate, and word rate 
    code_rate = 4200    
    symbol_rate = 512    
    word_rate = 1176    

    # TO-DO: Take input signal, convert it to frequency spectrum
    fft = np.fft.fft(signal)
   
    # TO-DO: Calculate the bandwidth
    start_freq = 0
    end_freq = code_rate/2
    bw = end_freq - start_freq

    # TO-DO: Separate POCSAG signal from noise by bandpass filter at 600 Hz
    b, a = signal.butter(3, [start_freq/bw, end_freq/bw], 'bandpass')
    POCSAG_signal_filtered = signal.filtfilt(b, a, fft)

    # TO-DO: Decode POCSAG
    decoded_message = '' #initialize output message
    ind_start = 0
    word_size = symbol_rate * 4 # POCSAG word size is 4 symbols. 576 bit per word
    while ind_start < len(POCSAG_signal_filtered):
        # create a single word
        word = POCSAG_signal_filtered[ind_start:ind_start+word_size]
        ind_start += word_size
        
        # get information bits
        info_bit_start = symbol_rate * 3    # first bit is start bit, leave it
        info_bits = word[