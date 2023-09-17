"""
# TODO: Error-handling
# TODO: Pass arguments to script

import numpy as np 
import scipy as sp

def decoder(data):
    #loading data
    data_o = np.loadtxt(data)
    #resizing the data
    data_i = sp.resize(data_o, (4000, 4000)) 
    #calculating FFT 
    data_fft = np.fft.fft2(data_i) 
    #resizing the FFT 
    data_fft_res = np.resize(data_fft, (5000, 5000)) 
    #taking only the imaginary part of the FFT 
    data_fft_res_i = np.imag(data_fft_res)
    #clipping to make data mappable
    data_clipped = np.clip(data_fft_res_i, -1, 1)
    #computing the argument of the FFT 
    data_arg = np.angle(data_clipped, deg=False) 
    #compute phase 
    data_phase = data_arg * 360
    #compute frequency 
    data_freq = np.multiply(data_clipped, 18000)
    #applying a low-pass filter 
    data_freq_lp = sp.signal.lfilter(np.array([0.001]), 1, data_freq)
    #compute amplitude
    data_amp = np.multiply(data_clipped, 3750)
    #compute probability
    data_prob = sp.signal.welch(0.001, 1, data_amp)
    #plotting probability
    plt.plot(data_prob) 
    #extracting the symbols
    data_syms = sp.signal.find_peaks(data_prob)
    return data_syms