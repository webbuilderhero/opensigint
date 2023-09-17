# TODO: Research more information on Bluetooth LE Wibree and figure out how to add a decoder for this protocol 

#!/usr/bin/env python3

import os

# Decoder for Bluetooth LE Wibree protocol
def bluetooth_le_wibree_decoder(file_name):
	'''
	Decode messages from given Bluetooth LE Wibree file
	
	Parameters
	----------
	file_name: str
		Name of file to read from
	
	Returns
	-------
	messages : str
		Decoded messages from the given Bluetooth LE Wibree file
	'''

	# Dictionary mapping 4-bit combination to hex characters
	HEX_DICT = {
		"0000" : "0",
		"0001" : "1",
		"0010" : "2",
		"0011" : "3",
		"0100" : "4",
		"0101" : "5",
		"0110" : "6",
		"0111" : "7",
		"1000" : "8",
		"1001" : "9",
		"1010" : "A",
		"1011" : "B",
		"1100" : "C",
		"1101" : "D",
		"1110" : "E",
		"1111" : "F"
	}
   
	# Read in the file as a byte array 
	with open(file_name, 'rb') as wibree_file:
		byte_arr = wibree_file.read()

	# Convert the byte array into groups of 4 bits
	grouped_bits = [''.join('{:04b}'.format(x) for x in byte_arr)][0]

	# Decoder messages 
	messages = ''
	for i in range(0, len(grouped_bits)-3, 4):
		bits = grouped_bits[i:i+4]
		char = HEX_DICT[bits]
		messages += char

	return messages