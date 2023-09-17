#TODO: Figure out the message type associated with MAFF v1. 

# Decoder script for MAFF v1

import sys

# Define constants
message_type = '' # TODO: Fill in message type associated w/ MAFF v1

# Define RF signals
RF_signal1 = '' # TODO: Define first RF signal value
RF_signal2 = '' # TODO: Define second RF signal value

# Initialize variables
decoded_message = ''

# Main loop:
def main(argv):
	
	raw_message = sys.argv[1]
	
	# if the message matches our message type:
	if message_type == 'MAFF v1':
		# decode based on MAFF v1 encoding rules
		
		# Check for RF signal 1
		if raw_message.find(RF_signal1) != -1:
			# Add corresponding letter to decoded message
			
			decoded_message += '' # TODO: Define letter associated with RF_signal1
		
		# Check for RF signal 2
		if raw_message.find(RF_signal2) != -1:
			# Add corresponding letter to decoded message
			decoded_message += '' # TODO: Add letter associated with RF_signal2
	
	# print decoded message
	print(decoded_message)

if __name__ == '__main__':
	main(sys.argv)