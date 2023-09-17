"""
Decoder for DMR ARC4 EP

TODO: 
1. Document function
2. Add logging

"""

import struct

def decodeDMR_ARC4EP(data):
    """
    Function for decoding an DMR/ARC4 EP SINGINT signal

    Parameters
    ----------
    data : bytes
        Bytes of data containing the SIGINT signal.
    
    Return
    -------
    result : dict
        Dictionary containing the decoded SIGINT signal.

    """
	
    # Define the length of the payload 
    payload_len = len(data) 
 
    # Check for the minimum length of the signal
    if payload_len < 8:
        return {}
    
    # Unpack the signal data
    _, config, key_id, _, rest_len, frame_type = struct.unpack("<BBBBLB", data[:8])

    # Check for the minimum length of the signal
    if payload_len < rest_len + 8:
        return {}
    
    # Create a dictionary for the result
    result = {'config':config, 'key_id':key_id, 'frame_type':frame_type}
    
    # Get the rest of the signal
    rest_data = data[8:rest_len + 8]
    
    # Unpack the rest data if it is set
    if rest_len > 0:
        result = {**result, **unpack_rest_data(frame_type, rest_data)}
    
    return result


def unpack_rest_data(frame_type, data):
    """
    Function for unpacking rest of the data in the SIGINT packet.
    
    Parameters
    ----------
    frame_type : int
        Integer containing the frame type of the packet.
    data : bytes
        Bytes containing the rest of the data in the packet. 
    
    Return
    -------
    result : dict
        Dictionary containing the rest of the data in the packet.

    """

    result = {}
    
    # Check for the type of the packet
    if frame_type == 0x10