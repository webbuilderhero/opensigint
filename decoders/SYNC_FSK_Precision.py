#TODO: Research synchronization

#Import libraries
import numpy as np
from scipy import signal

#Create class
class SyncFSKPrecission:

    def __init__(self, wavedata):
        self.wavedata = wavedata
        self.bit_interval = 0            # interval between each bit 
        self.bits_per_symbol = 0         # number of bits per symbol 
        self.preamble_bits = None        # list of bits in preamble 
    
    #Define synchronization function
    def synchronize(self):
        preamble = [1, 0, 1, 0, 1, 0, 1] # define preamble sequence 
        diffs = np.diff(preamble)

        # find the period between bits by searching for the preamble 
        correlations = signal.correlate(self.wavedata, diffs)
        self.bit_interval = np.argmax(correlations) 

        #find the number of signatures per symbol by searching through all 
        # possible combinations from 1 to 10 bits 
        for self.bits_per_symbol in range(1,11):
            correlations = signal.correlate(self.wavedata, preamble)
            self.preamble_bits = correlations[self.bit_interval*self.bits_per_symbol] > 0
            if self.preamble_bits == preamble: 
                break 
            else:
                self.preamble_bits = None
                
    #Define main decoding algorithm 
    def decode(self):
        
        # synchronize to preamble 
        self.synchronize()
        
        # start decoding from end of preamble 
        startpoint = self.bit_interval*self.bits_per_symbol 
        result = '' 
        
        # iterate through waveform and step by bit_interval 
        for b in range(int(len(self.wavedata) - startpoint) // self.bit_interval): 
            # get symbol values 
            symbol_values