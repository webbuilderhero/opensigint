# TODO: Work out definitions of variables used

import re
from array import array

# These are the symbols used to encode and decode data
symbols = {'Z0':'0000', 'Z1':'0001', 'Z2':'0010', 'Z3':'0011', 'Z4':'0100', 'Z5':'0101', 'Z6':'0110', 'Z7':'0111', 'Z8':'1000', 'Z9':'1001', 'Z+':'1010', 'Z-':'1011', 'ZH':'1100', 'ZL':'1101', 'ZS':'1110', 'ZT':'1111'}

# A function to decode a piece of TEAC-KV11V2 data
def teackv11v2_decode(data):
    decoding_pattern = re.compile('Z[0-9+-HLST]')  # This pattern will identify which symbols in the data need to be decoded
    decoded_data = array('B')   # Create an array to store the decoded 8-bit values in

    # Loop through the individual pieces of data and decode any necessary symbols into 8-bit values
    for item in data.split():
        if decoding_pattern.match(item):
            decoded_data.append(int(symbols[item], 2))
        else:
            decoded_data.append(int(item, 16))

    return decoded_data    # Return the entire decoded data array