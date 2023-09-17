# TODO: Research functions required for relevant conversion, data storage, and output formatting

# Import required libraries 
import binascii 
import struct 

# Create a decoder for IRA-ARQ ASCII-ARQ

def ira_arq_ascii_arq_decoder(input_data):

    # Initialize output
    output = []
    
    # Split input data into individual characters
    chars_list = list(input_data)
    
    # Initialize flags for IRA and ARQ bits
    ira_flag = False
    arq_flag = False
    
    # Loop through each character and turn it into 8 bits
    for char in chars_list:
        bits = '{:08b}'.format( ord(char) )
    
        # Check if IRA bit is 1
        if bits[0] == '1':
            if not ira_flag:
                ira_flag = True
                output.append((char, 'IRA'))
            else:
                output.append((char, 'N/A'))
        
        # Check if ARQ bit is 1
        if bits[1] == '1':
            if not arq_flag:
                arq_flag = True
                output.append((char, 'ARQ'))
            else:
                output.append((char, 'N/A'))
                
        # If neither IRA or ARQ bit is 1
        if bits[0] == '0' and bits[1] == '0':
            output.append((char, 'No Flag'))
    
    # Return output
    return output