"""
SIGINT Decoder for REACH HI

This script decodes REACH HI signal intelligence. It uses the Tonal Mode system to decode the signal.

"""

#TODO: Finish writing the script below

from scipy.io import wavfile

def decode(file):
    """ Decodes the REACH HI signal intelligence

    Parameters
    ----------
    file : str
        file path of the .wav file containing the signal intelligence

    Returns
    -------
    decoded_signal : str
        decoded signal intelligence
    """


    # Read the .wav file
    sample_rate, data = wavfile.read(file)


    # Calculate the frequencies of the tonalmode
    speed = sp.fft(data)
    freqs = sp.fftfreq(len(speed))


    # Create a table of the frequencies and their corresponding characters
    freq_table = {
        1000.0 : 'A',
        1150.0 : 'B',
        1300.0 : 'C',
        1450.0 : 'D',
        1600.0 : 'E',
        1750.0 : 'F',
        1900.0 : 'G',
        2050.0 : 'H',
        2200.0 : 'I',
        2350.0 : 'J',
        2500.0 : 'K',
        2650.0 : 'L',
        2800.0 : 'M',
        2950.0 : 'N',
        3100.0 : 'O',
        3250.0 : 'P',
        3400.0 : 'Q',
        3550.0 : 'R',
        3700.0 : 'S',
        3850.0 : 'T',
        4000.0 : 'U',
        4150.0 : 'V',
        4300.0 : 'W',
        4450.0 : 'X',
        4600.0 : 'Y',
        4750.0 : 'Z'
    }


    # Decode the signals
    decoded_signal = ''
    for idx, freq in enumer