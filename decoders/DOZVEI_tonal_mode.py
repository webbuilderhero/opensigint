#!/usr/bin/env python
# TODO: Modify to apply for DOZVEI tonal mode

# Import modules
import numpy as np
import scipy as sc
import scipy.signal

# Defining functions

def DOZVEI_tonal_decoder(x):
	"""
	This function decodes an incoming DOZVEI tonal signal
	Parameters
	----------
	x : array
		Input array of complex frequency samples

	Returns
	-------
	message : string
		Decoded message
	"""
	# Step 1: Estimate signal frequencies
	freqs = sc.fftpack.fftfreq(x.shape[0], d=1.0/x.shape[0])

	# Step 2: Detect the tonal DOZVEI signal frequencies
	primary_freqs = np.array([f for f in freqs if np.isclose(f, f//800*800)])

	# Step 3: Estimate the amplitudes of each tonal signal
	amps = np.abs(np.fft.fft(x))
	primary_amps = np.array([amps[i] for i, f in enumerate(freqs) if f in primary_freqs])

	# Step 4: Compute the phase angle at each signal frequency
	phases = scipy.signal.hilbert(x)
	primary_phases = np.array([phases[i] for i, f in enumerate(freqs) if f in primary_freqs])

	# Step 5: Convert the amplitudes, frequencies, and phases into symbols
	symbols = np.array([primary_amps[i]*np.exp(1j*primary_phases[i]) for i in range(len(primary_freqs))])

	# Step 6: Construct the decoded message
	message = ''
	for symbol in symbols:
		message += chr(int(np.angle(symbol)/np.pi*128+128))
	return message