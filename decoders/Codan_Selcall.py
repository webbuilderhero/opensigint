#TODO: obtain spectrogram of signal for decoding

import numpy as np
import scipy as sp
from scipy.signal import decimate

#Decimation Factor
dec_factor = 7

#Input signal
signal = np.random.random(100)

#Decimate the signal
signal_dec = decimate(signal, dec_factor)

#Find the location of peaks
peaks = sp.signal.find_peaks(signal_dec)[0]

#Create a dictionary to store the Selcall codewords
Selcall_dict = {1:[0,0,1,1,1,1,0],
                2:[1,0,1,1,0,1,0],
                3:[1,1,0,1,1,0,1],
                4:[0,1,1,1,1,0,1],
                5:[0,1,1,1,0,1,1],
                6:[1,0,1,1,1,0,0],
                7:[0,1,1,1,0,0,0],
                8:[1,1,0,1,1,1,1]}

#Create the decoder function
def selcall_decoder(sig, pks, dct):
    #Make sure all signals are the same size
    pk_len = len(list(dct.values())[0])
    #Create an output list
    output_codes = []
    #Loop through each peak
    for pk in pks:
        #Create an empty list to store the code
        curr_code = []
        #Loop through the points of the peak
        for p in range(pk_len):
            #Append the current signal point
            curr_code.append(sig[pk+p])
        #Loop through the 
        for k, v in dct.items():
            #If the code matches a code in the dict, append the current code to the output list
            if v == curr_code:
                output_codes.append(k)
    return output