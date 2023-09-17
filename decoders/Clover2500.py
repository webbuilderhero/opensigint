"""
clover2500 script

# TODO:
- Figure out the applicable frequency bands and modulation types for the Clover 2500. 

# Imports
import numpy as np
import pandas as pd
import scipy as sp
from scipy import signal
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

# Initializing data array
data_array = []

# Clover 2500 params 
frequency_band_min = 5E9 # GHz
frequency_band_max = 7E9
modulation_types = ['WBFM', 'AM', 'FM']

# Defining function to identify peaks (as per the modulation type)
def peak_detector(data, modulation):
    """Identifying signal peaks depending on modulation type"""
    # New array initialized
    new_data = []
    if modulation == 'WBFM':
        peak_idx, _ = find_peaks(data, height=None) # Low pass filter 
        new_data = peak_idx
    elif modulation == 'AM':
        peak_idx, _ = find_peaks(data, height=2)
        new_data = peak_idx
    elif modulation == 'FM':
        peak_idx, _ = find_peaks(data, height=0.01, width=1) # Hysteresis filter 
        new_data = peak_idx
    return new_data

# Function to process I/Q data within frequency range
def processing(freq_start, freq_end):
    """ Processing the I/Q data between given frequencies and for specific modulation types """
    for mod in modulation_types:
        # Filtering Signal 
        waveform = sp.signal.firwin(numtaps=32, cutoff=range(freq_start, freq_end), window='hamming', pass_zero=False) 
        filtered_data = np.convolve(waveform, data_array)
        # Identifying Peaks
        new_data = peak_detector(filtered_data,mod)
        # Plotting
        plt.plot(fil