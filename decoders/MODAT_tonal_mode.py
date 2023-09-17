# TODO: Need to figure out how to properly measure amplitude/strength of frequency bands

# Imports
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

# Decoder for MODAT tonal mode
def modat_decoder(sig):
    ''' 
    Decoder for MODAT tonal mode
    args:
        sig - Input signal to decode
    returns:
        decoded message
    '''
    # Create frequency bands
    fmin, fmax = np.percentile([1e2, 5e3], np.arange(0, 100+1))
    freqs = np.linspace(fmin, fmax, 21)
    bs = scipy.signal.firwin2(1024, freqs, window='hanning')
    
    # Filter signal by frequency bands
    vs = np.abs(scipy.signal.lfilter(bs, 1, sig))
    vs = np.sum(vs, axis=0)
    
    # Measure amplitude/strength of frequency bands and decode accordingly
    indices = np.arange(0, len(freqs), 2) # Even indices for amplitude
    msg = []
    for idx in indices:
        if vs[idx] > vs[idx+1]:
            msg.append(1)
        else:
            msg.append(0)
        
    # Convert to message
    return ''.join(map(str, msg))

# Test
sig = np.random.normal(0, 1, 1024)
msg = modat_decoder(sig)
print(msg)