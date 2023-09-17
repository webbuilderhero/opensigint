#!/usr/bin/env python

# TODO: Update decoder for specific framework 

"""
Decoder for the Serdolik Carnelian Sarah (SCS) communication system
"""

import binascii

def decodeSCS(message):
    """
    Decodes messages sent using the SCS system.
    Args:
        message (str): The encoded message to decode
    Returns:
        A decoded string from the message
    """
    # split the message into groups of 8 bits
    binary_groups = [message[i:i+8] for i in range(0, len(message), 8)]
    
    # convert the binary to characters using the SCS table
    scs_table = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 , - ! . ?".split(" ")
    decoded_message = ""
    for group in binary_groups:
        decoded_message += scs_table[int(group, 2)]
    
    return decoded_message