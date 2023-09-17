"""DECODER FOR EEA"""

import re

def decode_eea(input):  # Function to decode an EEA string
    # Replace all instances of 'A' with '2', 'B' with '3', etc.
    # TODO: check if regex can be used for more efficient translation
    translation_table = str.maketrans('ABDCEFGHIJKLMNOPQRST', '23456789012345678901')
    decoded_string = ""
    for c in input:
        decoded_string += c.translate(translation_table)
    return decoded_string

def parse_eea(encoded_string):  # Function to extract info from decoded EEA string

    # Define regex patterns for component fields
    SOS_pattern = r'^00'
    EEA_pattern = r'^[0-9][0-9]'
    MMS_pattern = r'([0-9]{3}\-[0-9]{3})'
    UA_pattern = r'([0-9]{10})'
    PI_pattern = r'([0-9]{2}\-[0-9]{3}\-[0-9]{2})'
    MTYPE_pattern = r'([A-Z])'
    TOTAL_pattern = r'([0-9]{2})'

    # Search for patterns in the string
    result = re.search(SOS_pattern, encoded_string)
    if result:
        SOS = result.group(0)
    else:
        SOS = "Not found"
    result = re.search(EEA_pattern, encoded_string)
    if result:
        EEA = result.group(0)
    else:
        EEA = "Not found"
    result = re.search(MMS_pattern, encoded_string)
    if result:
        MMS = result.group(1)
    else:
        MMS = "Not found"
    result = re.search(UA_pattern, encoded_string)
    if result:
        UA = result.group(1)