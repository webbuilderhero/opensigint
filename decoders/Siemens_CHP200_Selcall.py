#TODO: Modify script to fit into existing framework

#!/usr/bin/env python

import base64

# This function decodes the Siemens CHP-200 Selcall
def decodeSelcall(selcall):

    # Decode the selcall from base64
    encodedSelcall = base64.b64decode(selcall).decode("utf-8")
	
    # Create an empty array to store the decoded signal
    decodedSelcall = []

    # Loop through and decode the signal bits
    for signalBit in encodedSelcall:
        # If signal bit is '1', append '1' to the array
        if signalBit == '1':
            decodedSelcall.append(1)
        # If signal bit is '0', append '0' to the array
        elif signalBit == '0':
            decodedSelcall.append(0)

    # Return the decoded signal
    return decodedSelcall