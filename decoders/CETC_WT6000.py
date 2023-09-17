# TODO: Investigate what role this specific model of CETC WT6000 plays in RF signal intelligence

import base64

def decode(input_string):
	try:
		#convert the input string to base 64 bytes 
		decoded_string = base64.b64decode(input_string)
		#convert the decoded bytes to a string
		decoded_string = decoded_string.decode('utf-8')
		return decoded_string
	except (TypeError, binascii.Error):
		# if decoding fails, return none
		return None