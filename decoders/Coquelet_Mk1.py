# TODO: Figure out what Coquelet Mk1 actually is - written on comments on top of the code 

import signal 

# Decoding Coquelet Mk1 signals 

def decodeCoqueletMK1(sig):
	# Coquelet Mk1 uses frequency shift keying to encode data 
	# Reduce data to carrier frequency 
	carrier_freq = sig.frequency
	
	# Get the bit rate 
	bit_rate = sig.bitRate
	
	# Get the data pulse width
	data_pulse_width = sig.dataPulseWidth 
	
	# Get the start pulse width
	start_pulse_width = sig.startPulseWidth 
	
	# Get the data buffer
	data_buffer = sig.dataBuffer
	
	# Get the start buffer
	start_buffer = sig.startBuffer

	# Variable to store decoded data
	decoded_data = ""

	# Loop through data_buffer
	for data in data_buffer: 
		# If pulse width greater than data_pulse_width, convert to 0
		if data > data_pulse_with:
			decoded_data += "0"
		
		# If pulse width less than data_pulse_width, convert to 1
		elif data < data_pulse_width:
			decoded_data += "1"
			
	return decoded_data