#!/usr/bin/env python
# TODO: Add additional imports if needed

import numpy as np
import matplotlib.pyplot as plt 
import math

# Reference: https://www.ritek-global.com/pdf/RM7437_08.pdf

"""
Name: Racal MEROD MA-4420/MA-4450 Decoder
Purpose: Decodes and visualizes signals using the Racal MEROD MA-4420/MA-4450 RF Signal Intelligence Device
"""


def decode_signal(data):
    """
    Decodes signal and outputs waveforms

    Args:
        data (numpy array): 1-D array representing input signal
    """

    # TODO: Check for data type
    # TODO: Convert data type to floating point if necessary

    # Normalize data 
    data_scaled = data / np.max(data)

    # Generate time-scale based on sampling rate
    fs = 44.1e3  # Sampling Frequency
    N = np.shape(data_scaled)[0]  # # of Samples
    t = np.arange(0, N/fs, 1/fs)

    # Generate Plot
    f, ax1 = plt.subplots(1, 1, figsize=(8, 4))
    ax1.plot(t, data_scaled, color='blue')
    ax1.set_title(r"Decoded Signal Waveform")
    ax1.set_xlabel("Time (second)")
    ax1.set_ylabel("Normalized Amplitude")
    ax1.set_ylim(-0.2, 1.2)
    ax1.grid(color='gray', linestyle='dashed', linewidth=0.5)

    # Generate FFT plot
    Fs = fs  # sampling rate
    T = 1.0/Fs  # sampling interval

    N = data_scaled.shape[0]  # length of the signal

    xf = np.linspace(0.0, 1.0/(2.0 * T), N // 2)
    yf = fft(