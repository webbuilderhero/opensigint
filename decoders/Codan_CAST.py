import sys

# TODO: include a module that can detect the frequency of the radio signal

from scipy.fftpack import fft2

def codan_cast(signal):
	# Convert signal into frequency-domain
	fftdata = fft2(signal)
	# Get the power spectral density
	powerspectrum = fftdata**2
	# look for dominant frequencies from the power spectrum
	codan_freq = get_dominant_freq(powerspectrum)
	# look for the particular CODAN cast frequency
	if codan_freq == CODAN_CAST_FREQ:
		# Output "codan_cast" is present in signal
		print("codan_cast present in signal")
	# Output "codan_cast" is not present in signal
	print("codan_cast not present in signal")

# Find the most dominant frequencies in the power spectral density
def get_dominant_freq(powerspectrum):
	# TODO: fill code for finding the most dominant frequencies
	pass