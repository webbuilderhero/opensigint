# TODO: Flesh out certain areas of code

import numpy as np
from scipy import signal

def OFDM_Spectra_Decoder(input_signal, config):
    """ Builds a decorder for Spectra OFDM signal
    Args:
        input_signal: A Signal object
        config: Configuration dictionary to set parameters of decoding
    Returns:
        output_data: The data extracted from the signal"""

    # Read in size of subcarriers and CP length
    Nsc = config['Nsc']
    CP_length = config['CP_len']
    
    # Create OFDMProcessor object based on configuration
    ofdm_proc = OFDMProcessor(Nsc, CP_length)
    
    # Separate unprocessed signal into its constituent time frames
    time_frames = ofdm_proc.frame_signal(input_signal)
    
    # Apply DFT to each of the time frames
    dft_signals = ofdm_proc.apply_dft(time_frames)
    
    # Derive individual subcarriers
    sub_signals = ofdm_proc.derive_subcarriers(dft_signals)
    
    # Subcarrier mapping to determine data subcarriers
    data_carriers = ofdm_proc.map_subcarriers(sub_signals)

    # Extract data from data subcarriers
    output_data = ofdm_proc.extract_data(data_carriers)

    return output_data

class OFDMProcessor:
    """ A class for processing OFDM signals """
    def __init__(self, Nsc, CP_length):
        # Number of subcarriers
        self.Nsc = Nsc
        # Length of Cyclic Prefix
        self.CP_length = CP_length

    def frame_signal(self, input_signal):
        """ Segments an unprocessed signal into individual time frames
        Args:
            input_signal (Signal): The single unprocessed signal
        Returns:
            time_frames (list): List of individual time frames """
        time_frames =