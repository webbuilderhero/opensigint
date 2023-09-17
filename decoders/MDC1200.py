# TCP/IP decoder for motorola MDC1200 protocol
import argparse
import socket
import struct 

def getIntFromData(data, start):
    bytes = data[start: start+2]
    result = struct.unpack('<H', bytes)[0]
    return result

def getCharFromData(data, start):
    bytes = data[start: start+1]
    result = struct.unpack('<B', bytes)[0]
    return result

def getStrFromData(data, start, length):
    bytes = data[start : (start + length)]
    result = struct.unpack('<{0}s'.format(length), bytes)[0]
    return result

def MDC1200_Decode(data):
    # Validate data length
    if len(data) < 16:
        # TODO: Maybe raise exception
        return None
    
    # Store the data into convenient variables
    MI = getIntFromData(data, 0)
    SC1 = getCharFromData(data, 2)
    SC2 = getCharFromData(data, 3)
    RA = getStrFromData(data, 4, 6)
    TA = getStrFromData(data, 10, 6)
    FN = getCharFromData(data, 16)
    AD = getCharFromData(data, 17)
    CN = getCharFromData(data, 18)
    PB = getCharFromData(data, 19)
    SD = getCharFromData(data, 20)
    DT = getCharFromData(data, 21)
    RS = getCharFromData(data, 22)
  
    # Decode data
    decoded_data = {
        'mi': MI, 
        'sc1': SC1,
        'sc2': SC2,
        'ra': RA,
        'ta': TA,
        'fn': FN,
        'ad': AD,
        'cn': CN,
        'pb': PB,
        'sd': SD,
        'dt': DT,
        'rs': RS
    } 

    return decoded_data