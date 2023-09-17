# TODO: determine what "Gray Scale" means in this context

# !/usr/bin/env python

"""
This script contains a decoder for Facsimile FAX B&W signals for SIGINT purposes.
"""

import numpy as np
import pandas as pd
from scipy.signal import hilbert

def facsimile_decoder(data):
    """
    This function decodes facsimile data for RF signal processing.
 
    Parameters
    ----------
    data : numpy.ndarray
        The data to be decoded.

    Returns
    -------
    pandas.DataFrame
        The decoded signal as a DataFrame.
    """

    # Calculate Hilbert transform of the data
    h = hilbert(data)

    # Extract features and store in a DataFrame
    N = len(data)
    df = pd.DataFrame({
        'inst_freq': np.abs(np.diff(np.angle(h[:N-1]))/(2*np.pi)),
        'inst_amp': pd.Series(np.absolute(h[:N-1])),
        'gray_scale': pd.Series(np.absolute(h[:N-1])) #TODO: need to determine what "Gray Scale" impact is
    })

    return df