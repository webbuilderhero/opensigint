"""Sigint Decoder for PBO Page

TODO: Determine exact page length

This is a script for decoded a PBO page, a type of RF signal intelligence, into a readable format.

import binascii

def decode_pbo_page(data):
    """Decodes a PBO page

    Args:
        data (bytes): The raw data of the PBO page

    Returns:
        dict: A dictionary of the decoded PBO page
    """
    # Determine the size of the page
    # TODO: Make this more robust in the face of varying page sizes
    page_size = len(data)
    # Initialize empty dictionary
    decoded_data = dict()
    # Iterate over each byte of the page
    for i in range(0, page_size):
        # Read first byte
        byte = data[i]
        # Read the next byte
        byte_next = data[i+1]
        # Read the value of the byte
        value = byte & 0x0F
        # Read the type of the byte
        data_type = byte >> 4
        # Switch based on type of data
        if data_type == 0: #Counter
            decoded_data['counter'] = value
        elif data_type == 1: #Timestamp
            decoded_data['timestamp'] = (value << 8) + byte_next
        elif data_type == 2: #Data
            decoded_data[f'data_{i}'] = value
    return decoded_data