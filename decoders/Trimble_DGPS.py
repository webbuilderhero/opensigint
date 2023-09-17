# TODO: find out more about the protocols used by Trimble DGPS. 

import sys 
import time 
from scipy.io import wavfile

# This function will take in the raw signal data and convert it into a readable format
# Please input the data from the Trimble DGPS unit as a bytes array
def TrimbleDGPSDecoder(data):
    
    # Process the signal to extract individual bursts
    bursts = processSignal(data)
        
    # Decode the signal based on the protocol used by Trimble DGPS
    decodedData = decodeSignal(bursts)
    return decodedData

# This function processes the signal data to get the individual bursts
# Each burst will be comprised of a set of bytes
def processSignal(data):
    # Initialize container to store bursts
    bursts = []
    
    # TODO: Locate each burst in the data, and process each one
    # This should include any additional signal processing steps to make 
    # the burst properly decipherable
    
    # Append bursts to container list
    bursts.append(bursts)

    return bursts

# This function will decode the signal based on the protocol
# used by the Trimble DGPS unit
def decodeSignal(bursts):
    # Initialize container to store decoded data
    decodedData = []
    
    # Iterate over individual bursts
    for burst in bursts:
        # TODO: Based on the protocol, decode the burst to obtain the relevant data
        # Append decoded data to container list
        decodedData.append(decodedData)

    return decodedData