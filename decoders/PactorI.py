# TODO: Insert into Framework

#----------------------------------

# Decoder for Pactor-I 
# (c) 2020 Extremely Professional Decoder Makers

# Imports
import numpy as np 
import scipy.signal as sig 
import matplotlib.pyplot as plt 

# Parameters 
sample_rate = 44.1e3 # Samples per second
fsk_dev = 1800 # Frequency deviation
fsk_freq = 2125 # Center frequency

# Opening input file and importing data
input_array = np.fromfile("input.dat", dtype="uint8")

# Calculating Amplitude 
amp = np.mean(input_array**2)

# Normalizing input array 
input_array = input_array  / amp 

# Generating FSK Modulation signals
fsk_freq0 = fsk_freq - fsk_dev/2
fsk_freq1 = fsk_freq + fsk_dev/2

sig_t0 = np.cos(2 * np.pi * fsk_freq0 * np.arange(input_array.shape[0]) / sample_rate)
sig_t1 = np.cos(2 * np.pi * fsk_freq1 * np.arange(input_array.shape[0]) / sample_rate)

# Filtering input signal 
filtered_sig = sig.lfilter(input_array, [1], sig_t1 - sig_t0)

# Decoding Pactor-I
output_array = np.zeros(input_array.shape[0], dtype='uint8')

nsamples = int(sample_rate / fsk_dev)

# Parsing Pactor-I bit string
for i in range(0, input_array.shape[0], nsamples):
    bit = np.sum(filtered_sig[i:i+nsamples] > 0)
    output_array[i] = int(bit > nsamples/2)

# Output to file
output_array.tofile("pactor_output.dat")