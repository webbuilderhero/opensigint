# Used for decoding D-Star RF signals for sigint

# TODO: Figure out encryption used

import numpy as np
import rf_decoder_framework as framework

def decodeDStarSignal(signal):
    """
    Function to decode a D-Star RF signal
    
    Parameters
    ----------
    signal : numpy array
        The array of signal data

    Returns
    -------
    decoded_signal : array
        The decoded array of signal data
    """
    
    # Get the frequency of the signal
    freq = np.fft.rfftfreq(len(signal), 1/framwork.sample_rate)
    
    # Get current frequencies of the signal
    signal_frequencies = np.abs(np.fft.rfft(signal))
    
    # Find the frequency of the signal at max power
    max_freq = freq[np.argmax(signal_frequencies)]
    shift_angle = np.angle(np.cos(2 * np.pi * max_freq))
    
    # Apply phase shift
    decoded_signal = signal * np.exp(1j * shift_angle)
    
    # Conversion to a power signal
    decoded_signal = np.square(np.abs(decoded_signal))
    
    return decoded_signal