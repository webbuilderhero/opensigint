# TODO: Need better description of FEC

# import necessary libraries
import numpy as np
import scipy
from scipy import signal

# define constants
SYMBOL_RATE = (31/2) # symbol rate of 31/2 symbols per bit (QPSK31)
SYMBOL_PERIOD = 2/31 # symbol period of 2/31
BIT_RATE = 31 # bit rate of 31 bits/s

def qpsk31_decoder(rx_signal):
    """Decodes input signal using the QPSK31 FEC scheme.
    
    Parameters
    ----------
    rx_signal : array
        Input signal to be decoded

    Returns
    -------
    output_bits : array
        Array of decoded bits
    """
    # calculate number of samples needed from symbol period
    num_samples = int(np.ceil(SYMBOL_PERIOD / np.ptp(rx_signal)))
    # calculate t-spaced vector from symbol period 
    time_vector = np.arange(0 , SYMBOL_PERIOD, (SYMBOL_PERIOD/num_samples))
    # interpolate original samples
    interpolated_samples = scipy.interpolate.interp1d(rx_signal[::2], rx_signal[1::2])(time_vector)
    # format samples as complex numbers
    complex_samples = interpolated_samples[::2] + 1j*interpolated_samples[1::2]
    # scale samples to unit circle 
    normalized_samples = complex_samples/(np.abs(complex_samples).max())

    # calculate FFT for correlation
    fft_samples = np.fft.fft(normalized_samples) 
    fft_correctness = np.sum(np.abs(fft_samples[0::4]))
    fft_error = np.sum(np.abs(fft_samples[1::4]))
    fft_ratio = fft_correctness/fft_error