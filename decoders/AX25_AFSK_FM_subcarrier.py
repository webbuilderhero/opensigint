#This solution is for a decoder for AX.25 AFSK FM subcarrier. It is meant to be used as part of a RF signal intelligence framework.

#TODO: Ensure decoded message has the relevant header fields and is otherwise accurately decoded as a valid AX.25 formatted frame 

import numpy as np
import scipy.signal as signal
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

def ax25Decode(filename, baud, bw, fc):
    """
    This function reads in a .wav file containing an AX.25 AFSK FM subcarrier signal and decodes it. 

    Parameters
    ==========
    filename : str
        Name of .wav file containing AX.25 AFSK FM subcarrier signal
    baud : int
        The bit rate (bps) being transmitted
    bw : int
        The bandwidth of the transmitted signal
    fc : int
        The centre frequency of the transmitted signal

    Returns
    =======
    decoded_signal : list
        A list containing the decoded bits

    """
    
    #Read in .wav file
    fs, data = wav.read(filename)

    #Calculate Symbol Timing
    T_baud = 1/baud
    sps = round(T_baud * fs)

    #Define tones for AX.25
    f1 = fc-bw/2
    f2 = fc+bw/2

    #Generate Coefficient Arrays
    F1_coeff = signal.firwin(numtaps=sps, cutoff=f1, fs=fs, window="blackman") #blackman window
    F2_coeff = signal.firwin(numtaps=sps, cutoff=f2, fs=fs, window="blackman") #blackman window

    #Filter array for each frequency
    f1_samps = signal.lfilter(F1_coeff, 1.0, data)
    f2_samps = signal.lfilter(F2_coeff, 1.0