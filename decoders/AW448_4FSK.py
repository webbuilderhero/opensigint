# TODO: Look into the specifics of what AW448 4FSK stands for

import numpy as np
from scipy.fftpack import fft, ifft, fftshift

def decodeAW448FSK(data):
    # This section sets up the parameters for the filter 
    '''
    Fs = Sampling frequency
    f0 = lowest frequency for the filter
    f1 = highest frequency for the filter
    N  = filter width
    '''
    Fs = 20e3
    f0 = 0.4e3
    f1 = 1.4e3
    N = 128

    # This section applies the filter to the data 
    h = np.sinc(2 * f0 / Fs * (np.arange(N) - (N - 1) / 2.)) * \
        np.blackman(N)  # Create the filter
    h *= (f1 - f0)  # Scale the filter
    filtered_output = np.convolve(data, h)  # Apply the filter on the data

    # This section performs the FSK demodulation
    fft_data = fftshift(fft(filtered_output))  # Perform FFT on the data
    centfreq = (f1 - f0) / 2. + f0  # Compute the carrier frequency
    idx = np.argmin(abs(np.fft.fftfreq(fft_data.size, Fs) - centfreq))  # Find the carrier frequency index
    demod_data = np.angle(fft_data[idx])  # Generate the demodulated data

    return demod_data  # Return the demodulated data