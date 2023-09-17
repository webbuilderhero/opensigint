#TODO: Figure out frequency bands for ChVK-W

import re

def decode_signal(signal):
  bands = []
  #Regular expression to identify the format of the signal
  regex = re.compile("^([A-Z][A-Z|0-9]{2})-([A-Z][A-Z]?)$")

  #Check if signal follows correct format 
  matches = regex.match(signal)
  if matches == None:
    return
  
  #Get the Frequency Bands from the matches
  bands.append(matches.group(1))
  bands.append(matches.group(2))

  #Decode the signal 
  if bands[0] == "ChVK":
    if bands[1] == "W":
      #TODO: Add algorithm to decode signals for ChVK-W Frequency Band
      print("Signal decoded for ChVK-W frequency band")
    
  return 

#Testing decoder 
decode_signal("ChVK-W") #Output : Signal decoded for ChVK-W frequency band