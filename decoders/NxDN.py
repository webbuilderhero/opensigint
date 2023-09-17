#TODO: Decide what type of input the decoder will take (i.e. streamed audio or raw data)
#TODO: research the modulation schemes for NxDN

import numpy as np
import scipy.signal as sig
from enum import Enum

#Enum for keeping track of modulation/demodulation states
class State(Enum):
    DEMODULATION = 1
    MODULATION = 2

#The NxDN Decoder
#Takes raw data or streamed audio as input
class NxDNDecoder:
    def __init__(self, data, state=State.DEMODULATION):
        self.data = data
        self.state = state

    #Function for performing NxDN demodulation
    def demodulate(self):
        #Define modulated parameters
        mod_freq = 12.5e3 #The NxDN modulation signal frequency
        baud_rate = 4800 #The NxDN data rate
        fc = mod_freq #The NxDN carrier frequency
        fs = baud_rate*2 #The audio sampling frequency
        #Define filter parameters
        b,a = sig.butter(4,2*mod_freq/fs,'lowpass') #Define 2nd order low-pass Butterworth filter
        #Pass modulated signal through low-pass filter
        demodulated_signal = sig.filtfilt(b,a,self.data)
        #Return demodulated signal
        return demodulated_signal

    #Function to convert demodulated signal into digital data
    def decode(self):
        #Check if signal is already demodulated
        if self.state != State.DEMODULATION:
            #not demodulated - call demodulate() function
            self.data = self.demodulate()
            #set state to DEMODULATION
            self.state = State.DEMODULATION
        #Calculate sampling frequency
        baud_rate = 4800 #The NxDN data rate
        fs = baud_rate*2 #The audio sampling frequency
        #Calculate bit duration