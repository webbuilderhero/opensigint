# TODO: add in error handling and ability to debug

#import the necessary libraries
import numpy as np
import pandas as pd

#Define the necessary functions
def convert_channel_bitmask_to_num(bitmask):
    '''
    This function takes a bitmask and returns an integer when converted.
    '''
    return int(bitmask,2)

def APCO25_decoder(frame):
    '''
    This function takes in a frame of data and decodes it according to APCO25 digital voice protocol.
    '''
    
    # First convert the bitmask from frame comand into an int
    channelBitmask = frame[0]
    #print(channelBitmask) #For debugging 
    channelNum = convert_channel_bitmask_to_num(channelBitmask)
    
    # Now decode the blocks accordingly
    if (channelNum % 2 == 0):
        # Even block
        linkControlWord = frame[1:-4] # Remove last 4 bytes (CRC)
    else:
        # Odd block 
        linkControlWord = frame[1:-37] # Remove last 37 bytes (CRC + FEC)
        
    decoded_link_control_word = {}
    decoded_link_control_word['channel_number'] = channelNum
    decoded_link_control_word['source_addr'] = linkControlWord[0:10]
    decoded_link_control_word['dest_addr'] = linkControlWord[10:20]
    decoded_link_control_word['LCN'] = linkControlWord[20]
    decoded_link_control_word['reserved'] = linkControlWord[21]
    decoded_link_control_word['voice_bit_rate'] = linkControlWord[22]
    decoded_link_control_word['voice_algorithm'] = linkControlWord[23]
    decoded_link_control_word['lp_data_rate'] = linkControlWord[24]
    decoded_link_control_word['lp_data_encoding'] = linkControlWord[25]
    decoded_link_control