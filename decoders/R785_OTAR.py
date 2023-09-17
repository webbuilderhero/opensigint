# TODO: Need to figure out how to integrate this script into the framework for RF signal intelligence.

#Decoder for R-785 OTAR
#This decoder is designed to interpret the R-785 OTAR signal.

import bitstring

#Define the parameters for the R-785 OTAR
header_length = 3 #3 bytes
data_length = 8 #8 bytes

#Function to decode the signal
def r785Decoder(input_string):
    '''This decoder is designed to decode the R-785 OTAR signal'''
    #Check that the input string is the correct length
    if len(input_string) != header_length + data_length:
        return 'ERROR: Input string is not the correct length'
    
    #Parse the input string into sections
    header_byte = input_string[0:header_length]
    data_bytes = input_string[header_length:]
    
    #Decode the header
    header_data = bitstring.BitArray(header_byte).bin
   
    #Determine the type of data in the payload
    if header_data[0:2] == '00':
        data_type = 'voice'
    elif header_data[0:2] == '01':
        data_type = 'text'
    else:
        data_type = 'unknown'
        
    #Decode the payload
    payload = bitstring.BitArray(data_bytes).bin
    
    #Return the decoded signal
    return {
        'type': data_type,
        'payload': payload
    }