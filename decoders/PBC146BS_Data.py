# TODO: Clarify what "plug into my framework" should look like

#Decoder for PBC-146BS Data

#import relevant packages
import base64
import struct
import numpy as np

#Define the PBC-146BS Data Decoding Function
def decode_PBC_146BS(data):
    #decode data using base64 decoding
    data_decoded = base64.b64decode(data)
    
    #convert data to a list
    data_list = [val for val in struct.unpack('<'+'f'*(len(data_decoded)//4), data_decoded)]
    
    #convert list to an array
    data_array = np.asarray(data_list)

    #return decoded data array
    return data_array