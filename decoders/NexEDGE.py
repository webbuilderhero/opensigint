# TODO: Research NexEdge

import numpy as np
import scipy as sp
import scipy.signal as sig
from scipy.fftpack import fft

def nexedge_decoder(signaldata):
    '''
    Decodes NexEdge signals.
    
    Parameters
    ----------
    signaldata : numpy array
        Array containing signal data

    Returns
    -------
    decoded_signal : numpy array
        Decoded signal
    '''
    # Extract parameters of the signal frame
    f_samp = signaldata[:, 0]  # Sampling rate
    f_car = signaldata[:, 1]   # Center frequency

    # Downsample signal to approximately 17 kHz sampling rate
    filter_coefs = sig.firwin(50, cutoff=17k, fs=f_samp, window='hamming')
    signal_filtered = sig.lfilter(filter_coefs, 1.0, signaldata)

    # FFT of filtered signal
    output_fft = fft(signal_filtered, n=None, axis=-1, norm=None)

    # Detect indices of the peaks in the FFT output
    peak_indices =  np.argpartition(np.abs(output_fft), -5)[-5:]

    # Compute the frequency deviation of each peak
    freq_deviations = []
    for peak_idx in peak_indices:
        peak_freq = output_fft[peak_idx]
        deviation = peak_freq - f_car
        freq_deviations.append(deviation)

    # Compute decoded bits based on the frequency deviations
    dev_threshold = 3e3  # Threshold in Hz to determine whether a deviation is positive or negative
    decoded_bits = [1 if freq_dev >= dev_threshold else 0 for freq_dev in freq_deviations]

    # Return decoded signal
    return decoded_bits