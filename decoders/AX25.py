# TODO: Research Problem and add comment for resources consulted
# Resources:
# - https://wiki.predator.shockfish.com/index.php?title=AX.25_Discovery
# - http://www.tapr.org/pub_ax25.html

import re

'''
This script will decode AX.25 messages/packets. AX.25 is a data link 
layer protocol used in Amateur Radio (Ham Radio) that is used for 
establishing connections between two nodes over RF links.
'''

# Define the function
def ax25_decode(frame):
    '''
    This function takes in a frame (string) with AX.25-formatted information
    and returns a dictionary with the decoded values.
    '''

    # Initialize a dictionary to store decoded values
    data_fields = {}

    # Split the frame into a list
    packet_fields = re.split("( |^)", frame)
    
    # Iterate through the list and add to the dictionary
    for i in range(len(packet_fields)):
        # Check the packet for the flag characters
        # A flag character is any byte sequence beginning with the byte 0xff 
        if packet_fields[i].startswith("\xff"):
            data_fields['flag'] = packet_fields[i]
            break
        # Check the packet for the W flag
        elif packet_fields[i].startswith("\xf0"):
            data_fields['w_flag'] = packet_fields[i]
            break
        # Check the packet for source address
        elif packet_fields[i] == "":
            data_fields['source'] = packet_fields[i+1]
        # Check the packet for destination address
        elif packet_fields[i] == "":
            data_fields['destination'] = packet_fields[i+1]
        # Check the packet for the data or info field
        elif packet_fields[i].startswith(data_fields['source']) and packet_fields[i+1].startswith(data_fields['destination']):
            data_