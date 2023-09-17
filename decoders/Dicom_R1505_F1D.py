# TODO: Fill in necessary imports 
import scipy.signal as signal
import numpy as np

# This decoder is designed to decode Dicom R-1505 F1D signals
def decode(signalData):
    # First, parse signalData array into I and Q components
    I_data = signalData[:, 0]
    Q_data = signalData[:, 1]
    
    # Upsample from 2x to 8x
    upsampled_I = signal.resample(I_data, 8 * len(I_data))
    upsampled_Q = signal.resample(Q_data, 8 * len(Q_data))
    
    # Filter I and Q components using a BPF
    f1 = 0.2 # lower cutoff frequency
    f2 = 0.3 # upper cutoff frequency
    b, a = signal.butter(4, ([f1, f2]/0.5), 'bandpass') # 4th order butterworth BPF
    filtered_I = signal.filtfilt(b, a, upsampled_I)
    filtered_Q = signal.filtfilt(b, a, upsampled_Q)
    
    # Downsample the signal back to 2x
    downsampled_I = signal.resample(filtered_I, len(I_data))
    downsampled_Q = signal.resample(filtered_Q, len(Q_data))

    # Return decoded signal
    return np.array([downsampled_I, downsampled_Q])