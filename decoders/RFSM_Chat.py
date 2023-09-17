import re

#TODO: Figure out if there is a specific protocol we need to monitor for the RFSM chat 

def decode_rfs_chat(data):
    """This function decodes the RFSM chat protocol for use in sigint.
     
    Parameters
    ----------
    data: str
        The data stream to be decoded. 
    
    Returns
    -------
    messages (list)
        A list of decoded messages
    """
    
    messages = []
    data_lines = data.splitlines()  # Split data into separate lines

    for line in data_lines:
        # Look for the RFSM chat message type identifier
        if re.match(r'^\[ETX\] RFSM_CHAT', line):
            message = line.split(' ', 3)[3]  # Split line to get the message after the identifier 
            messages.append(message)
    
    return messages