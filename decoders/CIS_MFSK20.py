"""
A script for decoding cis mfsk-20 signals

TODO: 
"""

# import the necessary libraries
import numpy as np
import scipy as sp

# define the sample rate used for the signal
sample_rate = 20e6

# generate the-'polyphase filterbank (PFB)'s impulse response
def generate_IR(window_type, taps, bandwidth):
    # create a window with the specified type and length
    window = sp.signal.get_window(window_type, taps)
    # define offset amount in the frequency domain
    offset = bandwidth/taps
    # create an list of the frequency domain offset values
    frequencies = [offset*x for x in range(taps)]
    # define the impulse response for the PFB
    IR = sp.ifftshift(window*np.exp(-(1j)*2*np.pi*frequencies))
    return IR

# function to correctly demodulate signal
def signal_demod(input_signal, IR_taps, window_type, bandwidth_k):
    # length of the input signal
    N = len(input_signal)
    # generate the impulse response
    IR = generate_IR(window_type, IR_taps, bandwidth_k)
    # perform the demodulation of the signal based on the impulse response
    out_signal = np.convolve(input_signal, IR, mode='same') / IR_taps
    # pad the signal to account for the delay from the PFB
    out_signal = np.pad(out_signal, int(IR_taps/2), mode='constant', constant_values=0)
    # remove the padded values
    out_signal = out_signal[int(IR_taps/2):(N+int(IR_taps/2))]
    return out_signal

# function to decode signal
def sigint_decoder(input_signal, sample_rate):
    # perform the signal demodulation
    output_signal = signal_demod(input_signal, 20, 'hamming', 4*sample