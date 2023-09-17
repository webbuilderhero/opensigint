#!/user/bin/env python3

# TODO: Determine type of GPS module (e.g. Codan S6K)

import sys

def codan_gps_decoder(signal):
    """Decode the signal from the Codan GPS"""
    
    output = '' # Output string of decoded signal
    # Variables for counting bits in a byte
    bit_count = 0 # Currently count of bits
    byte_bits = 8 # Number of bits in a byte

    # Get the raw binary string for decoding
    binary = signal_to_binary(signal)
    
    # Iterate through the binary signal
    for bit in binary:
        bit_count += 1
        
        output += bit # Append the bit to our output
        
        # If all bits have been counted for a full byte, reset and add a space
        if bit_count == byte_bits:
            output += ' '
            bit_count = 0

    return output

def signal_to_binary(signal):
    """Convert the signal into corresponding binary string"""

    binary = '' # Output binary string
    for char in signal:
        ascii_int = ord(char) # Convert char to ascii int
        binary += format(ascii_int, 'b').zfill(8) # Convert int to binary string, with leading 0s and append it

    return binary

if __name__ == '__main__':
    # Get command line argument as signal
    if len(sys.argv) > 1:
        signal = sys.argv[1]
    else:
        print('Please provide a signal!')
        sys.exit(1)

    decoded_signal = codan_gps_decoder(signal)
    
    print(decoded_signal)