# TODO: Test and debug

# imports 
import numpy as np
import sounddevice as sd
import soundfile as sf

# define constants
CHUNKSIZE = 1024           # number of samples to read at a time from audio source
SAMPLE_RATE = 11025        # sample rate of audio source
ZVEI_FREQ_1 = 885.0        # ZVEI-2 tone freq 1 
ZVEI_FREQ_2 = 1750.0       # ZVEI-2 tone freq 2
THRESHOLD = 0.9            # minimum value that needs to be met to consider tone decoded

# variables
freq_bins = int(CHUNKSIZE / 2 + 1)     # bin size to calculate via FFT
freqs = np.fft.rfftfreq(CHUNKSIZE, 1./SAMPLE_RATE)   # array of frequencies for FFT

# initialization
signal_buffer = np.zeros(CHUNKSIZE)      # buffer array for signal processing

# define functions
def callback(indata, outdata, frames, time, status):
    """Callback function for audio processing
    """
    if status:
        print(status)

    # multiply samples with Hann window
    signal_buffer[:] = indata[:,0] * np.hanning(CHUNKSIZE)

    # calculate FFT
    fft = np.fft.rfft(signal_buffer)

    # look for both frequencies (freq bin +-2)
    freq_1_bin = np.argmax(fft[freq_bins + np.argmax(np.abs(fft[:freq_bins])) - 2: freq_bins + np.argmax(np.abs(fft[:freq_bins])) + 3])
    freq_2_bin = np.argmax(fft[freq_bins + np.argmax(np.abs(fft[freq_bins:])) - 2: freq_bins * 2 + 3])

    # calculate fast magnitude of signal