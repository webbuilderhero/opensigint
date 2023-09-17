# TODO: Figure out what KFF-61 stands for

import os
import struct

# KFF-61 Decoder Script
def KFF_61_decode(file_loc):
    # open the file and read the contents
    with open(file_loc, 'rb') as f:
        KFF_bytes = f.read()
        data = struct.unpack('<H', KFF_bytes[:2])
        # iterate through the packet bytes
        for i in range (0, len(KFF_bytes), 2):
            # unpack the bytes
            data = struct.unpack('<H', KFF_bytes[i:i+2])
            # if the byte indicates the start of a packet
            if data[0] == 0xF2E1:
                response_byte1 = struct.unpack('<B', KFF_bytes[i+2:i+3])[0]
                # if the response byte indicates a data packet, extract the payload
                # TODO: Inside the payload, decode the frequency, pressure, etc information
                if response_byte1 == 0x0E:
                    payload = KFF_bytes[i+4:i+4+8]
                    return payload

# call the decoder on a given file location
print(KFF_61_decode('KFF_Packet.bin'))