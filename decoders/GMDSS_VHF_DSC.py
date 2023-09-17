# TODO: Set up decoder framework 

import numpy as np
import scipy.signal
import math

# Constants used to decode RF Signals
GMDSS_VHF_DSC_RATE = 9600 # baud rate
GMDSS_VHF_DSC_SAMPLE_RATE = GMDSS_VHF_DSC_RATE * 8 # sample rate
GMDSS_VHF_DSC_PEAK_THRESHOLD = 0.8 # peak threshold used for peak detection

# Create decoder object for GMDSS VHF DSC
class GmdssVhfDs(object):
    def __init__(self, sample_rate):
        self.sample_rate = sample_rate # Sample rate of the samples passed to the decoder

    def decode(self, samples):
        # Resample the input samples to GMDSS_VHF_DSC_SAMPLE_RATE
        resampled_samples = scipy.signal.resample(samples, int(np.ceil(len(samples)*self.sample_rate/GMDSS_VHF_DSC_SAMPLE_RATE)))

        # Find peaks in resampled samples
        peaks = self._find_peaks(resampled_samples, GMDSS_VHF_DSC_SAMPLE_RATE, GMDSS_VHF_DSC_PEAK_THRESHOLD)

        # Find peaks in signal
        self.peaks = self._find_peaks(resampled_samples, GMDSS_VHF_DSC_PEAK_THRESHOLD)

        # Decode peaks
        decoded_binary = self._decode_peaks(self.peaks)

        # Return decoded bits
        return decoded_binary


    def _find_peaks(self, samples, sample_rate, peak_threshold):
        '''Find peaks in a signal by looking for zero crossings in a full-wave rectified version of the signal
        
        Arguments:
            samples {list} -- The signal data
            sample_rate {int} -- Sample rate of