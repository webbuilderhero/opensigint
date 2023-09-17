"""Decoder for Pactor-II"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
#TODO: Code for filtering
#TODO: Code for pulse separation
#TODO: Code for variable-speed predictive coding

def decode_pactor_II(x, Fs):
    """
    Decodes a signal received by Pactor-II 
    
    Parameters
    ----------
    x : ndarray
        The signal received by Pactor-II.
    Fs : int
        The sampling rate in Hz.
    
    Returns
    -------
    decoded_message : str
        The decoded message.
    """
    
    # Step 1: Filter the input signal
    # Use a Butterworth filter to remove noise
    b, a = signal.butter(10, 1/(Fs/2), 'low')
    x_filtered = signal.lfilter(b, a, x)
    
    # Step 2: Find the pulse edges
    # Use the filtered signal to find the edges of pulses
    edges = signal.find_peaks(x_filtered, height=0)[0]
    
    # Step 3: Separate pulses
    # Using the pulse edges, break the signal into separate pulses
    pulses = []
    for i in range(len(edges)-1):
        pulse = x_filtered[