import numpy as np

# TODO: double check syntax for BPSK220

def bpsk220_decoder(bpsk_in, fs, T_symb):
    """
    Decodes a BPSK-220 signal.

    Parameters:
        bpsk_in - Symbols input in the form of an array.
        fs - Sampling frequency of the signal.
        T_symb - Symbol period of the signal in s. 

    Returns:
        Decoded bits as an array

    """

    # Create a sine signal to compare with the BPSK-220 signal
    t =np.arange(0, T_symb+1/fs, 1/fs) # determine sample time
    sine220 = np.sin(2*np.pi*220*t) # create sine signal at 220Hz

    decodedBitStream = [] # decoded bit stream
    for i in range(len(bpsk_in)-len(sine220)):
        x = 0 # set x = 0
        for j in range(len(sine220)):
            x += bpsk_in[i+j]*sine220[j]
        if x <= 0: # if x is barrier or less, bit is logically 0
            decodedBitStream.append(0)
        else: # if x is greater than barrier, bit is logically 1
            decodedBitStream.append(1)
    return decodedBitStream