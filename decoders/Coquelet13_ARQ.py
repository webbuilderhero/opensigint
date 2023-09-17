#TODO: Resource allocations and setup

import sys
import binascii

#Input and initializing parameters
signalCode = sys.argv[1]
bitsPerSymbol = 13 
bin_equivalent = binascii.unhexlify(signalCode)

#Decoding
decoded_message = ''
for bit in range(0, len(bin_equivalent) * 8, bitsPerSymbol):
  decoded_message += chr(int(bin_equivalent[bit: bit + bitsPerSymbol], 2))

print(decoded_message)