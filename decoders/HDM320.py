# TODO: Research HDM-320 to determine type of signal it broadcasts

# Decode HDM-320 signals
import numpy as np
import scipy.signal as sig

# Define relevant constants
sample_rate = 48000 # Samples per second

def decode_hdm320(data):
    '''Decode data from HDM-320 signal

    Parameters: 
    data (numpy array): signal data to decode

    Returns:
    decoded_data (numpy array): decoded signal data
    '''

    # TODO: Define filter coefficients for the bandwidth expected from the HDM-320 signal
    b,a = sig.iirdesign(2*np.array([0.1, 0.2])/sample_rate, 2*np.array([1.0, 1.1])/sample_rate, gpass=1, gstop=20)
    # Use signal processing package to apply filter to incoming data 
    decoded_data = sig.filtfilt(b, a, data)

    return decoded_data