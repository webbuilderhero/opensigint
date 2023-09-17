# TODO: Get more detailed specs and double check this works for Mil-Std 188-141B 3G ALE BW0-BW5

# Import relevant libraries
import numpy as np
import scipy.signal as signal

# Define constants
BW0 = 12.5 
BW1 = 25
BW2 = 50
BW3 = 100
BW4 = 200
BW5 = 400

# Define the decoder function
def mil_std_188_141b_3g_ale_bw_decoder(data, sample_rate):
    """Decodes Mil-Std 188-141B 3G ALE BW0, BW1, BW2, BW3, BW4, and BW5 data. 
    
    Args:
        data (numpy array): The data to be decoded.
        sample_rate (float): The sample rate of the data (in Hz). 
    
    Returns:
        The decoded data (as a list of complex numbers).
    """ 
    
    # Create filter banks based on the bandwidth of the desired signal
    f_low = np.array([-BW0/2, -BW1/2, -BW2/2, -BW3/2, -BW4/2, -BW5/2, 0])
    f_high = np.array([BW0/2, BW1/2, BW2/2, BW3/2, BW4/2, BW5/2, sample_rate/2])
    bw_filters = signal.firwin2(numtaps=200, cutoff=[f_low,f_high], window=['blackman', 'blackman'], nyq=sample_rate/2)
    
    # Apply filter banks
    decoded_data = []
    for i in range(len(bw_filters)):
        filtered_data = signal.lfilter(bw_filters[i, :], 1.0, data)
        decoded_data.append(filtered_data)
    
    return decoded_data