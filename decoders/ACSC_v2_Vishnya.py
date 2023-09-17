#TODO: test script

#Decoder for ACS-C v2 Vishnya
#Used for RF signal intelligence

#Import necessary libraries
import numpy as np
import scipy as sp
from scipy import signal
import matplotlib.pyplot as plt

#Define symbols (cwo, cm, and cm_inv) for ACS-C v2 Vishnya
#Sent as 001
cwo = np.array([0, 0, 1])

#Sent as 000
cm = np.array([0, 0, 0])

#Sent as 111
cm_inv = np.array([1, 1, 1])

def ACS_C_v2_Vishnya_Decoder(data):
    '''Decode data from ACS-C v2 Vishnya.

    Parameters
    ----------
    data : numpy.ndarray
        Raw input data as a numpy array
    
    Returns
    -------
    output : list
        List of 0s and 1s representing decoded data
    '''
    #For each 3-symbol sequence,
    output = []
    for i in range(int(len(data)/3)):
        #Slice out the necessary data
        symbol = data[i*3:(i+1)*3]
        #Compare with the predefined symbols
        if (np.array_equal(symbol, cwo)):
            output.append(1)
        elif (np.array_equal(symbol, cm)):
            output.append(0)
        elif (np.array_equal(symbol, cm_inv)):
            output.append(1)
        #If none of the symbols match, raise error
        else:
            raise ValueError("Symbol decoding failed.")

    #Return decoded data
    return output