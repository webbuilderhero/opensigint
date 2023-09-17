# TODO: investigate what X.25 protocol is and how to decode it

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

#Set up variables for signal parameters
SAMP_RATE = 9600
SUB_CARRIERS = 2
SYMBOL_RATE = SAMP_RATE / SUB_CARRIERS

def decoder(data):
    '''
    Decodes a FM-encoded X.25 signal in the 9600bd rate. 
        Parameters:
        - data: a segments of a signal in an array
    '''
    # calculate the frequency deviation
    freq_dev = SAMP_RATE / (4 * SUB_CARRIERS)

    # bandpass filter the signal
    b, a = signal.butter(4, (freq_dev - 25, freq_dev + 25), btype='bandpass')
    filtered = signal.filtfilt(b, a, data)
    # write the signal out
    wavfile.write('9600fd_x25_filtered.wav', SAMP_RATE, filtered.astype('int16'))

    # determine the output sample rate
    output_samp_rate = SYMBOL_RATE * 2

    # demodulate the signal
    demod = signal.hilbert(filtered)
    demod = signal.resample_poly(demod, SAMP_RATE, output_samp_rate)
    demod = np.array(demod, dtype='float')

    # separate out the pilot and data tones
    pilot_start = int(SAMP_RATE / 8)
    pilot_end = int(7 * SAMP_RATE / 8)
    data_start = int(pilot_end + int(SYMBOL_RATE / 8))
    data_end = int(len(demod))

    pilot_tones = demod[pilot_start:pilot_end]
    data_tones = demod[data_start:data_end]

    # extract the amplitude and