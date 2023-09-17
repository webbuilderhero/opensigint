# TODO: Figure out input and output format

# imports
import scipy
import matplotlib
import numpy

#This function decodes a signal according to the specifications of the Selex Elsag HF2000 ALE
def HF2000_ALE_decoder(input_signal):
    # convert signal into frequency spectrum
    signal_freq_spec = scipy.fftpack.fft(input_signal)

    # bandstop filter
    out_freq_spec = scipy.signal.firwin(signal_freq_spec, cutoff, nyq=0.5, pass_zero=False)

    # use decoder model to process the signal
    symbol_sequence = decode(out_freq_spec)

    # output
    return symbol_sequence