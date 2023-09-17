'''
# TODO: integrate with sigint framework.

# Decoder for CCITT tonal system. Written in Python.

import numpy as np

# Number of samples to decode
samp_count = 512

# Set sample rate here
sampleRate = 44100

# Generate the time vector based on the sample rate
t = np.arange(samp_count) / sampleRate

# Tone frequencies used in the CCITT app
f1 = 1300
f2 = 1700

# Generate the tones
tone_1 = np.sin(np.pi * 2 * f1 * t)
tone_2 = np.sin(np.pi * 2 * f2 * t)

# Create a vector containing the tones
tones = tone_1 + tone_2

# Create a mask with booleans 
# representing the two tones
mask = np.zeros((samp_count), dtype=bool)

# Set the mask to True where the tones are present
mask[np.where(tones == 2)[0]] = True
mask[np.where(tones == -2)[0]] = True

# Create an empty dictionary
data = {}

# Iterate over every sample
for i, sample in enumerate(mask):
    
    # If both tones are present,
    # set the data dictionary at that sample index to True
    if sample:
        data[i] = True

# Return the data
print(data)