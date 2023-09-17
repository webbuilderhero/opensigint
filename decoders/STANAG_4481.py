#TODO: Research the STANAG 4481 protocol and its associated decoding rules

#!/usr/bin/python

import string

#This script implements a decoder for the STANAG 4481 protocol 

def decode_stana441(data):
    decoded_data = ''

    # Iterate through each character in the data stream
    for d in data:
        #Check for valid character
        if d in (string.ascii_letters + string.digits):
            decoded_data+=d
        #Check for special characters
        if d in ('*','#','!','.',' ','-'):
            # switching based on the decoded character
            if d == '*':
                decoded_data+="a"
            elif d == '#':
                decoded_data+="b"
            elif d == '!':
                decoded_data+="c"
            elif d == '.':
                decoded_data+="d"
            elif d == ' ':
                decoded_data+="e"
            elif d == '-':
                decoded_data+="f"
    return decoded_data