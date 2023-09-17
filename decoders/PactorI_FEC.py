#TODO: Test, verify accuracy of output

import numpy as np

def Pactor_I_FEC_decoder(signal):
    """Decode RF signal using 'Pactor-I FEC' algorithm

    Parameters
    ----------
    signal : numpy array
        An RF signal in the frequency domain

    Returns
    -------
    decoded_signal : numpy array
        The decoded RF signal
    """
    # Process the RF signal using Pactor-I FEC algorithm
    decoded_signal = np.zeros(signal.shape, dtype='int16')
    threshold = 0.3 * np.max(signal) # determine acceptable thresholds
    
    for i in range(len(signal)):
        if signal[i] > threshold:   # corresponding to 1 (value)
            decoded_signal[i] = 1
        elif signal[i] <= -threshold:   # corresponding to 0 (value)
            decoded_signal[i] = 0
        else:
            decoded_signal[i] = 0   # default to 0 for ambiguities

    return decoded_signal