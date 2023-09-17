# TODO: Research algorithm, RF signal filtering, & noise cancellation methods 

import numpy as np 
import scipy as sp
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize

# Define constants
SAMPLING_RATE = 250000  # Sampling rate in Hz
FREQUENCY_COLLECT = 1000  # Frequency resolution in Hz

# Define tone frequencies used in DTMF
TONES = {
    '1': 697,
    '2': 770,
    '3': 852,
    'A': 941,
    '4': 1209,
    '5': 1336,
    '6': 1477,
    'B': 1633,
    '7': 1633,
    '8': 1633,
    '9': 1633,
    'C': 1633,
    '*': 1633,
    '0': 1633,
    '#': 1633,
    'D': 1633
}

CHANNEL_COUNT = 3 # Takes 3 channels: I, Q, and code 

# Filtering to eliminate noise from DTMF signal
def filter_signal(signal):
    filtered_signal = signal
    filtered_signal[np.abs(signal) < np.std(signal)] = 0
    return filtered_signal

# designs a filter given a cutoff frequency
# and applies it to the signal
def apply_filter(signal, cutoff):
    nyq = 0.5 * SAMPLING_RATE
    normal_cutoff = cutoff / nyq
    b, a = sp.signal.butter(5, normal_cutoff, btype='low', analog=False)
    output = sp.signal.filtfilt(b, a, signal)
    
    return output   

# perform a fast fourier transform
def fft(data):
    return np.fft.fft(data)

# decode a DTMF signal
def decode(signal):
    # filter incoming signal
    filtered_signal = filter_signal(sign