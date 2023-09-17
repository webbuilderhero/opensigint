""" 
Decoder for Mil.Std 188-110B App C - RF signal intelligence

TODO: 
1. Find a way to determine bit rate of signal 
2. Research App C for further details

"""

import numpy as np 
import matplotlib.pyplot as plt 

# get signal from user 
signal = input('Please enter a signal to decode: ')

# compute bit rate 
FRAME_LENGTH = 3200  # frame length is known to be 3200 bits  
bits_per_frame = len(signal)/FRAME_LENGTH 

# check the signal length 
if bits_per_frame != int(bits_per_frame):
    raise ValueError("Length of input signal does not match frame size specified in App C")

# convert signal to an array of 0's and 1's 
signal_arr = np.array([int(x) for x in list(signal)])

# Plot signal 
x_axis = np.arange(len(signal_arr))
plt.plot(x_axis, signal_arr)
plt.title("Signal Graph")
plt.xlabel("Bit Number")
plt.ylabel("Bits")
plt.show()

# Create empty array to store decoded signal 
decoded_signal = np.zeros(int(FRAME_LENGTH/bits_per_frame))

# Decode signal
for i in range(0, len(signal_arr), int(bits_per_frame)):
    group = signal_arr[i : i+int(bits_per_frame)]
    s = 0 
    for j in range(1, len(group)+1):
        s += group[j-1] * (2**(bits_per_frame-j))
    decoded_signal[int(i/bits_per_frame)] = s

# Plot decoded signal 
x_axis2 = np.arange(len(decoded_signal))
plt.plot(x_axis, decoded_signal)
plt.title("Dec