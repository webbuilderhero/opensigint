"""
Decoder for APCO P25 Encrypted Voice

@author: 
"""

import bitstring
 
def decodeAPCOP25(data):
    """
    Decodes APCO P25 encrypted voice. 
 
    Args:
        data (string): Voice data encoded in APCO P25.
 
    Returns:
        string: Decoded voice message. 
    """
    decoded_data = ""
     
    # TODO: Add logic for decoding the APCO P25 encrypted voice 
  
    # Get length of encrypted data
    len_data = bitstring.BitArray(length=data)
    data_length = len_data.len
    data_length_bits = data_length * 8
 
    # Initialize empty bitstring 
    p25b_bitstring = bitstring.BitArray(length=data_length_bits)
 
    # Loop through data and populate values
    for index in range (0, data_length_bits):
        value = data[index] * 2 - 1
        p25b_bitstring.set(value, index)
 
    # Break up encrypted data into individual blocks
    # TODO: Figure out bit size (wordSize) of data blocks
    wordsize = 23
    data_blocks = p25b_bitstring.cut(wordsize)

    # Decode extracted blocks
    for block in data_blocks:
        # TODO: Figure out how to decode data blocks
        # ...
        decoded_data += decoded_block
 
    return decoded_data