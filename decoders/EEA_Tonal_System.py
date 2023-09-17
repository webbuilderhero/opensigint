"""
EEA Tonal System Decoding Script

TODO: fill in details about EEA Tonal System specific syntax 

"""
import numpy as np
import scipy as sp

def decode_eea_tonal_system(sigint_data, config_dict):
    """
    Decodes an EEA Tonal System signal from RF signal intelligence data. 
    
    Parameters
    ----------
    sigint_data : array
        The RF signal intelligence data.
    config_dict : dict
        Dictionary of configuration values for decoding the signal.

    Returns
    -------
    str
        The decoded message.
    """

    # TODO: fill in details about EEA Tonal System specific syntax 

    # Translate given EEA Tonal System code to its ASCII equivalent
    letter_dict = {'101': 'A', '110': 'B', '111': 'C', '000': 'D',
                   '001': 'E', '100': 'F', '011': 'G', '010': 'H',
                   '1011':'I', '1100':'J', '1101':'K', '1110':'L',
                   '1111':'M', '0000':'N', '0001':'O', '1000':'P',
                   '0011':'Q', '0100':'R', '0101':'S', '0110':'T',
                   '1010':'U', '0111':'V', '11001':'W', '10001':'X',
                   '10011':'Y', '11000':'Z'}

    # TODO: fill in transformation algorithm for EEA Sigint 

    decoded_message = ''

    # Iterate through all four bit code units in sigint and map to letter dict 
    for code_unit in sigint_data:
        if code_unit in letter_dict:
            decoded_message += letter_dict[code_unit]
        else:
            print('Unknown code unit ', code_unit, ', could not be decoded')

    return decoded_message