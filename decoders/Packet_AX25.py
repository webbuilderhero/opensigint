#!/usr/bin/env python
"""
A packet AX.25 decoder. 

TODO: Make sure this script can be plugged into sigint framework
"""

import numpy as np # Needed to do calculations
import bitstring # To manipulate bitstrings

def unpack_frame_data(data):
    """Unpack the frame data from the AX25 packet.
    
    Args:
        data: encoded frame data.
    
    Returns:
        decoded frame data.
    """
    # Definitions of frame types
    KISS_DATA_FRAME = 0x00
    KISS_TXDELAY = 0x01
    KISS_PERSISTENCE = 0x02
    KISS_SLOTTIME = 0x03
    KISS_TXTAIL = 0x04
    KISS_FULL = 0x05

    # Define constants 
    SOH = b'\x01' # Start Of Header
    STX = b'\x02' # Start Of Text
    ETX = b'\x03' # End Of Text
    EOT = b'\x04' # End Of Transmission

    decoded_data = b'' # To store decoded data

    # Check the frame type
    frame_type = data[0:2] # Get frame type bytes from data 
    
    # If it is a data frame
    if frame_type == KISS_DATA_FRAME:
        # Data in kiss frame starts after SOH and STX
        decoded_data = data[2:-3] # Remove SOH, STX, ETX and EOT
        decoded_data = bitstring.BitArray(decoded_data).bytes # Convert to bytes
    
    # If not data frame, discard data 
    else:
        decoded_data = None

    return decoded_data


def decode_ax25(data):
    """Decode AX.25 packet.
    
    Args:
        data: encoded AX.25 data.
    
    Returns:
        Decoded AX.25 data.
    """
    decoded_data = b'' # To store decoded