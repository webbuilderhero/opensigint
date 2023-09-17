# TODO: Figure out what character encoding is used for FAX Image Data

# Decoder for fax image data
# This script reads in raw RF signal in the form of amplitude data
# and decodes the information into usable data

import binascii # This will be used to convert the bytes to ascii characters

def decode_fax_image_data(data):
    """
    This function takes in signal data from a Fax image
    and decodes it into usable information

    Parameters:
        data (bytes): The raw signal data from the RF channel

    Returns:
        ascii_data (str): The decoded string data, in ascii characters
    """

    # TODO: Figure out character encoding
    byte_data = binascii.hexlify(data) # Convert the data into bytes

    # TODO: figure out what character encoding is used for image data
    ascii_data = byte_data.decode('utf-8') # Decode the bytes into ascii characters

    return ascii_data # Return the data as a string