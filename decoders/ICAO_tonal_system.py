"""Decoder for ICAO tonal system

#TODO:
#1) Translate ICAO tones to associated letters
#2) Implement logic to determine sequence of tones to decipher full message

#@author: _____

import collections

# ICAO tones
TONES = {
    'NIL' : 0,
    'DIT': 1,
    'DAH': 2,
    'HIDAH' :3
}

# Map the tones to morse code letters
MORSE_CODE = {
    'NIL' : '',
    'DIT': '.',
    'DAH': '-',
    'HIDAH' : ' '
}

# Function to convert ICAO tones to letters
def to_letter(index):
    '''
    Translates ICAO tones to letter
    Args:
        index - represents the index of the tone 
    Returns:
        Corresponding letter 
    '''
    # TODO: Complete logic   

    # Lookup in MORSE_CODE 
    letter = MORSE_CODE[list(TONES)[index]]

    return letter

# Function to decode tones
def decode(tones):
    '''
    Decodes ICAO tones 
    Args:
        tones - sequence of tones
    Returns:
        Decoded message 
    '''
    # Convert tone indexes to letters 
    letters = [to_letter(tone) for tone in tones]

    # Convert letter to message
    # TODO: Implement logic 
    # Create a deque to store letters
    queue = collections.deque(letters)
    # Create a temporary string
    string = ''
    while queue:
        # Get the next letter
        letter = queue.popleft() 
        if letter == ' ':
            # If letter is space, add current string to message
            message.append(string)
            # Reset string
            string = ''
        else:
            # Add letter to string
            string += letter
    # Add any remaining string to message
    message.append(string)
    
    # Return message