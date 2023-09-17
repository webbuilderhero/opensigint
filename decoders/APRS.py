# ApRS Decoder
# Description: This script will decode the APRS protocol, which is used in radios for real-time digital communications between moving vehicles. 

import re

# Regular expressions for decoding specific parts of the APRS protocol
AddresseeRegex = re.compile(r'[a-zA-Z]{1,6}')
PositionRegex = re.compile(r'\([0-9]{6}h[0-9]{6}P\)')
MessageRegex = re.compile(r':([\S ]+)(?=\*|$)')

def decode_aprs(packet):
    """Decodes an APRS data packet to a Python dictionary

    Arguments:
        packet: Packet string that has been received from an APRS enabled device

    Returns:
        Python dictionary containing decoded information
    """

    data = {}
    data['source'] = AddresseeRegex.findall(packet)[0]

    # TODO: 1. Decode the destination address
    data['destination'] = AddresseeRegex.findall(packet)[1]

    # TODO: 2. Decode the position information
    position = PositionRegex.findall(packet)
    data['pos_lat'] = position[0][1:7]
    data['pos_long'] = position[0][8:-2]
    
    # TODO: 3. Decode the message, if one is present
    message = MessageRegex.findall(packet)
    if message:
        data['message'] = message[0]
    
    return data