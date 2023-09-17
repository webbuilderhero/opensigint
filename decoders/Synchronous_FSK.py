"""
Decoder for Synchronous FSK signals

# TODO: 
import numpy as np

def synchronous_FSK_decoder(input_signal):
	"""
	Decodes a Synchronous FSK signal

	Args:
		input_signal: The signal to decode

	Returns:
		A decoded signal
	"""
	# # Determine the bitrate of the signal
	# TODO: Determine the bitrate

	# Frequency size (delta_fx)
	delta_fx = # TODO:

	# Frequency modulation index (beta)
	beta =  # TODO: 

	# Get the minimum frequency
	f_min = # TODO:

	# Get the frequencies of the two levels
	f_h = ((2*beta +1)*f_min) 
	f_l = f_min - beta*f_min

	# Get the start and end points of the signal
	s_start = np.where(input_signal==0)[0][0]
	s_end = np.where(input_signal==0)[0][-1]

	# Initialize the output signal
	output_signal = np.zeros(len(input_signal))

	# Iterate through the signal
	for index in range(s_start, s_end, delta_fx):
		if input_signal[index:index+delta_fx].mean() >= f_h: 
			output_signal[index:index+delta_fx] = 1

		elif input_signal[index:index+delta_fx].mean() <= f_l:
			output_signal[index:index+delta_fx] = 0

	return output_signal