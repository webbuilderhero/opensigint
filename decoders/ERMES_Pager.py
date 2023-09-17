import sys
import signal
import base64

# TODO: Get the library of protocols to decode ERMES pager

# Preamble to the default ERMES pager transmission
DEFAULT_PREAMBLE = 0xb8

def decode_ERMES(sig_string):
    """ Decode the ERMES pager signal.
    """
    # Break down the signal into components
    preamble, data_length, data = \
        sig_string[:1], sig_string[1:2], sig_string[2:]
    
    # Check if the signal matches the standard ERMES pager preamble
    if preamble != DEFAULT_PREAMBLE:
        raise ValueError("Signal doesn't match the default ERMES preamble.")
    
    # Decode data according to length
    data_length = data_length & 0x07
    if data_length == 6:
        data_bytes = int(data[:2], 16)
        data = data[2:]
        decoded_data = base64.b64decode(data)[:data_bytes]
    else:
        decoded_data = base64.b64decode(data)[:data_length]
     
    return decoded_data

# Main function of the script 
def main():
    # Get the sigint from stdin
    sigint = sys.stdin.read()

    # Decode the sigint
    decoded_sigint = decode_ERMES(sigint)
    print(decoded_sigint)

# Run the main function on SIGINT
signal.signal(signal.SIGINT, main)