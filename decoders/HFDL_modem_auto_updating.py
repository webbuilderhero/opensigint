"""Decoder for HFDL Modem auto updating

# TODO: Add code for capturing, decoding, and interpreting the data streams associated with the auto-updating HFDL modem.

import struct

def decode_hf_modem_update_stream(stream):
    '''Decodes the auto updating HFDL Modem data stream.
    
    Args:
        stream (int): Integer representing the data stream to be decoded.
        
    Returns:
        decoded_stream (dict): A dictionary of the decoded elements of the stream.'''
        
    # Unpack the stream and store as a list
    unpacked_stream = list(struct.unpack('!L', stream)[0])
    
    # Initialize a dictionary to store the decoded stream elements
    decoded_stream = {}
    
    # Parse the data elements from the stream
    decoded_stream['destination_id'] = unpacked_stream[0]
    decoded_stream['source_id'] = unpacked_stream[1]
    decoded_stream['update_type'] = unpacked_stream[2]
    decoded_stream['update_frequency'] = unpacked_stream[3]
    
    return decoded_stream