# TODO: Determine appropriate radio frequency for decoding
 
# Python 3.x script to decode ASYNC FSK 
# signals for RF signal intelligence

#import necessary packages
import radio
import numpy as np
import pandas as pd

#load the FSK radio library
radio = radio.loadLibrary('fsk')

# Define the parameters used to decode the signal
FSK_MODEM_PARMS = {
  'fsk_symbol_rate': 1000,           # Baudrate in symbols/second
  'fsk_freq_dev': 50,               # Frequency deviation (in Hz)
  'fsk_stop_bits': 1,               # 1 or 2
  'fsk_use_biphase': False,         # True or False
  'fsk_data_rate': 4000,            # Bits per second
  'fsk_scramble': True              # True or False
}

#create a new decoder using the defined parameters
decoder = radio.Decoder(FSK_MODEM_PARMS)

# Define the signal processing parameters
SIGNAL_PROCESSING_PARMS = {
    'sample_rate': 50000,
    'max_samples_per_frame': 4096
  }

#create a signal processor with the defined parameters
signal_processor = radio.SignalProcessor(SIGNAL_PROCESSING_PARMS)


#main function to decode incoming radio signals
def decode_radio_signal(radio_signal):
    #process the signal
    processed_signal = signal_processor.process(radio_signal)

    #decode the signal
    decoded_signal = decoder.decode(processed_signal)
 
    #return the decoded signal
    return decoded_signal