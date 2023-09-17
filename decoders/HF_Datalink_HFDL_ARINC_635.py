#TODO (if needed):
# -Add support for any other protocols needed
# -Create a new function to parse through HFDL headers

import sys
import os
import time

#Global Variables
protocol_name = "HF Datalink HFDL ARINC 635"

#Function to decode the given frame
def decoder(frame):
    frame_type = None
    #Check if frame is HFDL ARINC 635 protocol, if not return None
    if frame[0] != 0xB:
        return frame_type

    #Extract the Frame Type from the frame
    if frame[1] == 0x01:
        frame_type = "R-Code"
    elif frame[1] == 0x02:
        frame_type = "F-Code"
    elif frame[1] == 0x03:
        frame_type = "T-Code"
    elif frame[1] == 0x04:
        frame_type = "A-Code"
    elif frame[1] == 0x05:
        frame_type = "O-Code"

    #Return the Frame Type
    return frame_type

#Function to detect for frames of HFDL ARINC 635 protocol
def detect_frame(sample):
    #Check for the Begin BYTE (0xB) which is present in all HFDL ARINC 635 frames
    if sample[0] == 0xB:
        return True

    #If Begin BYTE is not present, return False
    else:
        return False