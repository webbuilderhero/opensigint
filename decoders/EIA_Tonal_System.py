#!/usr/bin/env python

"""
# TODO: Research EIA Tonal System - determine what type of signals should be expected and what format the output should be in 
"""

import re
from collections import Counter

def eia_tonal_decode(signal):
    """
    Decode a signal using the EIA Tonal System.
    
    :param signal: The signal, with tones separated by spaces
    :type signal: str
    :return: The decoded text
    :rtype: str
    """
    output = ''
    tone_map = {
        'A': '1',
        'B': '23',
        'C': '2',
        'D': '34',
        'E': '12',
        'F': '45',
        'G': '3',
        'H': '56',
        'I': '4',
        'J': '67',
        'K': '5',
        'L': '78',
        'M': '6',
        'N': '89',
        'O': '7',
        'P': '90',
        'Q': '8',
        'R': 'AB',
        'S': '9',
        'T': 'CD',
        'U': 'AB',
        'V': 'EF',
        'W': 'CD',
        'X': 'GH',
        'Y': 'EF',
        'Z': 'GH'
    }

    # Split the signal into tones
    tones = signal.split(' ')
    if len(tones) % 2 != 0:
        return None
    
    # Group the tones in pairs
    pairs = zip(tones[::2], tones[1::2])
    for first, second in pairs:
        # Count how many of each tone there is in each pair
        counts = Counter([first, second])
        char = None
        if 'A' <= first <= 'Z':
            # If one of the tones is a single letter, that's the character
            char = first
        else:
            # If one of the tones is a double letter