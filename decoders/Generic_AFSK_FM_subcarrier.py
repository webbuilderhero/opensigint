import numpy as np  
import scipy.signal.signaltools as sg
import scipy.signal

class GenericAFSKDecoder:

    def __init__(self, sample_rate):
        """
        Create a new decoder.

        sample_rate : The rate in which the sample was acquired in Hz.
        """
        self.sample_rate = sample_rate

    def decode(self, samples):
        """
        Decode the AFSK modulated sample

        samples : The sample
        returns : The decoded bitstream, bandwith [kHz]
        """
        # Bandwidth calculation from signal energy in frequency domain 
        freq_domain_samples = np.fft.fft(samples)
        freq_energy = np.square(np.abs(freq_domain_samples))
        energy_sum = np.sum(freq_energy)
        bandwidth = energy_sum/len(freq_energy)

        # Demodulation using envelope detector
        samples_filtered = sg.lfilter([1,0.9], 1, samples)
        samples_enveloped = sg.hilbert(samples_filtered)
        bitstream = samples_enveloped > 0

        return bitstream, bandwidth