"""
Decoder for IVSU signal
"""

# TO DO:
#  Still need to program the decoder logic

def ivsu_decoder(length, data):
    """Function to decode IVSU signal
    
    Parameters
    ----------
    length : int
        Length of the signal
    data : str
        Data to be decoded
    
    Returns
    -------
    ivsu_result : str
        Result of decoded signal
    """
    # Initialize output result
    ivsu_result = ""
    
    # Decode the signal using decoder logic
    for i in range(length):
        # Do some logic here to decode the signal
        ivsu_result += "decoded data"
        
    # Return decoded result
    return ivsu_result