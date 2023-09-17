# TODO: research EIA tonal mode

import numpy as np 

def eia_tonal_decoder(signal):
    """
    EIA tonal decoder for RF signal intelligence. 
    Takes a numpy array of RF signal (in normalized [-1,1] range) as input and outputs frequency and amplitude of each tone detected in the signal.

    Parameters
    ----------
    signal : np.ndarray
        A numpy array of RF signal (in normalized [-1,1] range).

    Returns
    -------
    tones : np.ndarray
        Numpy array containing the detected tones in the signal. Each row of the array corresponds to a detected tone, with the first column representing the frequency of the tone and the second column representing the amplitude of the tone.
    """
    peak_freqs, peak_amps = find_peaks(signal) #get frequencies and amplitudes at peaks
    tones = [] #list to hold (frequency, amplitude) tuples for each tone
    
    for i, peak_amp in enumerate(peak_amps):
        detected_tones = find_tones(peak_amp, peak_freqs[i]) #find tones in the signal with the given peak frequency and amplitude
        for tone in detected_tones: #append all detected tones to the 'tones' list
            tones.append(tone)
    
    tones = np.array(tones) #convert list into a numpy array
    return tones

# utility functions
def find_peaks(signal):
    """
    Helper function to find peaks in the input signal. 
    Takes a numpy array of RF signal (in normalized [-1,1] range) as input and outputs frequencies and amplitudes at those peaks.

    Parameters
    ----------
    signal : np.ndarray
        A numpy array of RF signal (in normalized [-1,1] range).

    Returns
    -------
    peak_freqs : np.ndarray
        Numpy array containing the frequencies of the detected peaks in the signal.
    peak_amps : np.ndarray
        Numpy array containing the amplitudes of the detected peaks in the signal.
    """
    peak_fre