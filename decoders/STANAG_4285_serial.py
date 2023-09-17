# TODO: modify for specific decoder parameters 

import serial

SERIAL_PORT = 'COM3'
BAUD_RATE = 115200

# Relevant Stanag 4285 document
DOCUMENT = 'stanag_4285.pdf'

# Create Serial port instance
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

# Open the Stanag 4285 document to find decoder parameters
doc = open(DOCUMENT, 'r')
mode = int(dis.readlines(3))

# Initialize variables 
packet = []

while True:
    # Read each byte from the serial port 
    byte = ser.read()

    # Check for start of packet
    if byte == 0x55:
        # Start collecting packet
        packet.append(byte)
    elif byte == 0xb3:
        # End of packet
        packet.append(byte)

        # Parse packet according to Stanag 4285
        pkt_len = packet[1]
        message_type = packet[2]

        # Identify packet type
        if mode == 0:
            payload = packet[3:-3]
        elif mode == 1:
            payload = packet[4:-3]
        # TODO: add code for remaining modes

        # Handle information
        if message_type == 0:
            # TODO: handle type 0 message 
        elif message_type == 1:
            # TODO: handle type 1 message 
        
        # Reset packet data
        packet = []