"""Tonal System Decoder for NATEL

@todo: Determine frequency ranges for each tonal audio frequency 

"""
import itertools
import numpy as np

# Constants 
NATEL_TONE_FREQUENCY = [178.4, 148.4, 156.7, 173.9]

def natrel_tonal_system_decode(signal):
    """Decoder for NATEL Tone System

    Parameters
    ----------
    signal : array_like
        The signal array containing frequency components

    Returns
    -------
    decoded_string : str
        Decoded signal in string format

    """
    num_tones = len(NATEL_TONE_FREQUENCY)
    signal_magnitudes = [signal[f] for f in NATEL_TONE_FREQUENCY]

    def decode_tone(tone):
        """Decodes the given tone

        Parameters
        ----------
        tone : int
            Tone to decode

        Returns
        -------
        tone_code : str
            Decoded tone code
        """
        if tone < 0.1:
            return '0'
        else:
            return '1'

    # Construct pairs of tones
    tone_pairs = list(itertools.combinations(signal_magnitudes, num_tones))

    bit_stream = []
    for tp in tone_pairs:
        # Decode each tone
        bit_stream.append(decode_tone(tp[0]) + decode_tone(tp[1]))

    decoded_string = ''.join(bit_stream)

    return decoded_string