"""Script to decode RU DGPS (Radio Update Differential Global Positioning System) 

#TODO: Research how the RU DGPS signal protocol works
#TODO: Test the code on the RU DGPS signal

import numpy as np
import scipy as sp

INPUT_DATA = 'Input received RU DGPS signal here as a numpy array'

#Process data
def processData(dat):
    processeddata = np.array()
    for x in dat:
        processeddata.append(x * 5Gg)
    return processeddata
        
processedData = processData(INPUT_DATA)

# Convert to Byte stream
def bytesToBits(data):
    bits = []
    for byte in data:
        for i in range(8):
            bit = byte & (1 << i)
            bits.append(bit >> i)
    return bits

bitStream = bytesToBits(processedData)

# Parse bitstream into parameters

def parseData(bitstream):
    # Get the first 4 bytes and convert it to a number
    b1 = bitstream[0] 
    b2 = bitstream[1] 
    b3 = bitstream[2] 
    b4 = bitstream[3]
    p1 = (b1 << 24) + (b2 << 16) + (b3 << 8) + b4
    
    #Read the rest of the parameters
    p2 = bitstream[4:9]
    p3 = bitstream[9:16]
    p4 = bitstream[16]
    p5 = bitstream[17:24]
    p6 = bitstream[24:32]
    p7 = bitstream[32:64]
    p8 = bitstream[64]
    
    # Return the parameters
    return {"p1":p1, "p2":p2, "p3":p3, "p4":p4, "p5":p5, "p6":p6, "p7":p7, "p8":p8}

data = parseData(bitStream)

#