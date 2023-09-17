#TODO: Adjust formatting 

# Decoder for COSMOS
def Cosmos_Decoder(signal): 
  """ 
  Takes a signal (as a list of integers) and returns a decoded message from COSMOS. 
  """
  
  # Dictionary to store alphabet 
  ALPHABET = {0: 'C', 1: 'O', 2: 'S', 3: 'M', 4: 'A'}

  # Empty string to store decoded message 
  decoded_msg = ''

  for num in signal: 
    try: 
      # Get the character for the current number 
      decoded_msg += ALPHABET[num]
    except KeyError: 
      # If the key doesn't exist in the dictionary, return an error 
      return 'Error: Invalid character in signal'

  return decoded_msg