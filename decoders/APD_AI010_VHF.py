# TODO: Add error handling

# This script is a decoder for the APD AI-010 VHF signal intelligence
import base64

def decodeAPDAI010VHFData(data):
    '''Function to decode APD AI-010 encoded VHF data

    Args:
        data (string): The encoded VHF data
        
    Returns:
        string: The decoded VHF data
    '''
    # transform the data from base64 into bytes
    data_bytes = base64.standard_b64decode(data)
    
    # declare a decoded_string variable
    decoded_string = ""
    
    # for each character in the data_bytes
    for ch in data_bytes: 
        # put the character in its integer form
        ch_int = int.from_bytes(ch, byteorder='big', signed=False)
        
        # shift the characters by 15 
        ch_int = ch_int - 15
        
        # transform the characters back to bytes
        ch_byte = int.to_bytes(ch_int, 1, byteorder='big')
        
        # decode the bytes to ascii format
        ch_ascii = ch_byte.decode("ascii")
        
        # add the character to the decoded string
        decoded_string+= ch_ascii
    
    return decoded_string