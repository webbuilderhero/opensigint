# Sigint Decoding - Coquelet Mk2
# TODO: finish filling in the decoding logic 

# Needed imports
import numpy as np 
import scipy.signal as sig

# This is class handles decoding of
# Coquelet Mk2 RF signals
class CoqueletMk2Decoder:

  def __init__(self):
    self.name = 'CoqueletMk2-I'

  # Start the decoding process
  # input: raw signal data
  # output: decoded signal data 
  def decode(self, data):

    # Step 1: Apply a low-pass filter to the signal data
    filtered_data = sig.lfilter(data)

    # Step 2: Calculate the FFT of the signal
    fft_data = np.fft.rfft(filtered_data)

    # Step 3: Apply the channel filter
    channel_data = self.apply_channel_filter(fft_data)

    # Step 4: Perform de-mapping of the signal
    decoded_signal = self.apply_demapping(channel_data)

    return decoded_signal


  # Channel filter - Coquelet Mk2
  # input: fft data
  # output: filtered fft data
  def apply_channel_filter(self, fft_data):
    # TODO: Implement the channel filter

    return filtered_data

  # De-mapping - Coquelet Mk2
  # input: channel data
  # output: decoded signal
  def apply_demapping(self, channel_data):
    # TODO: Implement the de-mapping logic

    return decoded_signal