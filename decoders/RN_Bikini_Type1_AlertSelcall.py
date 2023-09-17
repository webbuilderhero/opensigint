#TODO: Replace "****" with proper port information

import serial
from time import sleep

def RN_bikini_decode(ser): 
    """Function to decode RN Bikini Type-1 Alert/Selcall
    Parameters
    ----------
    ser : Serial
        Serial port object 
    Returns
    ------
    decoded_message : str
        decoded message from RN Bikini Type-1 Alert/Selcall
    """
    
    initial_byte = ser.read(1)
    if initial_byte != b'\x05': 
        return None
    
    header_byte = ( ser.read(2) )
    decoded_message = ""
    
    if header_byte[0] == b'\x18' and header_byte[1] == b'\x02': 
        header_string = "kielcall"
        
        digit_1 = ser.read(2)
        digit_2 = ser.read(2)
        digit_3 = ser.read(2)
        
        decoded_message = header_string + " " + str(int.from_bytes(digit_1, byteorder='big')) + str(int.from_bytes(digit_2, byteorder='big')) + str(int.from_bytes(digit_3, byteorder='big'))
        
    elif header_byte[0] == b'\x18' and header_byte[1] == b'\x04': 
        header_string = "alert"
        
        digit_1 = ser.read(2)
        digit_2 = ser.read(2)
        
        decoded_message = header_string + " " + str(int.from_bytes(digit_1, byteorder='big'))+ str(int.from_bytes(digit_2, byteorder='big'))
        
    # truncate message after 16-bits
    ser.read(2)
    
    return decoded_message

# main function 
if __name__ == "__main__":  
    
    ser = serial.Serial("****")