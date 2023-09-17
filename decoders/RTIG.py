#TODO - Work on RF signal intelligence

#Decoder for RTIG

#Function to decode RTIG
def decodeRTIG(data):
  #Check if valid input
  if type(data) != str:
    raise ValueError("Data is not in string format")

  #Split data into chunks
  chunks = data.split()

  #Check if valid amount of chunks
  if len(chunks) != 5:
    raise ValueError("Incorrect number of chunks")
    
  # Create empty dictionary for decoding
  decodedData = {}

  #Decode each chunk
  decodedData["position"] = chunks[0]
  decodedData["origin"] = chunks[1]
  decodedData["ident"] = chunks[2]
  decodedData["velocity"] = float(chunks[3])
  decodedData["heading"] = float(chunks[4])

  return decodedData

#Run decodeRTIG
decoderOutput = decodeRTIG("41 31.01N 78 41.17W VRBS 523 025")

#Print Output
print(decoderOutput)