"""A Decoding Script for Sigint RF-41A00 ALE"""

#TODO: Plug the script into the framework


import bitarray  # needed to manipulate the signals

# This class will host all the necessary decoding functions for the ALE signal
class Decoder():
    
    # This is an init function to store information when an instance of the class is created
    def __init__(self, signal):
        self.signal = signal
        
    # This will decode the ALE signal
    def decode_ALE(self):
        
        # We'll use this empty list to store the BWAM and SEL signals
        decoded_signal = []
        
        # We'll use bitarray to turn the signal into an array of bits
        signal_bits = bitarray.bitarray(self.signal)
        
        # Next, we'll split the signal into 16 bit pieces, one for BWAM and one for SEL
        bwam_signal = signal_bits[0:16]
        sel_signal = signal_bits[16:32]
        
        # Finally, we'll push the decoded signals into the list
        decoded_signal.append(bwam_signal)
        decoded_signal.append(sel_signal)
        
        # Return the decoded signal
        return decoded_signal