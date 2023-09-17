#TODO: Test script

#Decoder for T-310 RF signal

import numpy as np
import scipy.signal as signal

def T310Decoder(signal):
    # Extract payload from signal
    
    # First, remove any DC offset present in signal
    tmp = np.sum(signal)/len(signal)
    payload = [v-tmp for v in signal]
    
    # Create & apply matched filter for T-310 signal
    matched_filter = signal.firwin2(len(payload), [0, 7.5, 10, 12.5, 15, 17.5, 20], [1., 1., 0., 0., 0., 0., 0.])
    filtered_signal = np.convolve(payload, matched_filter)
    
    # Peak detection
    peaks = signal.find_peaks(filtered_signal, height = 0, distance = 8)[0] 

    # Extract bits
    decoded_bits = []
    for i in range(len(peaks)-1):
        avg = np.average(filtered_signal[peaks[i]:peaks[i+1]])
        decoded_bits.append(1 if avg > 0 else 0)
    return decoded_bits