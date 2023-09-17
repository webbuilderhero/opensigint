# TODO: research WESNA protocol for signal intelligence

validInputDict = {}
validInputDict['T'] = 'Transmission Protocol: '
validInputDict['206'] = 'Packet Length: '
validInputDict['3'] = 'Source Node: '
validInputDict['M'] = 'IPv6 Source Field Length: '
validInputDict['1'] = 'Destination Node: '
validInputDict['WESNA'] = 'Destination Address: '

def decodeInput(input):
	# storage for decoded values
	decodedInput = {}

	# iterate over given input
	for char in input.split(' '):
		# check if char is a key in our validInputDict
		if char in validInputDict.keys():
			# add the designed key/value pairs to the dictionary
			decodedInput[validInputDict[char]] = char

	return decodedInput

# Test
inputString = 'T-206 3M1 WESNA'
print(decodeInput(inputString))