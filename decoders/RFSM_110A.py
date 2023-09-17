"""
Decoder for RFSM 110A

TODO:
- Research and understand ‘RFSM’
- Understand data format and decode accordingly
"""

# Import necessary libraries
import struct

# Define source parameters
DATA_BYTES = 6 # Number of bytes per data unit

def decode_rfsm_110a(data):
    """
    Decodes an RFSM 110A data signal into meaningful signal intelligence information
    
    Parameters: 
    data (bytes): Data bytes to decode
    
    Returns: 
    info (array): Decoded RF signal intelligence information
    """
    # Unpack raw bytes
    info = struct.unpack(f"={DATA_BYTES}H", data) # Unpack Hexadecimal data
    # Invert data as appropriate
    data_inverted = [~x & 0xFFFF for x in info]
    # Create output data structure
    out = []
    # Parse uniform data to output
    for i in range(len(data_inverted)):
        out.append((data_inverted[i] >> 8, data_inverted[i] & 0xFF))
    # Return output
    return out