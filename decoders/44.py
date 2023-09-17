# TODO: Change `value` key name to something else
# TODO: Add print statements to inform user of current decoding

def decode(signal):
    """
    Decoder for the 4+4 RF signal
 
    Parameters:
    signal (str): String containing the signal to be decoded
 
    Returns:
    decoded (dict): Dictionary containing the following keys
        * value (str): Decoded signal represented as a string
    """

    # Initialize decoded signal
    decoded = {
        'value': None,
    }

    # Decode signal
    binary_str = ""
    for ch in list(signal):
        # Convert character to binary, add to binary string
        bin_ch = bin(ord(ch))[2:]
        binary_str += bin_ch
 
    # Convert binary string to an integer
    decoded['value'] = int(binary_str, 2) 
 
    return decoded