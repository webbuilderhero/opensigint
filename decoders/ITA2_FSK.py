#todo:
#1. Research ITA2 FSK
#2. Research Python decoder scripts

import numpy as np
import scipy.signal as signal
from scipy.fftpack import fft,ifft

#ITA2 FSK format
# Modulation: FSK
# Word length: 8/9
# Symbol rate : 45.4545 bits/second


def decode_FSK(samples):
    #Filter the samples
    filtered_signal=signal.remez(60, [0, 5000, 5500,9000], [1, 0], Hz=20000)
    filtered_samples = signal.lfilter(filtered_signal, 1.0, samples)

    #DTFT
    N=len(filtered_samples)
    x=np.arange(N)
    k=np.arange(N)
    DTFT_result= np.exp(-2j*np.pi*k*x/N)*filtered_samples

    #FFT
    FFT_result = fft(DTFT_result)

    #Find FFT peaks
    FFT_abs = np.abs(FFT_result)**2
    frequency_peaks_index = np.array(np.where(FFT_abs > np.mean(FFT_abs))).T

    #Select two peakes for ITA2 FSK signal
    main_frequency=[]
    for x in frequency_peaks_index:
        if(len(main_frequency)>2):
            break
        else:
            main_frequency.append(x[0])

    #Calculate the symbol rate
    i0=main_frequency[0]
    i1=main_frequency[1]
    T=N/20000 #sampling rate
    symbol_rate = (i1-i0)/T

    #Check if it is ITA2 FSK Signal
    ITA2_FSK_symbol_rate = 45.4545
    if(abs(ITA2_FSK_symbol_rate-symbol_rate)<1):
        #Dec