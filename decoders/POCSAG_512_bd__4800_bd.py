# This is a decoder for POCSAG 512 and 4800 baud signals  
# Written by [author] 

# Import the necessary modules
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal

# TODO: Plug in necessary data from Sigint framework

# Set the baud rate
baud_rate_512 = 512
baud_rate_4800 = 4800

# Initialize the sample rate
sample_rate = 20000 #Hz

# Initialize the symbol duration
num_samples_512 = sample_rate//baud_rate_512
num_samples_4800 = sample_rate//baud_rate_4800

# Function to decode the symbols
def pocsag_decoder(signal):

	# Initialize the symbols
	symbols_512 = []
	symbols_4800 = []

	# Decoding for 512 baud
	for i in range(len(signal)//num_samples_512):

		# Get the current symbol
		symbol_512 = signal[i*num_samples_512 : (i+1)*num_samples_512]

		# Calculate the average of the symbol
		symbol_avg_512 = np.mean(symbol_512)

		# Assign the symbol based on its mean
		if symbol_avg_512 > 0:
			symbols_512.append(1)
		else:
			symbols_512.append(0)

	# Decoding for 4800 baud
	for i in range(len(signal)//num_samples_4800):

		# Get the current symbol
		symbol_4800 = signal[i*num_samples_4800 : (i+1)*num_samples_4800]

		# Calculate the average of the symbol
		symbol_avg_4800 = np.mean(symbol_4800)

		# Assign the symbol based on its mean
		if symbol_avg_4800 >