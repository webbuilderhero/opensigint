# To Do (Items still needing to be completed):
# 1. Research the specific signals sent in the GL-5100 FSK protocol 
# 2. Finish adjusting parameters to ensure accuracy of specific signals 

# GL-5100 FSK Decoder
import scipy.signal as signal
import numpy as np

# adjust parameters for target signal
sample_rate = 990000 # sampling rate in hertz
samples_per_symbol = 18 # Number of samples per symbol
symbols = ['0', '1'] # list of the two symbols

# define filter coefficients
alpha = 0.3
taps = np.ones(int(samples_per_symbol * 1.5))
taps *= alpha
taps[0] = 1 - alpha

# create decoder object
decoder = signal.lfilter(taps, 1.0, symbols)

# Get Binary data as bytes array
data = decoder.decode(signal.lfilter(taps,1.0,binary))

# Convert bytes array to string
decoded_signal = ''.join(chr(i) for i in data)

print(f"Decoded Signal: {decoded_signal}")