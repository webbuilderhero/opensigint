# The Piccolo Decoder Script

# The script will decode Piccolo RF signal intelligence

# TODO: Determine the API/protocol of the Piccolo signal

# Import necessary libraries
import sys
import binascii
import struct

# Decoder function
def piccolo_decoder(sigint): 
#Input sigint bytestring into 'sigint' argument
    # Get the first four bytes in big endian 
    header_bytes = struct.unpack('> 4B', sigint[:4]) 
    # Get the length of message
    message_len = header_bytes[2] * 256 + header_bytes[3]  # Calculate length from the two 8-bit bytes 
    # Get the actual message 
    message_payload = sigint[4:(4 + message_len)]

    # TODO: Decode the message payload based on the Piccolo protocol
    out_string = "" # placeholder for decoded string

    # Return the decoded string
    return out_string