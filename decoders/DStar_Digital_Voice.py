#Todo look into existing decoders for D-star Digital Voice

import scipy
import numpy as np

def decode(data):
    """
    This function takes in signal data (which can be received from a RF sigint framework) in and process it to produce a decode of a D-Star Digital Voice signal.
    
    Parameters
    ----------
    data : str
        The input raw signal data
    
    Returns
    -------
    decoded_data : str
        The decoded signal
    """
    # We need to get the raw signal
    signal = scipy.signal.decimate(data, 2)
    # Compute the power spectrum
    ps = np.abs(scipy.fft(signal))**2
    # Compute frequency info
    freqs = scipy.fftpack.fftfreq(signal.size, 1/2e6)
    # Peak detection
    idx = scipy.signal.find_peaks_cwt(ps, np.arange(1,10))
    peak_freqs = freqs[idx]
    
    # Identify D-Star signaling carriers
    for freq in peak_freqs:
        if self._is_dstar_freq(freq):
            # We found a D-Star carrier
            # Get its decode data
            decoded_data = self._get_decode_data(freq, data)
            return decoded_data
    
    # If we get here, we did not find any D-Star frequencies
    return None

def _is_dstar_freq(self, freq):
    """
    Helper function to check if a given frequency is within the range of 
    a valid D-Star signal.
    
    Parameters
    ----------
    freq : float
        The frequency to check
    
    Returns
    -------
    is_dstar : bool
        Whether or not the given frequency is a valid D-Star signal freq.
    """
    is_dstar = False
    # Look for frequency within given the given range
    if freq > 430