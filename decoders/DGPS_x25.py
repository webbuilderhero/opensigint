##TODO

#Research the x.25 protocol

import sys
import base64

"""
    DGPS x.25 Decoder 
    Author: YOUR NAME

    This script takes in radio frequency data from a DGPS x.25 signal
    and output its decoded form 
"""

# Define utility functions
def bit_string_to_byte_array(bit_string):
    """
    Decode a string of bits into an array of their corresponding byte representations
    Arguments:
        bit_string - bit string to decode
    Return: 
        List of byte values
    """
    # TODO: Implement bit_string_to_byte_array


    return None # Stub return, replace


def x25_unpack(data):
    """
    Unpack an x.25 signal by decoding the bit-string into an array of bytes
    Arguments:
        data - bit string of the x.25 signal to decode
    Return: 
        Unpacked data in the form of list of bytes 
    """

    # TODO: Implement x25_unpack 
    return bit_string_to_byte_array(data) # Stub return, replace


def decode_dgps_data(data):
    """
    Decodes a DGPS x.25 signal by unpacking the bit string and then decoding the base64 payload. 
    Arguments:
        data - bit string of the x.25 signal to decode
    Return: 
        Decoded DGPS data in the form of a text string
    """

    # Extract the payload as bytes from the x25 signal
    payload_bytes = x25_unpack(data)

    # TODO: Decode the base64 payload

    decoded_dgps_data = None # Stub return, replace

    return decoded_dgps_data

# Define the function that will be called when script is run
def main():
    # TODO: Handle command line arguments

    # Read input data from file
    with open('infile.txt') as f:
        data = f.read()

    # Decode the DGPS x.25 signal
    decoded_dg