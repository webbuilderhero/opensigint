#TODO: Flesh out the framework for the decoder

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def decoder(signal_input):
    '''
    This function decodes a signal that has been transmitted in a facsimile 
    over different modes. This function accepts a signal_input and processes 
    it to determine the type of facsimile transmission that it is and 
    constructs the message from the signal. 
    
    Parameters
    ----------
    signal_input : array_like
        A set of data points representing a signal.
        
    Returns
    -------
    decoded_signal : array_like
        A decoded signal, depending on its facsimile transmission type. 
    '''
    
    # Get high and low frequency components
    nyq_rate = 0.5*np.mean(np.diff(signal_input)) 
    lowcut = 10/nyq_rate 
    highcut = 24/nyq_rate
    low_freq_sig = signal.fftconvolve(signal_input, signal.butter(3, lowcut, 'low'), mode='same')
    high_freq_sig = signal.fftconvolve(signal_input, signal.butter(3, highcut, 'high'), mode='same')
    
    n = len(signal_input) 
    t = np.arange(n) 
        
    # Detect type of facsimile transmission 
    if np.max(low_freq_sig) > 2 and np.max(high_freq_sig) < 2:
        decoded_signal = _decode_monochrome(signal_input, t, n)
    elif np.max(high_freq_sig) > 2 and np.max(low_freq_sig) < 2:
        decoded_signal = _decode_color(signal_input, t, n)
    else:
        decoded_signal = _decode_error_correction(signal