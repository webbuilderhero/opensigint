#TODO
#Make sure the decoder account for encoding/decoding of all known versions of Yaesu/Vertex Standard C4FM Smart Fusion YSF

import bitarray 

# Algorithm for encoding/decoding Yaesu/Vertex Standard C4FM Smart Fusion YSF

def decode(encoded_bitstream):

	# Initialize decoder variables
	decoded_bitstream = bitarray.bitarray() 

	# Decode the bitstream
	for bit in encoded_bitstream:
		decoded_bitstream.append(bit ^ xor_with)
	return decoded_bitstream

def encode(decoded_bitstream):

	# Initialize encoder variables
	encoded_bitstream = bitarray.bitarray() 

	# Encode the bitstream
	for bit in decoded_bitstream:
		encoded_bitstream.append(bit ^ xor_with)
	return encoded_bitstream

# The "xor_with" variable is a globally set variable used to encode/decode XOR
xor_with = 0x82