# TODO: Unclear what input/output is expected  

def decodeM823DifferentialGPS(receivedMessage):
    """
    Decodes a M823 GPS differential message. 
    
    Parameters: 
        receivedMessage (string): the raw hex message received 
    
    Returns: 
        decodedMessage (dict): a dictionary with keys corresponding to each field and the values being the decoded values for each field 
    """
    
    # decode a 6 byte message 
    # convert from hexidecimal to binary 
    receivedBinary = ''.join(format(s, '08b') for s in bytearray.fromhex(receivedMessage))
    
    # bundle into dictionary 
    decodedMessage = {
        "id": receivedBinary[0:4], 
        "data": receivedBinary[4:6],
        "message": receivedBinary[6:32],
        "error-check": receivedBinary[32:]
    }
        
    # return the decoded message
    return decodedMessage