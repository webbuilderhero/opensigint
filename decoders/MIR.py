# TODO: Need to add logic to see if signal decoded properly

def decode_MIR(signal):
    """ 
    This function takes in an RF signal and decodes it 
    to determine the MIR identity information

    Parameters
    ----------
    signal: array
            The signal to decode

    Returns
    -------
    decoded_signal: dict
            The decoded signal including MIR information
    """
    # Initialize empty output
    decoded_signal = {}
    
    # TODO: Get information from signal to decode for MIR

    # Decode the MIR from signal
    decoded_signal['MIR_identity'] = decodeMIRfromSignal(signal)

    return decoded_signal

def decodeMIRfromSignal(signal):
    """ 
    This function takes in an RF signal and decodes it 
    to determine the MIR identity information

    Parameters
    ----------
    signal: array
            The signal to decode

    Returns
    -------
    mir_id: string
            The MIR identity
    """
    # Initialize empty output
    mir_id = ""
    
    # TODO: Decode the MIR from signal and store in mir_id

    return mir_id