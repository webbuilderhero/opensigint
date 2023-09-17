#TODO: Investigate exact protocol name and parameters

import sys

#The number of bytes that will be received in total
BYTES_RECEIVED = 12

#Values to represent the various bit flags
FLAG_NO_BYTES = 0x00
FLAG_COMPLETED_PACKET = 0x01
FLAG_INCOMPLETE_PACKET = 0x02

#Create dictionaries to store the data from the packet
data = {}

def decode(data): 
    #TODO: Determine protocol and packet length 
        
    #Parse the data from the packet into the created dictionaries
    #TODO: Add code that will properly parse the data
    
    #Return the dictionaries
    return data

#Main loop
while True:
    #Read in the bytes received
    packet_bytes = sys.stdin.read(BYTES_RECEIVED)
    
    #Check the data for the flag byte
    flag_byte = packet_bytes[0]
    if flag_byte == FLAG_NO_BYTES:
        #No data in the packet, stop processing
        break
    else:
        #Bytes were present, decode them and store in the data dictionary
        data = decode(packet_bytes)