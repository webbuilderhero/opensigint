# TODO: Plug into framework - where applicable

''' 
Decoder for TEAC-KV-17 ALE + Data

Aims to decode the frequency-hopping spread-spectrum information encoded 
in the TEAC-KV-17 ALE + Data signal for the purpose of Sigint (signal intelligence).

'''

import numpy as np

# Define constants
IF_FREQUENCY_MHZ = 50000
BIT_RATE_KBPS = 800

# Variables
fft_length = 8192  # 8192 is the default FFT length for this protocol
hops_per_sec = 1000 # 1000 hops per second by default
symbols_per_hop = 3  # 3 symbols per hop

# Calculate sampling rate for FFT
sampling_rate = IF_FREQUENCY_MHZ * (2 ** (fft_length / hops_per_sec))

# Calculate time frame length for given bit rate
time_frame_length = BIT_RATE_KBPS / symbols_per_hop

# Perform FFT to transform signal from the frequency domain to the time domain
signal_fft = np.fft.fft(signal_source, fft_length)

# Using time frame length and sampling rate, determine the start and end sample index of active hop
start_sample_index = 0
end_sample_index = time_frame_length * sampling_rate

# Slice and extract active hop from signal_fft
active_hop = signal_fft[start_sample_index:end_sample_index]

# Perform inverse FFT to transform active hop from time domain to frequency domain
active_hop_ifft = np.fft.ifft(active_hop)

# Process hop for further analysis, extract information from the hop
data_bits = decode_hop(active_hop_ifft)

# TODO: Plug into framework