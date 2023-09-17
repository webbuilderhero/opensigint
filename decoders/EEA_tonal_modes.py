# TODO: Test script on sample data

import pandas as pd
import numpy as np

def decode_EEA_tonal_modes(data):
    """
    Decode EEA tonal modes
    """
    
    # Step 1: Convert to Frequency Domain
    fourier = np.fft.fft(data)
    
    # Step 2: Obtain the magnitude of the data
    mags = np.absolute(fourier)
    
    # Step 3: Obtain the power spectrum (value^2)
    powers = np.power(mags, 2)
    
    # Step 4: Calculate the average power per octave (averaging over 12-25 cycles/octave)
    cyclic_octave = powers.reshape(-1, 12)
    avg_octave_power = np.mean(cyclic_octave, axis=1)
    
    # Step 5: 20dB/decade slope resulting in dividing previous power by next power
    next_octave_power = np.roll(avg_octave_power, -1)
    next_octave_power[-1] = 0
    decibels = 20*np.log10(avg_octave_power/next_octave_power)
    
    # Step 6: Tonal modes detected when value in dB is greater than 20dB/decade (20dB higher than adjacent octaves)
    tonal_modes = decibels > 20
    
    # Step 7: Get the indices of the tonal modes detected
    indices = np.where(tonal_modes == True)[0]
    
    return indices