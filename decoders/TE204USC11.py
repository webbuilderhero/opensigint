#TODO: Research different ways of decoding symbols in TE-204/USC-11

#import all necessary libraries 
import numpy as np
from scipy import signal 

# Define signals 
sig = signal.dlti([], [1,1], 1)

#Define signal parameters 
fs = 44100

#load data 
x, t, rx = signal.dlti(sig, t=[0, 1], fs=fs)

# Convert symbols into bits 
bits = []
for sample in rx:
    if sample > 0:
       bits.append(1) 
    else: 
       bits.append(0)

# Group bits into bytes 
bytes = []
byte = []
for b in bits:
    byte.append(b)
    if len(byte) == 8:
        bytes.append(byte)
        byte = []

# Convert bits to ASCII characters 
decoded_data = ""
for b in bytes:
    decoded_data += chr(int("".join(str(x) for x in b),2))
 
# Output decoded data 
print(decoded_data)