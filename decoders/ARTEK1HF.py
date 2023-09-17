"""
Decoder for ARTEK-1HF RF Signal Intelligence

TODO:
    - Add support for other frequencies
    - Add support for different modulation
"""

# Imports
import signal_processing as sp

# RF Parameters
CENTER_FREQ = 1.8 # GHz
BW = 20 # MHz

# Modulation Parameters
BAUD = 1000 # Bits/Second
ENCODING = "BPSK"

def decode_ARTEK_1HF(signal):
    """Decodes input signal based on ARTEK-1HF parameters

    Args:
        signal (np.array): The signal to decode
    
    Returns:
        decoded_signal (np.array): The decoded signal
    """
    # Downconvert
    downconverted_signal = sp.downconvert(signal, CENTER_FREQ, BW)

    # Demodulate
    decoded_signal = sp.demodulate(downconverted_signal, baud=BAUD,
                                  encoding=ENCODING)

    return decoded_signal