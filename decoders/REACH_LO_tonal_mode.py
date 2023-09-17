# TODO: Add input parameter for Alice's signal wave type

"""
This file contains a decoder script for REACH LO, a tonal mode used in RF signal intelligence.
"""

import numpy as np
import scipy.signal

def decode(signal):
    """Decodes a REACH LO signal into binary data.
    
    Args:
        signal (numpy array): a numpy array containing the raw signal received from Alice.
        
    Returns:
        (list): a list containing strings of binary data decoded from the signal. 
    """
    
    # Load parameters for the signal
    baud_rate = 300 # number of symbols per second
    sample_rate = 4000 # samples per second
    
    # Filter the signal with Butterworth lowpass
    cutoff_freq = 900
    order = 11
    b, a = scipy.signal.butter(order, cutoff_freq, btype='lowpass', fs=sample_rate, output='ba')
    filtered_signal = scipy.signal.filtfilt(b, a, signal)
    
    # Rectify the filtered signal
    rectified_signal = np.absolute(filtered_signal)
    
    # Find "corners" in signal
    corners = scipy.signal.find_peaks(rectified_signal, height=100)[0]
    
    # Form chunks from the corners
    chunk_size = 1.2 / baud_rate * sample_rate
    chunks = np.split(rectified_signal[corners[0]:corners[-1]], len(corners))
    
    # Calculate Mean Squared Error for each chunk
    errors = [np.mean((chunks[i]-np.mean(chunks[i]))**2) for i in range(len(chunks))]
    
    # Convert the MSE into binary bit
    binary_bits = [1 if (errors[i] < np.mean(errors)) else 0 for i in range(len(errors))]
    
    return binary_bits