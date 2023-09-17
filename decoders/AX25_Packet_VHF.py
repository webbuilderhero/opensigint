# TODO: Add a list of commonly used AX.25 packet protocols.

import binascii

# Decoder for for AX.25 Packet VHF signals. 

def decoder(frame):
    """
    A function to decode AX.25 packet VHF signals.
    
    Parameters:
    frame (Byte): The frame of the AX.25 packet VHF signal.
    
    Returns:
    frame (String): A decoded value of the frame.
    """
    
    # Check if frame is in bytes
    if not type(frame) == bytes:
        raise TypeError('Frame must be in bytes')
    
    # Dictionary of AX.25 packet protocols
    ax25_protocols = {'3C': 'LOGIN', '6F': 'DATA', '23': 'CLIENT_REQ', 
                      '43': 'SERVER_RES'}
    
    # Convert frame to hexadecimal
    hex_frame = binascii.hexlify(frame)
    
    # Determine the protocol
    ax25_protocol = ax25_protocols.get(hex_frame[0:2])
    
    # Initialize identifiers for each protocol
    login_id = ''
    data_id = ''
    client_req_id = ''
    server_res_id = ''
    
    # Set the corresponding identifier for each protocl
    if ax25_protocol == 'LOGIN':
        login_id = hex_frame[2:4]
    elif ax25_protocol == 'DATA':
        data_id = hex_frame[2:4]
    elif ax25_protocol == 'CLIENT_REQ':
        client_req_id = hex_frame[2:4]
    elif ax25_protocol == 'SERVER_RES':
        server_res_id = hex_frame[2:4]
    
    decoded_frame = {'protocol': ax25_protocol, 'login_id': login_id, 
                     'data_id': data_id, 'client_req_id': client_req_id,