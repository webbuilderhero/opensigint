#TODO:    Make sure to check the API documentation for Kato SB


# import necessary packages
import numpy as np
from matplotlib import pyplot as plt


def kato_decoder(radio_signal):
    """Decoder for Kato SB radio signal
    
    Parameters
    ----------
    radio_signal : array
        Radio signal received

    Returns
    -------
    decoded_message : str
        Decoded message
    """
    
    # Transform the radio signal into fourier transform
    fourierTransform = np.fft.fft(radio_signal)
    
    # Find the frequency from the transformed signal
    frequency = np.fft.fftfreq(fourierTransform.size)
    
    # Use the frequency to decode the message
    message_decoded = ""
    for f in frequency:
        if f in KATO_SB_DICTIONARY.keys():
            message_decoded += KATO_SB_DICTIONARY[f]
    
    return message_decoded


# Dictionary with the different frequencies and the corresponding character
KATO_SB_DICTIONARY = {
    0.2: 'A',
    0.5: 'B',
    2.0: 'C',
    5.0: 'D',
    7.5: 'E',
    10.0: 'F'
    }