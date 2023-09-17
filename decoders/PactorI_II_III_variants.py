"""
This script designed to decode Pactor-I, II, and III variants.
"""

# TODO: Figure out how to interpret data interrupts

#import necessary libraries
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


def decode_Pactor(signal):
"""
This function is designed to decode a signal containing Pactor-I, II, and III variants.

Args:
    signal (numpy array): array containing the signal values


Retvals:
    decoded_data (numpy array): contains the decoded signals
"""

    # generate the FFT
    dft = np.fft.fft(signal)

    # identify frequencies associated with Pactor-I, II, and III
    # note these may vary depending on application/context
    Pactor_I_freq = 2200 # Hz
    Pactor_II_freq = 1500 # Hz
    Pactor_III_freq = 1200 # Hz

    # isolate peaks in the signal
    # note that peak filtering may need to be done, but the filtering values
    # may vary depending on signal distortion/noise
    peaks = sp.signal.find_peaks(dft)

    # search peaks array for frequencies associated with Pactor
    # remember to factor in frequency variance/bandwidth
    pactor_i_peaks = np.where(np.in1d(peaks, Pactor_I_freq, invert=True))
    pactor_ii_peaks = np.where(np.in1d(peaks, Pactor_II_freq, invert=True))
    pactor_iii_peaks = np.where(np.in1d(peaks, Pactor_III_freq, invert=True))

    # calculate amplutude of the peaks
    pactor_i_amps = dft[pactor_i_peaks[0]]
    pactor_ii_amps = dft[pactor_ii_peaks[0]]
    pactor_iii_amps = dft[pactor_iii_peaks[0]]

    # calculate phases and group into