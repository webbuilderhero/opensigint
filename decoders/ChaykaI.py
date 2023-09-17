"""SIGINT: Chayka-I Decoder

This script is a decoder for the Chayka-I RF signal intelligence.

TODO:
1. Figure out the frequency of the signal
2. Determine method of modulation (e.g. BPSK)
3. Design demodulation algorithm

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sounddevice as sd

# Frequency of the signal
f =  # Fill in

# Define the sampling rate
sampling_rate = 44100
# Generate samples
samples = np.arange(sampling_rate)

# Generate the signal
signal = np.sin(2 * np.pi * f * samples / sampling_rate)

# Preview the signal
plt.plot(samples, signal)
plt.show()

# Sound out the signal
sd.play(signal, sampling_rate)

# Convert signal to baseband 
# Shift signal from RF to baseband
BB_signal = signal * np.cos(2 * np.pi * f * samples / sampling_rate)

# Demodulate
# Use a complex band-pass filter to filter out the signal's frequency.
N = 16                  # Filter order
Wn = [f, f] / (0.5 * sampling_rate)  # Normalized cutoff frequency
b, a = signal.butter(N, Wn, 'bandpass')

# Apply filter
demodulated_signal = signal.filtfilt(b, a, BB_signal)

# Plot the demodulated signal
plt.plot(samples, demodulated_signal)
plt.show()

# Sound out the demodulated signal
sd.play(demodulated_signal, sampling_rate)