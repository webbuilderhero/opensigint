#!/usr/bin/env python

#TODO: Figure out how to incorporate STANAG 5066 into the Sigint framework 

import sys
import requests
import signal
import base64


def base64_to_bytes(s):
    return base64.b64decode(s)

def stanag5066_decode(s):
    decoded = bytearray()
    for i in range(0, len(s), 8):
        d = s[i:i+8]
        # Convert the bytes into bitstring
        bits = ""
        for c in d:
            bits += '{:08b}'.format(c)
        # Extract STANAG 5066 bitfields
        B1 = bits[:40]
        B2 = bits[40:64]
        B3 = bits[64:]
        # Get the 4 12 bit ints for B1/B2
        payload_ints = [int(B1[i:i+12],2) for i in range(40,59,12)] + \
                       [int(B2[i:i+12],2) for i in range(12,27,12)]
        # Convert those ints to 4 bytes
        for n in payload_ints:
            decoded.append( (n & 0xFF00) >> 8 )
            decoded.append( (n & 0x00FF) )
        # Check the validity bit
        valid = int(B3[7],2)
        decoded.append(valid)
    return decoded


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Usage: program.py <encoded message>")
    encoded = sys.argv[1]

    bytes = base64_to_bytes(encoded)
    message = stanag5066_decode(bytes)

    # Output 
    sys.stdout.buffer.write(message)