"""
Decoder for ARQ-E Signal
Author: _______________
"""
#TODO: Understand and research ARQ-E signal

import numpy as np 

def decodeArqESignal(signal):

    #Split signal into frames based on preamble delimiters
    frames = np.split(signal, np.where(signal==0)[0])
    
    #TODO: clean up rough edges due to split by filling with 0s
    
    decodedMsg = []
    
    #Parse each frame and decode
    for frame in frames:
        decodedByte = []
        bitCount = 0
        #Check for correct length of frame
        if len(frame) != 8:
            #TODO: throw exception here
            pass
        else:
            #Begin decoding each byte
            for byte in frame:
                decodedBit = int(byte >= 0)
                decodedByte.append(decodedBit)
                bitCount += 1
            #Confirm bytes were correctly decoded, then append to final msg
            if bitCount == 8:
                decodedMsg.append(decodedByte)

    return decodedMsg