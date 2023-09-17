# NOTE: This script won’t run unless it’s plugged into a framework-based sigint system

import numpy as np

# Todo: Fill in necessary imports for the script to work

# Decoder for EURO Tonal System
def euro_decoder(signal):
    sample_rate = signal.sample_rate
    results = []

    # Todo: Clean the signal and prepare so it'll work with numpy functions
    sampled_signal = signal.samples

    # Todo: Determine the frequency range of the EURO tonal system
    #       and assign to these variables
	min_frequency = 0
    max_frequency = 0

    # Use numpy to create an array of frequencies
    frequencies = np.arange(min_frequency, max_frequency, 1)

    # Use Fast Fourier Transform to find amplitudes of signal
    # across different frequencies
    fourier = np.fft.rfft(sampled_signal)
    frequencies = np.fft.rfftfreq(len(sampled_signal), 1/sample_rate)
    amplitudes = np.abs(fourier)

    # Loop through the frequencies and determine the presence of certain tones
    for i, freq in enumerate(frequencies):
        if freq >= min_frequency and freq <= max_frequency:
            # Store results in results array
            results.append((freq, amplitudes[i]))

    return results