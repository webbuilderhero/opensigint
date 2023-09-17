# TODO: Test script and plug into framework

# Declare necessary library
import numpy as np

# Define Auriga Decoder
def decode_auriga(data):
    '''
    Decoder for Auriga signal intelligence datastreams
    
    Parameters
    ----------
    data : array_like
        Data to be decoded
        
    Returns
    -------
    data_decoded : array_like
        Data decoded by Auriga
    '''
    
    # Perform data decoding
    data_decoded = np.array([i+1 for i in data])
    
    return data_decoded