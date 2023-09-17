# TODO: figure out how to modulate the signal

import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

def decode_vdew_tonal_mode(input_signal):
    """
    Takes an input signal in the VDEW tonal mode and decodes it.
    
    Arguments:
        input_signal {np.ndarray} -- The input signal to be decoded
    
    Returns:
        {tuple} -- A tuple containing amplitude and frequency information of the decoded signal in the form (amplitude, frequency)
    """

    # First perform a Fast Fourier Transform (FFT) to generate the frequency 
    # components of the signal
    fft_output = np.fft.fft(input_signal)

    # Find the frequency which contains the maximum amplitude of the signal 
    # components -- this is the frequency of the signal
    max_freq = np.argmax(np.abs(fft_output))
    signal_freq = max_freq / len(input_signal) * 2 * np.pi
    
    # Use a Butterworth filter to get the amplitude of the signal at its
    # frequency
    b, a = signal.butter(4, signal_freq, btype='low')
    frequency_amplitude = signal.filtfilt(b, a, input_signal)
    signal_amplitude = np.sqrt(np.mean(frequency_amplitude**2))

    # Return the signal information in the form of a tuple
    return signal_amplitude, signal_freq