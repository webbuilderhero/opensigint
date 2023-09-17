# TODO: Decide which signals to detect
# TODO: Detail the process for decoding the signal

# Necessary libraries
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Define signal parameters and constants
FS = 110 # Sampling rate as specified in the RFSM 110B
Fc = 10000 # Frequency cutoff for the signal as specified in the RFSM 110B

# Set up plotting
plt.grid(True)

# Read input signal from file
time,x = np.loadtxt('08RFsignal.csv', delimiter=',', skiprows=2, unpack=True)

# Plot time domain data
plt.plot(time, x, label='Signal')
plt.xlabel('Time (s)')
plt.legend()

# Construct the low pass filter
b, a = signal.butter(4, Fc, 'low', fs=FS)

# Use filter to filter the signal
output = signal.filtfilt(b, a, x)

# Plot the time domain signal after filtering
plt.plot(time, output, label='Filtered Signal')
plt.xlabel('Time (s)')
plt.legend()

# Calculate the signal decoding using the FIR filter coefficients
# Get the output signal by applying the FIR filter
decodedSignal = np.convolve(x, b)

# Plot decoded signal
plt.plot(time, decodedSignal, label='Decoded Signal')
plt.xlabel('Time (s)')
plt.legend()

# Save the decoded signal to a file
np.savetxt("decodedSignal.csv", decodedSignal, delimiter=",")

# Show all plots
plt.show()