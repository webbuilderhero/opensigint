#TODO: COMMENT ON CODE BELOW

### DECODER CODE for BPSK-124F FEC ###

import numpy as np

# import libraries needed for signal processing and graphical display
import matplotlib.pyplot as plt
from scipy import signal

# Variable to store signal from the RF Signal Intelligence framework
rawdata = np.array([])


def bpsk_decode(rawdata):
    """Decode BPSK with soft-decision decoding (FEC).
    Args:
        rawdata: RF signal from framework
    """

    # filter the signal
    filt_sig = signal.lfilter(b=[1], a=[1], x=rawdata)
   
    # Conjugate the signal and detect symbols by comparing to a threshold
    conj_filt_sig = np.conjugate(filt_sig)
    detected_symbols = np.where(conj_filt_sig > 0, 1, 0)
   
    # decode the symbols using FEC
    decoded_message = ""
    for i in range(0, len(detected_symbols), 7):
        codeword = [detected_symbols[i], detected_symbols[i+1], detected_symbols[i+2], detected_symbols[i+3], detected_symbols[i+4], detected_symbols[i+5], detected_symbols[i+6]]
            
        # determine which binary-valued sequence was sent
        errors = 0
        for x in range(0, 7):
            if codeword[x] != 0 and codeword[x] != 1:
                errors += 1
        if errors == 0:
            if codeword == [0, 0, 0, 0, 0, 0, 0]:
                decoded_message += 'A'
            elif codeword == [0, 0, 0, 0, 0, 0, 1]:
                decoded_message += 'B'
            elif codeword == [0, 0, 0, 0, 0, 1, 0]: