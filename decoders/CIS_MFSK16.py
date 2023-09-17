#TODO: Set up input/output ports

#!/usr/bin/env python

# Imports
import sys           # For system utilities (arg handling, comparison)
from bitstring import BitArray # For bit manipulation

# Funcitons

def CIS_MFSK16_decoder(data):
    '''
    CIS MFSK16 requires binary data for decoding, input should be in
    bitstring form. 
    '''
    # initialize output
    output = ''
    # set up all bit frequencies
    bitfreq = [1, 2, 4, 8, 16]
    # get the length of data in bytes
    length = (len(data) / 8)
    # go through each byte
    index = 0    
    while index < length:
        # convert the incoming data to bits
        bits = BitArray(data[index:index+8]) 
        # determine frequency of each bit 
        result = [bits.count(i) for i in bitfreq]
        # get the index of the highest frequency bit
        bitindex = result.index(max(result))
        # append the associated character to the output string
        output += chr(bitindex + 65)
        # increment index
        index += 1
    # return decoded output
    return output

# Main execution block
# check for proper invocation
if len(sys.argv) != 2:
    print("Incorrect usage, see documentation")
    exit(1)

# decode incoming data    
data = sys.argv[1]
decoded_data = CIS_MFSK16_decoder(data)

# output decoded data    
print(decoded_data)