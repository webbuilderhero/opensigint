"""A script to decode HAL P-Mode Selcall"""
# TODO: add more error-handling

# imports
import numpy as np
import scipy.signal

def HAL_PMode_Selcall(signal):
    """
    Decodes a HAL P-Mode Selcall
    
    Parameters
    ----------
    signal :  array-like
             Raw signal data
    
    Returns
    -------
    (data,freq)
    data : array-like
           The decoded data
    freq : float
           The frequency of the signal
    """
    
    # Get the signal
    sig = np.array(signal)
    
    # Preprocess the signal
    # TODO: Add more filters
    filt_sig = scipy.signal.medfilt(sig, 9)
    filt_sig = signal - filt_sig
    
    # Decode the signal
    data = np.array([int(x) for x in filt_sig[::2]])
    
    # Calculate the frequency
    freq = np.average(np.diff(filt_sig))
    
    # Return the decoded signal and the calculated frequency
    return (data, freq)