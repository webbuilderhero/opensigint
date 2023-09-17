#TODO: Update Decoder script for Jenal/Schuemperlin Selcall CCIR493-4

"""
Decoder script to process Jenal/Schuemperlin Selcall CCIR493-4 signals.
"""

import numpy as np
import scipy.signal

def jenal_selcall_decoder(sig, fs):
    """ Jenal/Schuemperlin Selcall CCIR493-4 Decoder

    Parameters
    ----------
    sig: numpy array 
        signal to process
    fs: float 
        sample rate of signal

    Returns
    -------
    receivedCode: str
        received Selcall code
    """

    # Set Constants
    f0 = 11025 #kHz
    n = 8 # tone separation

    # Create Tones
    f = [f0 * (2**(1/n))**i for i in range(n)]

    # Initialize Variables 
    receivedCode = ""

    # Filter Input Signal
    filteredSignals = [scipy.signal.lfilter(filt,1,sig) for filt in [scipy.signal.firwin(4096,[freq-1,freq+1],fs=fs,pass_zero=False) for freq in f]]

    # Convert tone signals to Magnitude and find Max
    mag = [np.max(np.abs(filt)) for filt in filteredSignals]

    # Decode each tone
    for m in mag:
        # Tone frequency corresponds to encoded bit
        if m > 0.1:
            receivedCode += "1"
        else:
            receivedCode += "0"
    
    # Return Decoded Code
    return receivedCode