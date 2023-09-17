#TODO: research NexREF and determine proper decoder variables

import math

#NexREF Decoder
def NexRefDecode(input_text):
    
    #Split the input string on spaces
    nexref_split = input_text.split(" ")
    
    #Verify there is an even number of entries
    if len(nexref_split) % 2 != 0:
        return False
    
    #Verify at least 2 entries
    if len(nexref_split) < 2:
        return False
    
    #Parse out the coordinates, frequency, and password
    coords = []
    freq = None
    pwd = None
    for i in range(len(nexref_split)):
        if i % 2 == 0:
            coords.append(int(nexref_split[i]))
        elif i == len(nexref_split) - 2:
            freq = int(nexref_split[i])
        else:
            pwd = nexref_split[i]
            
    #Calculate the signal range
    signal_range = calculate_range(coords)
    
    #Return the decoded values
    return {
        "coordinates": coords,
        "frequency": freq,
        "password": pwd,
        "signal_range": signal_range
    }

#Calculate the signal range for given coordinates
# Formula:
#   d = Sqrt( x2 - x1 + y2 - y1 )
def calculate_range(coords):
    x1 = coords[0]
    x2 = coords[2]
    y1 = coords[1]
    y2 = coords[3]
    
    d = math.sqrt( math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    
    return d