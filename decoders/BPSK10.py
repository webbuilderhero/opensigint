# Decode BPSK 10 signal #
# TODO - Connect this script to framework #

#Import libraries
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# Decode the signal
def decode_BPSK10(input_signal):
    #Filter with low pass filter
    filtered_signal = sp.signal.lfilter(LP_filter_coefficients, 1.0, input_signal)

    #Parse data packet
    packets = sp.signal.lfilter(packet_split_coefficients, 1.0, filtered_signal)

    #Differentiate data packets
    bpsk_data_symbols = np.diff(packets,n=1,axis=0)

    #Binarize data
    bpsk_symbol_map = {-1.0: 0, 1.0 : 1}
    bpsk_data_bits = [bpsk_symbol_map[symbol] for symbol in bpsk_data_symbols]

    #Generate output data
    return bpsk_data_bits