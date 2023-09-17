#!/usr/bin/env python
"""
ReFLEX signal decoder script

TODO
 - add methods to clean and pre-process the signal 
 - design algorithm to detect data within the signal
 - add methods to decode data 
 - create output format
"""

import numpy as np

def signal_cleaner(signal):
    """ 
    This method takes in raw signal and applies low-pass filter
    to attenuate noise in signal, thus improving signal clarity
    """
    ...
    return filtered_signal

def data_detector(signal):
    """
    This method scans the signal to detect bits of data within
    """
    ...
    data_detected = ....
    return data_detected

def prevent_errors(data):
    """
    This method takes in data output of detector and 
    corrects/accounts any errors in received data
    """
    ...
    return corrected_data

def data_decoder(data):
    """
    This method takes in corrected data and decodes 
    data into meaningful information.
    """
    ...
    decoded_data = ....
    return decoded_data

def output_formatter(decoded_data):
    """
    This method takes in decoded data and formats it 
    into output that is suitable for plugging into
    sigint framework.
    """
    ...
    output_data = ...
    return output_data
    
def reflex_decoder(signal):
    """
    Main decoder for ReFLEX signal intelligence
    """
    f_signal = signal_cleaner(signal)
    data = data_detector(f_signal)
    c_data = prevent_errors(data)
    d_data = data_decoder(c_data)
    output = output_formatter(d_data)
    return output