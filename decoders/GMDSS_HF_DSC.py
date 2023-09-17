#!/usr/bin/python

"""
GMDDS HF DSC Decoder
Author: [Your Name]
Date: [Today's Date]
"""

# DECODING IMPORTS
import math

# FRAMEWORK IMPORTS
import signal_processing

# TODO: Add any additional imports needed

# BUILD DECODER CONSTANTS
BIT_NOMINAL = 1.5 # Nominal bit length
BIT_TOLERANCE = 0.2 # Allowed tolerance for bit recognition
SAMPLE_RATE = 8 # Sample rate

# TODO: Add any additional constants


def detect_mark_bits(in_signal, sample_rate):
    """
    Decodes the the given mark bits from the given signal.
    Identifies the bits based on the sample rate
    Args:
        in_signal (array): The signal array
        sample_rate (int): The sample rate of the signal
    Returns:
        mark_bits (list): A list containing the mark bits
    """
    # Initialize empty array
    mark_bits = []
    
    # Iterate through signal
    for i in range(len(in_signal)):
        if i == 0:
            # First sample, not valid
            continue

        # Calculate rate of change
        rate_of_change =  abs(in_signal[i] - in_signal[i-1])

        # Check if mark bit found
        if rate_of_change > BIT_NOMINAL - BIT_TOLERANCE and rate_of_change < BIT_NOMINAL + BIT_TOLERANCE:
            # Mark bit found
            mark_bits.append(1)
        else:
            # No mark bit found, default to 0
            mark_bits.append(0)
   
    # Return marked bits 
    return mark_bits

def decode_hf_dsc(in_signal):
    """
    Decodes GMDSS HF DSC from the given signal
    Args:
        in_signal (array): The signal array
    Returns:
        hf_dsc_info (dict):