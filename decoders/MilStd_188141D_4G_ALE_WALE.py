#TODO: Figure out Mil-Std 188-141D 4G ALE WALE

import numpy as np 
import scipy.signal as sig

def decode(signal): 
	"""
	Decodes the Mil-Std 188-141D 4G ALE WALE signal 

	Parameters
	---------- 
	signal: np.ndarray
		Input signal to be decoded

	Returns
	------- 
	decoded_val: str 
		Decoded output from signal
	"""
	#Define signal parameters for this decoder
	fs = 16000 # sample rate
	freq_center = 537 #center frequency
	BW = 2.048 #bandwidth
	
	#Filter signal
	sos = sig.butter(4, [2*(freq_center/BW - 0.5)/fs, 2*(freq_center/BW + 0.5 )/fs], 'bandpass', output='sos')
	filtered_signal = sig.sosfilt(sos, signal)
	
	#Decode the signal
	#TODO: Figure out how Mil-Std 188-141D 4G ALE WALE signal is encoded

	decoded_val = '...' #placeholder for when completed

	return decoded_val