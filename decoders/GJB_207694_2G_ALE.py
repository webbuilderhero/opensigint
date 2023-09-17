"""Sigint Decoder for GJB 2076-94 2G ALE"""
# TODO: Fill in any missing analysis or data analysis

# Imports
import numpy as np
import pandas as pd

# Signal data
input_signal = [
    [-3dB, -2.5dB, -2dB, -2dB, -2.2dB], # invert 0
    [-1.5dB, -1.5dB, -1.5dB, -1.5dB, -1.5dB], # invert 1
    [-2.0dB, -2.2dB, -2.3dB, -2.4dB, -2.5dB], # invert2
    [-3dB, -2.5dB, -2.0dB, -2.0dB, -2.1dB], # invert 3
    [-1.5dB, -1.8dB, -1.8dB, -1.8dB, -1.9dB], # no invert
    [-2.0dB, -2.0dB, -2.2dB, -2.2dB, -2.3dB], # no invert
    [-3dB, -2.2dB, -2dB, -2.2dB, -2.2dB], # invert 0
    [-1.5dB, -1.5dB, -1.5dB, -1.5dB, -1.5dB], #invert 1
    [-2.0dB, -2.0dB, -2.2dB, -2.2dB, -2.2dB], # no invert
    [-3dB, -2.5dB, -2.5dB, -2.5dB, -2.5dB]  #invert 2
]
# Dictionary of signal patterns and corresponding bits
pattern_dict = {
    [-3dB, -2.5dB, -2dB, -2dB, -2.2dB]: [0, 1], #invert0
    [-1.5dB, -1.5dB, -1.5dB, -1.5dB, -1.5dB]: [0, 0], #invert