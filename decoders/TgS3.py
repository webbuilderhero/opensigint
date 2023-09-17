# TODO: Test the program to make sure it is functioning correctly

def main():
    '''A decoding program for TgS-3'''
    
    #define the input
    tgs_signal = input("Please enter the TgS-3 signal: ")
	
	#split the signal into the components
    signal_list = tgs_signal.split('-') 
	
	#define the output variables 
    coded_message = '' 
    secret_message = ''
	
	#if the signal has 3 components, continue with the conversion
    if len(signal_list) == 3:
         # Get the coded message from the first component
        coded_message = signal_list[0]

        # Get the shift value from the third component
        shift =int(signal_list[2]) 

    	# Decode the message
        decoded_message = decode(coded_message, shift)
        secret_message = decode(decoded_message, shift)
		
		#ember the decoded message
        print('Decoded message: ', decoded_message)
        print('Secret message: ', secret_message)
    	
    else:       
        print('Invalid input.')
		
# Define the decode function 
def decode(message, shift):
    decoded_message = ''
    # Iterate over each character in the message
    for char in message:
        # ASCII character conversion
        new_char = chr(ord(char) + shift)
        decoded_message += new_char
    
    return decoded_message

# Call main function 
if __name__ == '__main__':
    main()