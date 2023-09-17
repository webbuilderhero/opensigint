#import libraries
import numpy as np
import scipy as sp

#Define sampling rate
Fs = 6000000

#Define DBPSK transformer
def DBPSKTransformer(signal_input):
    #Create empty lists
    signal_output = []
    symbols = []
    
    #Loop through signal input
    for i in range(len(signal_input)):
        if i == 0:
            #First bit is set as 0
            signal_output.append(0)
            q=0
            symbols.append(0)
        else:
            #Compare current bit to previous bit
            if signal_input[i] != signal_input[i-1]:
                #If different set new bit 
                q=q*(-1)
                signal_output.append(q)
                symbols.append(q)
            else:
                #Else keep same bit
                signal_output.append(q)
                symbols.append(q)
    #Normalize
    TXSIG = np.array(signal_output, dtype = 'int')
    TXSIG *= 0.99 / np.max(abs(TXSIG))
    return TXSIG, symbols

#Define DBPSK Detector
def DBPSKDetector(signal_input):
    #Create empty list
    signal_output = []
    
    #Loop through signal input
    for i in range(len(signal_input)):
        #Check for sign change
        if signal_input[i] < 0:
            signal_output.append(1)
        else:
            signal_output.append(0)
    return signal_output
    
#Define Main Decoding Function
def DecodeDBPSKSignal(data):
    #Convert to complex numbers
    data_complex = [complex(x,0) for x in data]
    
    #Call Transformer & Detector
    TXSIG, Encoded_Data = DBPSKTransformer(data_complex)
    Decoded_Data = DBPSKDetector(TXSIG)
    
    return Encoded_Data,