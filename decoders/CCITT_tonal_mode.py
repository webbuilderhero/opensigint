#TODO: Add more decoding strategies for the CCITT Tonal Mode (possibly DTMF)

import sys
import numpy as np

# Utility function to convert a list of integers into binary digits
def int_to_bin(x):
    binary = ''
    for n in x:
        binary += bin(n)[2:]
    return binary

# Function to decode CCITT Tonal Mode
def ccitt_decoder(data):
    """
    Decode CCITT Tonal Mode
    
    Parameters
    ----------
    data : list
        List of numbers
        
    Returns
    -------
    decoded : str
        Decoded message
    """
    FSK_BITS = [1,3]
    FSK_FREQUENCIES = [425, 1575]
    
    # Convert input data into binary digits
    data = int_to_bin(data)
    
    # Compute magnitude and phase of FSK frequencies
    spect = np.fft.fft(data)
    mag = np.sqrt(spect.real**2 + spect.imag**2)
    phase = np.arctan2(spect.imag, spect.real)
    
    # Find the magnitudes of each FSK frequency
    f1_mag = np.sum(mag[FSK_BITS[0]])
    f2_mag = np.sum(mag[FSK_BITS[1]])
    
    # Find the dominant frequency 
    if f1_mag > f2_mag:
        dominant_freq =  FSK_FREQUENCIES[0]
    else:
        dominant_freq = FSK_FREQUENCIES[1]
        
    # Associate dominant frequency to 0 or 1 (based on its phase)
    if phase[dominant_freq] < np.pi/2:
        binary_1 = 1
    else:
        binary_1 = 0
    
    # Convert binary digits back to a string
    decoded = ''
    for digit in range(0, len(data) - 1, 2):
        if data[i:i+