"""

#TODO: create a loop that allows for input of signal type(s), regardless of the size (e.g. Selex HF AIS, Wikileaks AIS, etc.) 

#import libraries
import struct
import binascii

#Selex HF AIS decoder
def selex_hf_ais_decoder(SIGINT_data):
    #calculate number of bytes
    num_bytes = len(SIGINT_data)
    #check that data is in bytes
    if isinstance(SIGINT_data, bytes):

        #check that the number of bytes is in the appropriate range (32-40 bytes)
        if num_bytes >= 32 and num_bytes <= 40:
            #convert the data into a tuples
            data_tuple = struct.unpack('<8sqbb',SIGINT_data[:18])
            # identify factors from the sigint data - start and end of header and payload
            start_of_header,frame_length,prm_indicator,len_encapsulated_data = data_tuple[3:7]
            #calculate the end of the encapsulated data
            end_of_payload = start_of_header + len_encapsulated_data
            # convert the data into bytes, using the range
            encoded_data = bytes(SIGINT_data[start_of_header+1:end_of_payload+1])
            # decode the data and store the decoded data
            decoded_data = binascii.a2b_hex(encoded_data)
            #return the decoded data
            return decoded_data
        #if the number of bytes is not in the appropriate range, return None
        else:
            return None
    #if the bits are not bytes, return None    
    else:
        return None