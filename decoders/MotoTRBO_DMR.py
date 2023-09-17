# TODO: Have way to identify start/stop of audio signal

import wave
import numpy as np

# define constants
MOTOTRBO_DMR_FREQ = 439.9875 

def decode_mototrbo_dmr(audio_file):
    """
   This function decodes MotoTRBO radio DMR audio files
    Args:
        audio_file (str): Audio file (.wav) to decode
    Returns:
        decoded_data (str): Decoded data from audio file
    """

    # read audio file
    audio_data = wave.open(audio_file, 'rb')

    # get sampling rate and samples per frame
    sampling_rate = audio_data.getframerate()
    samples_per_frame = audio_data.getnframes()

    # get audio frames and convert to numpy array
    audio_frames = np.fromstring(audio_data.readframes(samples_per_frame), 'Int16')
    audio_frames_np = np.array(audio_frames)

    # get original number of samples
    num_samples = audio_frames_np.shape[0]
    
    # check if frequency is valid
    if (MOTOTRBO_DMR_FREQ < (sampling_rate / num_samples) or (MOTOTRBO_DMR_FREQ > (sampling_rate / 2))):
        # frequency is not valid
        return None
    
    # FFT
    spectrum = np.fft.fft(audio_frames_np)

    # get index of peak frequency
    peak_freq_index = np.argmax(spectrum)

    # get decoded data from peak frequency  
    peak_freq_bin = peak_freq_index * (sampling_rate / num_samples)
    decoded_data = peak_freq_bin / MOTOTRBO_DMR_FREQ

    return decoded_data