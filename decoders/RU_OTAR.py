# TODO: Modify code to plug into existing framework for sigint

def sig_decode(encoded_str):
	"""Decode a string encoded with the RU OTAR encoding scheme
	
	Args:
		encoded_str (str): The encoded string

	Returns:
		str: The decoded string
	"""

	decoded_str = ""
	for ch in encoded_str:
		if ch.isalpha():
			decoded_str += ch
		elif ch.isdigit():
			decoded_ch = chr(ord('A') + int(ch))
			decoded_str += decoded_ch

	return decoded_str