# TODO: Further research to determine the exact characteristics of the NATEL tonal mode

import numpy as np
import scipy.signal as sp

def decode_NATEL_tonal_mode(rf_data):
    """
    This function decodes the NATEL tonal mode scrample in a given RF data signal

    Parameters
    ----------
    rf_data : 1D np.float array
        the RF data signal

    Returns
    -------
    decoded_signal: 1D np.float array
        the decoded signal
    """
     
    #Step 1: Performbandpass filtering
    b, a = sp.butter(5, [310/4000., 990/4000.], btype='bandpass', analog=False)
    filtered_signal = sp.filtfilt(b, a, rf_data)
    
    # Step 2: Downsample and Rectify the filtered signal
    downsampled_sig = filtered_signal[::4] # Downsample by 4
    dec_sig = np.absolute(downsampled_sig) # Rectify 
    
    # Step 3: Perform Lowpass filtering
    b, a = sp.butter(2, 0.4)
    decoded_signal = sp.filtfilt(b, a, dec_sig)
    
    return decoded_signal