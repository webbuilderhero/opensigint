"""
Decoder for dPMR446 - Tiers I and II

Created by: (Name)
Date: (Date)

TODO:
    * Need to figure out what type of RF signals to expect. 
    * Need to determine which encoding standards and formats are appropriate for decoding.
    * Need to determine any additional data or information required to conduct an effective decode. 

"""

import sys
import logging

ONE_POINT_FIVE_K_HZ = 1500.0

def dPMR_decoder_446_I_1_II(signal):
    """Decodes dPMR Tier I and II signals.
    
    Args:
        signal (str): The signal to be decoded.
    
    Returns:
        A decoded message indicating the type of message (voice, data, etc).
    """
    # Determine the frequency of the signal.
    frequency = determine_frequency(signal)

    # Determine if the signal is a Tier I or Tier II packet.
    if frequency < ONE_POINT_FIVE_K_HZ:
        message_type = decode_tier_I_packet(signal)
    else:
        message_type = decode_tier_II_packet(signal)

    # Return the decoded message type.
    return message_type

def determine_frequency(signal):
    """Determines the frequency of the signal.
    
    Args:
        signal (str): The signal to be decoded.
    
    Returns:
        The frequency of the signal as a float.
    """
    # TODO: Code to determine frequency of the signal.

    return frequency

def decode_tier_I_packet(signal):
    """Decodes a Tier I packet.
    
    Args:
        signal (str): The signal to be decoded.
    
    Returns:
        The message type (voice, data, etc).
    """
    # TODO: Code to decode Tier I packets.

    return message_type

def decode_tier_II_packet(signal):
    """Decodes a Tier II packet