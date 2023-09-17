# TODO: Look up documentation on the XClover2000 RF signal format

import binascii
from bitstring import BitArray

def xclover2000_decode(data):
    decoded_data = BitArray(bin=data).bytes
    output_data = binascii.unhexlify(decoded_data.hex())

    return output_data

# Test out the decoder
data = '101101001101010010010111010100010'
print(xclover2000_decode(data)) # This should output some ascii-encoded chars