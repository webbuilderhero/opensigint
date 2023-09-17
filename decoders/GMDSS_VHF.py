# TODO: fill in remaining logic

import re

# define some helpful constants
VHF_LOWER_FREQ = 156.0
VHF_UPPER_FREQ = 174.0

# define some helpful functions
def validate_freq(freq):
    """Validates a given frequency is within VHF range
    Args:
        freq(float): frequency to validate
    Returns:
        True if frequency is within range, False otherwise
    """
    if VHF_LOWER_FREQ <= freq <= VHF_UPPER_FREQ:
        return True
    return False

def decode_call_sign(sign):
    """Decodes a given call sign.
    Args:
        sign(str): two or three part string representing decoded call sign
    Returns:
        decoded call sign as a string (e.g. 'AA12345A')
    """
    # try to match three part call sign string
    regex = re.compile(r'^[A-Z]{2}[0-9]{4}[A-Z]$')
    m1 = regex.search(sign)
    if m1:
        return sign

    # try to match two part call sign string
    regex2 = re.compile(r'^[A-Z]{2}[0-9]{3}[A-Z]$')
    m2 = regex2.search(sign)
    if m2:
        return '{0}{1}A'.format(sign[0:2], sign[2:5])

    return None

def decode_message(message):
    """Decodes a GMDSS VHF message.
    Args:
        message(str): string representing encrypted message
    Returns:
        decoded GMDSS VHF message as a dictionary
    """

    # extract message info from string
    regex = re.compile(r'^([A-Z]+)\s+([0-9]+)\s([A-F0-9]{8})$')
    m = regex.search(message)
    if not m:
        return