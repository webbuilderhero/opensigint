'''
#TODO: 
1. research the WSA5000 and its native API 
2. Implement methods for connecting to the WSA5000 
3. Create functions for decoding/analyzing signals from the device

import numpy as np
import scipy
import matplotlib.pyplot as plt

#import methods from WSA5000 API 
#TODO: research WSA5000 API and include necessary modules for connection and decoding

#connect to WSA5000
def connect_wsa5000(ip_address):
    #TODO: implement API functions for connecting to WSA5000
    return None

#capture if signal
def capture_signal():
    #TODO: implement API functions for capturing if signal
    return None

#decode signal
def decode_signal(signal):
    #TODO: implement API functions for decoding if signal
    #TODO: use scipy or numpy methods to filter and display signal
    return None

#plot frequency/amplitude of signal
def plot_signal(signal):
    #TODO: use pyplot or matplotlib to visualize the signal
    return None

#main method
def main():
    #TODO: add code for forming complete IP address
    #TODO: add code for using functions from WSA5000 API
    ip_address = ""
    connect_wsa5000(ip_address)
    signal = capture_signal()
    decoded_signal = decode_signal(signal)
    plot_signal(decoded_signal)

if __name__ == "__main__":
    main()