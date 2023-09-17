# TODO: add code to identify source of Sitor-B signal

import collections 
import signal
import operator

STANDARD_ALPHABET = {
    'A' : '*-', 
    'B' : '-***', 
    'C' : '-*-*',
    'D' : '-**',
    'E' : '*',
    'F' : '**-*',
    'G' : '--*',
    'H' : '****',
    'I' : '**',
    'J' : '*---',
    'K' : '-*-',
    'L' : '*-**',
    'M' : '--',
    'N' : '-*',
    'O' : '---',
    'P' : '*--*',
    'Q' : '--*-',
    'R' : '*-*',
    'S' : '***',
    'T' : '-',
    'U' : '**-',
    'V' : '***-',
    'W' : '*--',
    'X' : '-**-',
    'Y' : '-*--',
    'Z' : '--**'
        }

# Create a dictionary with reverse values for decoding Sitor-B

DECODING_TABLE = {y:x for x,y in STANDARD_ALPHABET.items()}

def decode_sitorb(signal_string):
    """ 
    Function to decode a recieved Sitor-B signal.
    Takes a signal (string) as an argument.
    Returns a decoded message (string).
    """

    output = ''

    # Split the signal_string into individual characters
    signal_chars = signal_string.split()

    # Iterate over the characters
    for char in signal_chars:
        # Look up the corresponding letter in the decoding table
        decoded_char = DECODING_TABLE[char]
        # Add the corresponding letter to the output
        output += decoded_char