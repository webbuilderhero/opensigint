#TODO: Further research on Selex CM117E

import numpy as np
import scipy
from scipy import signal

# Get the input signal from file
input_signal_array = np.load('input_signal.npy')

# Filter the signal
f_cut = 1500 # Cut-off value of the low pass filter
order = 5 # The order of the filter
b, a = signal.butter(order, f_cut)
filtered_signal_array = scipy.signal.filtfilt(b, a, input_signal_array)

# Decode the signal
# Break up filtered signal into chunks that match Selex CM117E's data rate 
rate_chunk_size = 15 # Size of data rate chunks
rate_chunks = np.reshape(input_signal_array, (-1, rate_chunk_size)) #

# Find data chunks
data_chunk_size = 5 # Size of data chunks
start_indices = np.array([]) # Array of found start packet indices
for i in range(rate_chunks.shape[0]): # Iterate over rate_chunks
  # Check if data packet start is found
  if (rate_chunks[i, -1] == 1): # If last bit in rate_chunk is 1
    start_indices = np.append(start_indices, i) # Mark rate_chunk as possible start packet
    
# Create decoded_signal array from data_chunks
decoded_signal = np.array([]) # Decoded signal array
for i in start_indices:
  # Check each data_chunks shape size
  data_chunk = rate_chunks[i:i+data_chunk_size] 
  if (data_chunk.shape == (data_chunk_size, rate_chunk_size)): # If data_chunk is correct size
    decoded_signal = np.append(decoded_signal, data_chunk) # Add data_chunk to decoded_signal

# Save the decoded signal
np.