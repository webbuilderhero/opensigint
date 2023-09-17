# TODO: Still need to confirm that the script can be plugged into sigint framework

import binascii

def pactor_II_FEC_decoder(encoded_bitstring):
    """
    Decodes data encoded using Pactor-II FEC 
    Args:
        encoded_bitstring (str): The encoded bitstring
    Returns:
        decoded_bitstring (str): The decoded bitstring
    """

    data_length = len(encoded_bitstring)

    # Check the length of the bit string is divisible by 8
    # TODO: Handle an uneven number of bits
    assert (data_length % 8 == 0), "Input bitstring not divisible by 8"

    decoded_bitstring = ""

    # Iterate through each 8 bit chunk
    for i in range(0, data_length, 8):

        # Extract an 8-bit chunk
        chunk_bits = encoded_bitstring[i : i + 8]

        # Convert the binary string to an int
        num = int(chunk_bits, 2)

        # Compute the base ten value
        if num < 128:
            base_ten_value = num + 0
        elif num < 8185:
            base_ten_value = num - 127
        elif num < 8458:
            base_ten_value = num - 8526
        else:
            base_ten_value = num - 12702

        # Convert the base ten value back to ASCII
        decoded_char = chr(base_ten_value)

        # Append the decoded character to the decoded string
        decoded_bitstring += decoded_char
    
    return decoded_bitstring