# TODO: Check why some frequencies are out of bounds.
#import necessary packages
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

#Define constants used in decoder
#This includes the upper and lower bound of frequencies that were given in Federal Standard 1052
LOWER_FREQ = 225000
UPPER_FREQ = 399000

def decoder(data, sampling_rate, plot_fft=True):
    """Decodes RF signals in accordance with Fed-Std 1052 - a standard for RF signal intelligence.
    
    Parameters
    ----------
    data : 1d array
        The data that needs to be decoded
    sampling_rate : int
        Sampling rate of the given data.
    plot_fft : bool
        Set to True if you want to see the plot of the frequency spectrum of the data.
        
    Returns
    -------
    frequency : float
        Frequency of the RF signal present in the given data
    """
    
    #Calculate FFT
    fft = np.fft.fft(data)
    
    #Plot frequency spectrum
    if(plot_fft):
        fig, ax = plt.subplots(1,1)
        ax.plot(abs(fft))
        ax.set_xlabel('Frequency (Hz)')
        ax.set_ylabel('Amplitude')
        ax.set_title('Frequency Spectrum')
        plt.show()
    
    #Find the frequency of the signal within the specified frequency range
    bins = np.linspace(LOWER_FREQ, UPPER_FREQ, UPPER_FREQ-LOWER_FREQ+1, False)
    frequency,_  = sig.find_peaks(np.abs(fft), width=3, prominence=5, bins = bins)

    #Make sure that one, and only one frequency is found
    if(len(frequency) == 0):
        raise ValueError('No frequency found')
    elif(len(frequency) > 1):
        raise ValueError('