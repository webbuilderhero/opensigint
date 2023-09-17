#TODO: Incorporate into framework

import os
import numpy as np

def R187AB_decoder(data):
    '''
    This function decodes the R-187A/B Azart RF signals. 
    
    Input arguments: 
        data: A binary sequence from the RF signal 
        
    Output:
        decoded_data: A decoded string
    '''
    
    decoded_data = ""
    #First, we break up the data sequence into sections of 8 bits
    data_len = len(data)
    num_sections = data_len//8
    data_sections = [data[i:i+8] for i in range(0, data_len, 8)]
    
    #Next, we look at each 8-bit section to determine the meaning
    for section in data_sections:
        
        #If the first bit is 0, the next 7-bits are the character
        if section[0] == '0':
            bin_char = ''.join(section[1:])
            decoded_char = chr(int(bin_char, 2))
            decoded_data += decoded_char
            
        #If the first bit is 1, the next 7-bits and the next section are the character
        elif section[0] == '1':
            next_section = data_sections[len(data_sections)-1]
            bin_char = ''.join(section[1:] + next_section)
            decoded_char = chr(int(bin_char, 2))
            decoded_data += decoded_char
            
    return decoded_data