# TODO: Figure out how to integrate this script into the framework

import numpy as np
from scipy import signal

# Sampling rate
fs = 4800 # Hz

# Modulation
fb = 1200 # Hz
PhaseDegree = 180 # Degrees

# Define a BPSK signal
# Set phase shift
PhaseShift = PhaseDegree*np.pi/180 

# Generate a BPSK signal
T = 2*np.pi/fb; 
t = np.arange(0,T, 1/fs)
s = np.cos(2*np.pi*fb*t + PhaseShift)

# Form the demodulation matrix
M1 = np.cos(2*np.pi*fb*t)
M2 = np.sin(2*np.pi*fb*t)

M = np.vstack((M1,M2))

# Get the original message
measurement = np.dot(M.T,s)

# Filter the received signal
# TODO: Determine optimal filter settings
b,a = signal.butter(5, 0.1, 'lowpass')
measurement = signal.lfilter(b,a,measurement)

# Extract symbol from received signal
msgSymbol = np.zeros(measurement.shape)
msgSymbol[measurement > 0] = 1

# Output decoded message
msg = ''.join([str(int(x)) for x in msgSymbol])

print('Decoded message: ' + msg)