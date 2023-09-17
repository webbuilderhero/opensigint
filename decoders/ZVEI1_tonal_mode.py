import numpy as np 
import matplotlib.pyplot as plt

# TODO: Adjust for differing sample rates.

# Variables for adjusting the ZVEI-1 parameters
bitlength = 8
bitspace = 8
zvei_dbit_len = 16  # Length of double bits

# Signal Processing Parameters
fs = 44100  # Sample Rate 
buffer_size = 44100  # Buffer size

# Initializing the signal buffer
buffer = np.zeros(buffer_size)

# Main Loop 
for sample_idx in range(buffer_size):
    # Grab the sample from the buffer 
    sample = buffer[sample_idx]
    
    # ZVEI-1 processing
    zvei_index = sample_idx % (bitlength + bitspace)
    if zvei_index == 0 or (zvei_index % (bitlength + bitspace)) < bitlength:
        buffer[sample_idx] = 1    # High bit
    else:
        buffer[sample_idx] = 0    # Low bit

    # Making groups of zvei_dbit_len length bits
    zvei_dbits = buffer[sample_idx - (zvei_dbit_len - 1): sample_idx]
    
    # Check for ZVEI-1 message
    if np.array_equal(zvei_dbits, [1, 0] * int(zvei_dbit_len / 2)):
        #TODO: Add in message decoding
        
        # Reset the buffer to 0s
        buffer = np.zeros(buffer_size)
        
# Plotting the buffer
plt.plot(buffer[:200])
plt.show()