# TODO: Research/Source more of the Tadiran FLASH specific parameters to decode

# Script to decode Tadiran FLASH signals

# Imports
import numpy as np
import scipy
import scipy.signal

# Initializations
sampling_freq = 12e6 # Sampling frequency
flip_freq = 2.2e6 # Flip Frequency
sig_length = 200*10^(-6) # Signal Length

# Generate Samples of Tadiran FLASH Data
data_in = np.array([])
for i in range(int(sig_length*sampling_freq)):
    data_in = np.append(data_in, np.sin(i/flip_freq))

# Perform FFT to detect signal energy
fft = np.fft.fft(data_in)

# Calculate power spectrum
def power_spec(sw, std):
    return (sw/std) + 1

spec_res = power_spec(fft, np.std(fft))

# Process and Execute Power Spectrum
processed_spec = [x for x in spec_res if x > 0.5]

# Calculate Baud rate
baud_rate = np.mean(processed_spec) / sampling_freq

# Calculate the center frequency
center_freq = np.mean(processed_spec) * sampling_freq

# Calculate the bit length
bit_length = 1.0 / baud_rate

# Create Bandpass Filter
b, a = scipy.signal.butter(5, [1/bit_length, 1/(bit_length/2)], "bandpass")

# Filtering the signal
filtered_sig = scipy.signal.lfilter(b, a, data_in)

# Apply sample & hold
sampled_sig = scipy.signal.resample(filtered_sig, int(bit_length * sampling_freq))

# Extract bits
bits = np.array([x[0] for x in sampled_sig])