# Import required Libraries
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# TODO: Drop in SigInt framework

# Function to convert bit array into Nibbles
def bit2nibble(bits):
    """
    Converts bits to four symbol values (nibbles)
    """
    nibbles = np.zeros(len(bits)//4)
    
    for i in range(len(nibbles)):
        nibbles[i] = bits[i*4:(i+1)*4].dot([2**j for j in range(4)])
        
   return nibbles

# Decode transfer is used to decode a file within the AX.25 FSK protocol
def decodeTransfer(f):
    """
    Decodes an RF signal encoded with AX.25 FSK protocol
    **This will need to be further adapted to the specific protocol.
    """
    # Parameters of the AX.25 FSK protocol which may need to be adjusted
    low_freq = 1.2
    high_freq = 2.4
    Fs_rx = 20.0
    baud = 600.0
    N = int(Fs_rx/baud)
    
    # Construct two filters
    flp = np.sinc(2*low_freq*(np.arange(N) - N/2.))
    flp = flp * np.blackman(N)
    flp = flp / np.sum(flp)
    fhp = np.sinc(2*high_freq*(np.arange(N) - N/2.))
    fhp = fhp * np.blackman(N)
    fhp = fhp / np.sum(fhp)
    fkm = np.convolve(flp - fhp,f[:-N+1])
    
    # Usage of the Signal to Noise Ratio to improve decoding performance
    SNR_thres = 0.01
    BER_thres = 0.1
    SNR_val_min =-20
    SNR_val = SNR_thres