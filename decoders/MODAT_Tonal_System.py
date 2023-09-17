"""
# TODO: Find appropriate library/package to use for MODAT tonal system

import #libraryNameHere

def decodeMODAT(tonalString):

	# Initializes an empty list to store the decoded signal
	decodedSignal = []

	# Iterates over each value in the tonalString
	for tone in tonalString:

		# Retrieves the signal from the MODAT library
		signal = #libraryNameHere(tone)

		# Appends the signal to the decodedSignal list
		decodedSignal.append(signal)

	# Returns the decoded signal list
	return decodedSignal