# TODO: Further decode the meaning of the signal

# Import necessary libraries
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Create signal
fs = 1000 # Sample rate
N = 1000 # Number of sample points
T = 1.0/fs # Sample spacing
t = np.linspace(0, N*T, N) # Time vector
x = np.sin(50.0 * 2.0*np.pi*t) + 0.5*np.sin(80.0 * 2.0*np.pi*t)

# Generating the frequency spectrum using FFT
X = np.fft.fft(x, N) # Perform FFT
X_mag = np.abs(X) # Get the magnitude of the FFT
X_angle = np.angle(X) # Get the phase of the FFT
f = np.linspace(0.0, 1.0/(2.0*T), N/2) # Frequency vector

# Plot the signal and the FFT
plt.subplot(211)
plt.plot(t, x)

plt.subplot(212)
plt.plot(f, 2.0/N * X_mag[:N//2])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.show()

# Decode T-206 2MT WESNA
TD = {'T': 'Thuraya', 
      '2MT': 'Two-Way Messaging Terminal', 
      'WESNA': 'Wide-Area and Enhanced Secure Network Accessibility'
     }

# Print out the decoded results
print("T-206: {}".format(TD['T']))
print("2MT: {}".format(TD['2MT']))
print("WESNA: {}".format(TD['WESNA']))