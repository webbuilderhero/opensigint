# TODO: Research and plug in CTCSS Tonal System

# Libraries for handling signals
import scipy.signal
import scipy.fftpack
import numpy as np
import matplotlib.pyplot as plt

# Function for decoding CTCSS Tonal System
def ctcss_decode(signal):
    
    # Get frequency spectrum
    freq_spec = np.fft.fft(signal)
    
    # Set up CTCSS frequency "zones"
    freqs_ctcss_1 = [67.0, 71.9, 74.4, 77.0, 79.7, 82.5, 85.4, 88.5, 91.5, 94.8]
    freqs_ctcss_2 = [97.4, 100.0, 103.5, 107.2, 110.9, 114.8, 118.8]
    freqs_ctcss_3 = [123.0, 127.3, 131.8, 136.5, 141.3]
    freqs_ctcss_4 = [146.2, 151.4, 156.7, 162.2]
    freqs_ctcss_5 = [167.9, 173.8, 179.9]
    freqs_ctcss_6 = [186.2, 192.8]
    freqs_ctcss_7 = [203.5, 206.5]
    freqs_ctcss_8 = [210.7, 218.1]
    freqs_ctcss_9 = [225.7, 229.1]
    freqs_ctcss_10 = [233.6, 241.8]
    
    # Find peak values for each CTCSS "zone"
    peak_1 = np.amax(freq_spec[freqs_ctcss_1])
    peak_2 = np.amax(freq_spec[freqs_ctcss_2])
    peak_3 = np.amax(freq_spec[freqs_ctcss_3])
    peak_4 = np.amax(freq_spec[freqs_ctcss_4])