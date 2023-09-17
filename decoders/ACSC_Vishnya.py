# TODO: determine main functionality of Decoder


""" 
The ACS-C Vishnya is a decoder designed for RF signal intelligence. It is intended to help users decode, organize and analyze signal data.
"""

import numpy as np
from scipy.io.wavfile import read

def decodeSignal(signal):
  """ Decodes a signal data array
  
  Args:
    signal (numpy array): A signal data array
    
  Returns:
    dict: Decoded signal information
  """
  
  # TODO: Add actual decoding logic
  
  # Read array as a wave file
  signal = read(signal)
  
  # Initialize decoded signal data
  decoded_signal = {"sample_rate": signal[0],
                    "num_frames": signal[1].shape[0],
                    "bit_depth": signal[1].dtype.itemsize * 8,
                    "data": signal[1]
                    }
  
  return decoded_signal


def organizeSignal(decoded_signal):
  """ Organizes a decoded signal data array
  
  Args:
    decoded_signal (dict): Decoded signal information
    
  Returns:
    list: Organized signal data
  """
  
  # TODO: Add actual organization logic
  
  # Call the decoded_signal data
  sample_rate = decoded_signal['sample_rate']
  num_frames = decoded_signal['num_frames']
  bit_depth = decoded_signal['bit_depth']
  data = decoded_signal['data']
  
  # Initialize organized signal data
  organized_signal = []
  
  # Organize the signal data by inserting into signal list of arrays
  for frame in range(num_frames):
    organized_signal.append(data[frame])
  
  return organized_signal


def analyzeSignal(organized_signal):
  """ Analyzes organized signal data
  
  Args:
    organized_signal (list): Organized signal data
    
  Returns: