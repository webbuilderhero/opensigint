# TODO: method to recognize and decode the DNP3 signaling protocol

import bitstring
import time


def dnp3_decoder(data):
	'''
	This function will decode string bits that represent 
	the DNP3 (Distributed Network Protocol 3) SCADA protocol. 
	Takes bitstring data as an argument, returns a decoded string with data.
	'''
	# Initialize output variables
	start_bits = ''
	control_octet1 = ''
	control_octet2 = ''
	segment_length = ''
	apdu = ''

	# Process argument to extract necessary bits
	data_bin = data.bin
	start_bits = data_bin[0:2]

	if start_bits != '01':
		# Detected error in bitstream
		return 'Error: Invalid bitstream data'

	# Extract control octets
	control_octet1 = data_bin[2:10]
	control_octet2 = data_bin[10:18]
	
	# Extract segment length
	segment_length_bits = [data_bin[18], data_bin[19], data_bin[20]]
	segment_length = ''
	for i in segment_length_bits:
		segment_length += str(int(i, 2))

	# Extract APDU
	apdu_start_index = 21
	apdu_end_index = 21 + (int(segment_length) * 8)
	apdu = data_bin[apdu_start_index:apdu_end_index]

	# Construct Dictionary with decoded data
	dnp3_data = {
		'start_bits': start_bits,
		'control_octet1': control_octet1,
		'control_octet2': control_octet2,
		'segment_length': segment_length,
		'apdu': apdu
	}
	
	return dnp3_data