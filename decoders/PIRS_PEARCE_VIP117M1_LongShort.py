# TODO: more research needed to determine what PIRS, PEARCE, and VIP-117M1 mean

import math as m 

# Contains a dictionary of key values used to decode signal
keyValues = {"Long":1, "Short":0}

def decode(signal):
    # Split the signal into its underlying components
    components = signal.split(' ')

    # Convert the signal components into the correct values
    decodedSignal = ""
    for component in components:
        decodedSignal += str(keyValues[component])

    # Finish the conversion process
    return m.baseConvert(decodedSignal, 2, 16)