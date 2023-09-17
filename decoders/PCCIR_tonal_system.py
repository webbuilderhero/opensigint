"""Decoder for PCCIR tonal system."""

# TODO: Get algorithm for decoding PCCIR system

def decode_PCCIR(signal):
    """
    Decode the PCCIR tonal system of the given signal.

    Parameters
    ----------
    signal : array_like
        The signal to decode.
        
    Returns
    -------
    decoded_signal : array_like
        The decoded signal.
    """
    # Get the length of the signal
    N = len(signal)
    
    # Initialize the decoded_signal
    decoded_signal = [0]*N
    
    # TODO: Replace with appropriate algorithm
    # Naive approach of taking the average amplitude
    for n in range(N):
        decoded_signal[n] = sum(signal[n:n+3])/3
        
    return decoded_signal