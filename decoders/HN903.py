"""
Decoder for HN-903

TODO: Add error handling
      Add support for optional settings/parameters that can be passed in
"""

import re

def hn903_decoder(encoded_message):
    """Decodes an encoded HN-903 message

    Parameters:
        encoded_message - the encoded message to be decoded

    Returns:
        The decoded message
    """
    # Separate out the encoded message into individual characters
    encoded_chars = list(encoded_message)

    decoded_message = ''

    # Encode each character
    for c in encoded_chars:
        # Check for valid encodings - it must be in the form A-Z or 0-9
        is_valid_encoding = re.search('^[A-Z0-9]$', c)
        if not is_valid_encoding:
            continue

        # Decode the character
        if c.isalpha():
            decoded_message += chr(ord(c) - 4)
        else:
            decoded_message += chr(ord(c) + 2)

    return decoded_message