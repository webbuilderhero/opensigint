"""POCSAG Telemetry Decoder"""
import numpy as np

# TODO: Add appropriate library to convert raw waveforms to POCSAG protocol

def decode(waveform_data):
    """Decode POCSAG protocol from waveform
    
    Parameters
    ----------
    waveform_data : array_like
        Raw waveform data associated with POCSAG protocol
        
    Returns
    -------
    decoded_data : list
        List of messages decoded from waveform
    """
    
    # Initialize decoded_data
    decoded_data = []
    
    # TODO: Write code to convert raw waveforms to POCSAG protocol
    
    # Once waveforms are converted, process them to decode message
    # Iterate through the waveforms
    for waveform in waveform_data:
        # Get raw message from waveform
        message = raw_message_from_waveform(waveform)
        
        # Unpack raw message to get individual fields
        (id_word, num_words, message_code, check_sum, address_bits) = decode_raw_message(message)
        
        # Verify checksum
        if not verify_checksum(message_code, check_sum):
            continue

        # Extract bits from message_code
        message_bits = unpack_bits(message_code)
        
        # Generate decoded message from message bits
        decoded_message = decode_bits_to_message(message_bits, address_bits)
        
        # Append decoded message to list of decoded messages
        decoded_data.append(decoded_message)
        
    return decoded_data

def raw_message_from_waveform(waveform):
    """Generates raw message from POCSAG waveform

    Parameters
    ----------
    waveform : array_like
        Waveform associated with POCSAG protocol

    Returns
    -------
    raw_message : str
        Raw message from the waveform
    """
    # TODO: Write code to convert waveform to raw message
    
def decode_raw_message(message):