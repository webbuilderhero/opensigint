# TODO: Research more into APCO-25 and its RF signaling protocols

import logging

logger = logging.getLogger('Decoder')

def decode_apco_25(signal):
    """
    Decorator for decoding APCO-25 protocol 
    
    Args:
        signal: raw signal data to decode
    Returns:
       ifications of protocol structure as dictionaries 
    """
    # Define starting variables
    frame_list = []
    bit_list = []
    byte_list = []

    # Convert signal to bits
    for d in signal:
        for bit in d:
            bit_list.append(bit)

    # Separate bits into 8 bite frames
    while len(bit_list) >= 8:
        frame_list.append(bit_list[:8])
        bit_list = bit_list[8:]

    # Convert bits to bytes
    for b in frame_list:
        byte = 0
        multiplyer = 0
        for bit in reversed(b):
            byte = byte + bit * (2 ** multiplyer)
            multiplyer = multiplyer + 1
        byte_list.append(byte)

    # Reverse byte order in the frame
    if len(byte_list) > 0:
        first = [byte_list[0]]
        if len(byte_list) == 5:
            first = first + byte_list[2:4]
        last = [byte_list[-1]]
        idx = 0 if len(byte_list) == 5 else 1
        decoded_signal = first + byte_list[idx:-1] + last

    else:
        decoded_signal = byte_list

    # Return decoded signal dictionary
    apco_dict = {
        'apco-25': decoded_signal
    }

    return apco_dict