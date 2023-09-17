#TODO: Resolve any unknown values for decoding

import sys

def decoder(data):
	'''Decodes the received data stream into meaningful information'''
	
	# initializing relevant variables
	decoded_data = []

	for j in range(len(data)):
		x = data[j]
		if x == 0b0000_0010: # User frame
			first_byte = data[j+1]
			command=first_byte >> 4
			length = first_byte & 0b0000_1111
			payload = data[j+2: j+2+length]
			decoded_data.append("Autocab Ver D user frame: command#=" + str(command)+" payload=" + str(payload))
		if x == 0b0000_0011: # Feedback
			first_byte = data[j+1]
			length=first_byte & 0b0000_1111
			payload=data[j+2:j+2+length]
			decoded_data.append("Autocab Ver D feedback: payload=" + str(payload))

	return decoded_data

if __name__ == '__main__':
	decoded_data = decoder(sys.stdin.readlines())
	for d in decoded_data:
		print(d)