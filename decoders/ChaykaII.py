# TODO : Calculate signal strength based on signal-to-noise ratio

import binascii
import math

# Decoder for the Chayka-II
def decode_Chayka_II(rfdata):
    rf_chunks = rfdata.split('0x')
    
    coded_data = []
    for chunk in rf_chunks:
        current_byte = bytearray.fromhex(chunk)
        byte_bits = '0'*(8 - len(chunk)) + bin(int(chunk, 16))[2:]
        bits = []
        for hex_char in current_byte:
            char_bits = '0'*(4 - len(hex_char)) + bin(int(hex_char, 16))[2:]
            bits.append(char_bits)
        
        bits = ''.join(bits)

        decoded_data = []
        frame = 0
        bitindex = 0
        while bitindex < len(bits)-8:
            length = int(bits[bitindex:bitindex+2],2)
            bitindex += 2
            data = bits[bitindex:bitindex+length]
            bitindex += length
            decoded_data.append(data)
        
        decoded_frame = [int(d, 2) for d in decoded_data]
        frame += 1
        coded_data.append(decoded_frame)
    
    return coded_data