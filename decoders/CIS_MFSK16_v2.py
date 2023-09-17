# TODO: Fill out this script with all its components 

import numpy as np
import scipy.signal
from scipy.signal import find_peaks

def cis_mfsk16_v2_decoder(input_signal, baud_rate, modulation_order):

    N = 64 # Number of elements per symbol
    T = 1 / (N * baud_rate) # 'Time for each element'
    t_sample = np.linspace(0, N*T, N + 1) # Define sample times
    t_sample = t_sample[:-1]

    ## Phase Gereration program

    fc = 1 / T # Carrier frequency

    # Define index of carriers used
    k = np.linspace(-fc/(2*baud_rate), fc/(2*baud_rate), 16)
    alpha1 = 0.5
    alpha2 = 0.23
    k_amp = 1/np.sqrt(2)*np.sqrt(1-alpha1-alpha2-np.sqrt((alpha1-alpha2)**2 - 4*alpha1*alpha2))
    phi = np.arange(0, 2*np.pi, 2*np.pi/N) 

    # Generate carrier signals
    c_k = np.zeros((16, N))
    for i in range(16):
        c_k[i, :] = k_amp*np.cos(2*np.pi*k[i]*t_sample + phi*(1 + alpha1*np.cos(2*np.pi*k[i]*t_sample) + alpha2*np.cos(4*np.pi*k[i]*t_sample)))

    # Get signal into pulse shape
    m = 0.2
    q = np.linspace(-15, 15, 31)
    pulse_shape = np.sin((1 + m)*np.pi/2*q) * (np.cos(np.pi/2*q)**m)
    signal_symbol = 0
    sig_in_time = np.convolve