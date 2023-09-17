'''
#TODO: sigint framework integration

# imports needed for decoder
import numpy
import scipy
import logging

#script variables 
decoding_algorithm = 0  # 0 is for Motorola/Vertex MessageCall decoding 
start_index = 0;
stop_index = 0;

#Logging for debugging
logging.basicConfig(filename='logger.log', level=logging.INFO)

# Function for decoding the message
def decode_message(data, start_index, stop_index):
    try: 
        #decode Motorola/Vertex MessageCall messaging protocol
        decoded_msg = ""

        #iterate through the data packet
        for i in range(start_index,stop_index):
            byte_data = data[i]  #extract byte data 
            
            #convert from byte to bin 
            byte_string = bin(byte_data)[2:].zfill(8)
            #reverse the bits
            byte_string_rev = byte_string[::-1]

            #check for start signal 0xF0
            if(byte_string_rev[0:8] == "11110000"):  
                decoded_msg += "Start Signal detected \n"
            #check for stop signal 0xF1
            elif (byte_string_rev[0:8] == "11110001"):
                decoded_msg += "Stop Signal detected \n"
            else:
                # strip parity data bit
                data_bits = byte_string_rev[1:8]
                # convert from bin to ascii
                ascii_data = chr(int(data_bits,2))  
                #append decoded message
                decoded_msg += ascii_data 
    except Exception as e:
        logging.exception(e)
    return decoded_msg

# Decode data and store the result
decodedResult = decode_message(data, start_index, stop_index)
print (decodedResult) # print the decoded message