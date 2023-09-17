# TODO: Determine how big a data package is coming through 

import RPi.GPIO as GPIO
import time

def decode_CV_786(incoming_signal):
    msg_str = ""
    GPIO.setmode(GPIO.BCM)

    bit_pos = 0
    DATA_PACKET_SIZE = 0  # FILL THIS IN with the determined size.
    
    while bit_pos < DATA_PACKET_SIZE: 
        if incoming_signal[bit_pos] == 1:
            msg_str += "1"
        else:
            msg_str += "0"
        bit_pos +=1
        time.sleep(0.1)
    
    print("Data decoded from video signal is: " + msg_str)
    GPIO.cleanup()

decode_CV_786(incoming_signal) # where incoming_signal is the input video signal