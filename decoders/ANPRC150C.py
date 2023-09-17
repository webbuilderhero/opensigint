#TODO: Check FM and frequency range in documentation

#Decoder Script For RF Signal Intelligence for AN/PRC-150C
#Assumes you have the necessary drivers for the receiver

import serial

#Open a connection with the receiver
serialPort = serial.Serial("/dev/ttyS0", 9600, timeout=1)

#Set the receiver parameters 
serialPort.write(b'\xFE\x44\x00\x01\x03\x00\x03\x00') #Set mode to RF Channel Scan
serialPort.write(b'\xFE\x44\x00\x01\x04\x01\x00\x02') #Set frequency range 

#Scan for signals
while True:
    serialPort.write(b'\xFE\x44\x00\x01\x04\x01\x00\x03') #Enable receiver
    data = serialPort.read(size=8)
    if (data):
    	#Decode signal & print it (if you can!)
    	output = decodeSignal(data)
    	return output