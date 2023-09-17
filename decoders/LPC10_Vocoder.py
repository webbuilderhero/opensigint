#TODO: Verify the decode script
 
import wave
import numpy as np
from scipy.fftpack import dct
 
def lpc_decoder(signal):
 
    # get samplerate
    samplerate = wave.open(signal).getframerate()
 
    # get signal 
    signal = np.array(wave.open(signal).readframes(-1), dtype=np.int16)
 
    # get number of samples
    samples = len(signal)
 
    # create window
    window_size = Int(0.02 * samplerate)
    window = np.ones(window_size)
 
    # get length of each frame based on a 10ms frame size
    frame_length = Int(0.01 * samplerate)
 
    # create an empty list to store the frames
    frames = []
 
    for i in range(0, samples, frame_length):
        frame = signal[i:i+frame_length] # extract frame
        framed_data = frame * window # multiply frame with window
        findex = int(i/frame_length) # frame index
        frames.append(framed_data)
 
    # use DCT to get log spectral
    log_spectral = dct(frames, axis=1, norm='ortho')
 
    # reconstruct signal using LPC
    recon_signal = np.zeros(samples)
    iter_num = 0
 
    # loop from 0 to number of frames
    while (iter_num < len(frames)):
        frame_length = len(frames[iter_num])
        frame_length_2 = int(frame_length/2)
 
        # get auto correlation array
        auto_corr_array = np.correlate(frames[iter_num], frames[iter_num], mode='full')
 
        # get the part of it that we need
        auto_corr_array = auto_corr_array[len(auto_corr_array) - frame_length_2:]
 
        # solve