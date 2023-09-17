# TODO: Determine the specific protocol and protocol version for the Spectratek Selcall

import re

# Dictionary of Spectratek Selcall tones to text
selcall_tones_dict = {
    '100': '0',
    '200': '1',
    '300': '2',
    '400': '3',
    '500': '4',
    '600': '5',
    '700': '6',
    '800': '7',
    '900': '8',
    '1000': '9',
    '1100': 'A',
    '1200': 'B',
    '1300': 'C',
    '1400': 'D',
    '1500': 'E',
    '1600': 'F',
    '1700': 'G',
    '1800': 'H',
    '1900': 'I',
    '2000': 'J',
    '2100': 'K',
    '2200': 'L',
    '2300': 'M',
    '2400': 'N',
    '2500': 'O',
    '2600': 'P',
    '2700': 'Q',
    '2800': 'R',
    '2900': 'S',
    '3000': 'T',
    '3100': 'U',
    '3200': 'V',
    '3300': 'W',
    '3400': 'X',
    '3500': 'Y',
    '3600': 'Z',
    '3700': '?',
    '3800': '!'
 }

def decode_spectratek_selcall(signal):
    """Decode Spectratek Selcall signal

    Parameters:
    signal (str): Signal input. 

    Returns:
    decoded (str): Decoded signal text.
    """

    decoded = ""
    tones = re.findall(r'[0-9]{4}', signal)

    for tone in tones:
        # Get corresponding text for the given tone
        decoded_text = selcall_tones_dict.get(tone)
        # Append decoded