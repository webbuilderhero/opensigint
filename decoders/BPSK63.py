"""
Decoder for BPSK63
Author: _________________
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt

#TODO: Break in to separate steps - Timing recovery, AGC


def BPSK63_decode(input_signal):
	"""
	This function decodes a BPSK63 signal given a complex input signal.
	
	Parameters
	----------
	input_signal : numpy array
		A complex array of the input signal

	Returns
	-------
	message : numpy array
		A numpy array of the symbols of the decoded message
	
	"""
	
	# Initialize decoder
	samp_freq = 125_000
	sample_length = len(input_signal)
	data_points = sample_length//63

	# Estimate clock frequency
	est_clk = scipy.signal.correlate(input_signal, np.ones(63)).max()/63 # Estimate clock frequency
	clk_freq_error = ((est_clk/samp_freq) - 1) * 100 # Percentage error in estimated clock frequency
	print("Clock Frequency Error = {}%".format(clk_freq_error))

	# Apply automatic gain control to equalize signal power
	agc_gain = (np.sum(abs(input_signal))/sample_length)**(-1)
	agc_signal = agc_gain*input_signal
	
	# Retrieve the data points
	data_points_re = np.array(agc_signal[0::63], dtype='float32')
	data_points_im = np.array(agc_signal[1::63], dtype='float32')
	
	# Perform timing recovery and bit decoding
	message = []
	for i in range(data_points):
		data_point = data_points_re[i] + 1j*data_points_im[i]
		symbol = data_point.real > 0
		message.append(