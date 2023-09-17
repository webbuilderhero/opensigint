'''
# TODO: Define configuration settings needed to decode HF signals

# TODO: Add software functions for signal analysis

# TODO: Import necessary libraries
import numpy as np
from scipy import signal

# TODO: Define global variables
dataLen = 1024               # sample size of buffered data
sampleFreq = 72000           # sampling frequency

# Global scope settings
averageWindowSize = 5        # size of the sliding window used for averaging
thresholdWinSize = 16        # size of threshold window width

# Initialization
# HF-9000 decoder
decoder = signal.remez(72,[0, 0.3, 0.46, 0.5],[1, 0])  #filter coefficients for hamming window

# Define functions for signal processing  
def lowPassFilter(x, printflag):
    # Apply HF-9000 decoder to signal
    y = np.convolve(x, decoder)
    return y

def averageFilter(x):
    # Apply windowed averaging filter on signal
    # Create window
    w = np.ones(averageWindowSize)/averageWindowSize
    # Filter signal
    y = np.convolve(x, w)
    return y

def thresholdFilter(x):
    # Create window
    w = np.ones(thresholdWinSize)/thresholdWinSize
    # Filter signal
    y = np.convolve(x, w)
    # Set threshold
    y[y<0.15] = 0
    # Maximum level values
    y[y>1.0] = 1.0
    return y

# Decoder function
def hf9000Decode(x):
    # Low pass filter
    y = lowPassFilter(x, 0)
    # Averaging filter
    y = averageFilter(y)
    # Threshold filter
    y = thresholdFilter(y)
    return y