# TODO: Decide which algorithm should be used for decryption. 

import signal

def ccir1_Tonal_Decode(signal):
	"""
	This function will decode an incoming signal using the CCIR-1 
	Tonal System. The CCIR-1 Tonal System is a type of encryption 
	used in Radio Frequency Signal Intelligence (RF SIGINT).
	
	Args:
		signal (Signal): The signal to be decoded. 
	
	Returns:
		decoded_ signal (Signal): The decoded signal.
	"""
	# Initialize Variables
	frequency_list = []
	decoded_signal = ""
	
	# Iterate through signal frequencies
	for frequency in signal: 
		# Convert frequencies to tones
		tones = convert_frequencies_to_tones(frequency)

		# Append tones to list
		frequency_list.append(tones)
	
	# Convert tones list to string
	frequency_string = "".join(frequency_list)
	
	# Decode string using CCIR-1 Tonal System algorithm
	decoded_signal = ccir1_tonal_system_algorithm(frequency_string)
	
	# Return decoded signal
	return decoded_signal
 
def convert_frequencies_to_tones(frequency):
	"""
	This function will convert an incoming signal frequency 
	to CCIR-1 tones.
	
	Args:
		frequency (float): The signal frequency.
	
	Returns:
		tones (str): The tone representation of the initial frequency.
	"""
	# Initialize Variables
	tones = ''	
	# Convert frequency to tones
	
	# TODO: Implement conversion algorithm
 
	# Return tones
	return tones

def ccir1_tonal_system_algorithm(frequency_string):
	"""
	This function will use the CCIR-1 Tonal System algorithm 
	to decrypt a string containing tones.
	
	Args:
		frequency_string (str): The string of tones to be decrypted.