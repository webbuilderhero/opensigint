# TODO: Define Selcall Model for Barrett

# imports
import numpy as np
import scipy.io.wavfile as wav
import scipy.signal as sig
from scipy.fftpack import fft

# constants
FS = 8000 # sample rate
SELCALL_PERIOD = 8.3 # milliseconds

# signal processing functions
def apply_windowing(signal):
    """
    Applies windowing to a signal.
    
    Parameters:
    signal (ndarray): The target signal to apply windowing to.
    
    Returns:
    windowed_signal (ndarray): The windowed signal.
    """
    windowed_signal = np.apply_along_axis(lambda frame: frame*sig.blackmanharris(frame.size), 1, signal)
    return windowed_signal

def fft_transform(signal, fs):
    """
    Performs the Fast Fourier Transform on a signal.
    
    Parameters:
    signal (ndarray): The target signal
    fs (int): The sampling frequency of the signal in Hz.
    
    Returns:
    fft_output (ndarray): The result of the FFT on the signal.
    """
    fft_output = fft(signal, fs)
    return fft_output

def decode_selcall(fft_output):
    """
    Decodes a Selcall using the output of an FFT.
    
    Parameters:
    fft_output (ndarray): The output of an FFT on a signal.
    
    Returns:
    code (int): The decoded Selcall code.
    """
    # TODO: define algorithm for decoding Selcall from FFT output
    code = 0
    return code

# main program
# load audio file
audio_file_loc = 'path/to/wave/audio/file'
fs, data = wav.read(audio_file_loc)

# apply window
windowed_signal = apply_windowing(data)

# perform FFT
fft_output = fft_transform(