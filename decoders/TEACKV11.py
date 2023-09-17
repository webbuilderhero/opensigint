#!/usr/bin/env python

# TODO: Get TEAC-KV11 specific protocols from the manufacturer

# Imports 
import sys
import numpy as np
import pandas as pd
from scipy.signal import detrend
from scipy.fftpack import fft, fftfreq

# Functions 
def TEAC_KV11Decode(sig):

    # Assure Signal type compatibility
    if not isinstance(sig, np.ndarray):
        sys.exit("Signal must be a numpy.ndarray.")

    # Get sampling frequency
    fs = getSamplingFrequency(sig)
    
    # Frequency Analysis
    freq_sig = fft(sig)    # Fast Fourier On Sig
    freqs = fftfreq(sig.size, 1/fs)  # Get associated frequencies
    f_sig = np.absolute(freq_sig)    # Absolute of signal

    # Identify peaks in spectrum
    peak_sig = find_peaks(f_sig)

    # Calculate Probabilities of Occurence
    prob_peak_sig = calculate_prob_occur(f_sig, peak_sig)

    # Create Dataframe
    out_df = pd.DataFrame()
    out_df['Frequencies (Hz)'] = freqs
    out_df['Absolute Signal'] = f_sig
    out_df['Signal Peaks'] = peak_sig
    out_df['Probability of Occurence'] = prob_peak_sig
    out_df = out_df.round(4)

    # Return Output
    return out_df

def getSamplingFrequency(sig):
    """
    Calculates signal's sampling frequency in Hertz. 

    Args:
        sig (np.ndarray): Filtered signal. Must be type numpy.ndarray. 
    
    Returns:
        float: Sampling frequency in Hertz.
    """

    # Get signal length 
    sig_len = sig.size

    # Create time