#TODO: Solve for how to interface with RF hardware

#import statements
import numpy as np
import scipy.signal

def SuperNeT_ST2300_decoder(signal):
    # Define filter
    bw = 1000  # estimated bandwidth
    transition_bandwidth = 200
    stopband_attenuation = 40
    fs = signal.sample_rate  # sampling rate of signal

    N, beta = scipy.signal.kaiserord(stopband_attenuation, transition_bandwidth/bw)
    taps = scipy.signal.firwin(N, bw/fs, window=('kaiser', beta))
    # Filter signal
    filtered_signal = scipy.signal.lfilter(taps, 1.0, signal.data)

    # Demodulation
    demod_signal = scipy.signal.complex_demodulation(filtered_signal, fs=signal.sample_rate, demod_type='AM')

    # Downsampling
    downsampled_signal = scipy.signal.downsample(demod_signal, 8)
   
    # Decoding
    # TODO: Find encoding scheme and figure out how to decode
    
    return(decoded_signal)