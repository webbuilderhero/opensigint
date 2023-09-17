#TODO: Ensure framework compatability

#Decoder for TADIL-B

"""
TADIL-B (aka Link-16) is an RF signal intelligence protocol that allows for real-time exchange of tactical data.
"""

import re

# Dictionary storing values for various messages
message_dict = {
  # text - message ID
  "Emergency - Very Urgent Message" : 1230,
  "All Stations" : 1231,
  "Request Operational Readiness Level" : 1208,
  "Report Operational Readiness Level" : 1209,
  "Request Friend or Foe Status" : 1232,
  "Report Friend or Foe Status" : 1233
}


def decode_message(message: str) -> int:
  """
  Decodes a TADIL-B formatted message and returns the message ID
  
  Parameters:
    message (str) : String representing a TADIL-B formatted message
  
  Returns:
    int : Message ID if found, else 0
  """
  
  # Strip out illegal TADIL-B characters
  message = re.sub(r'[^\w\s]', '', message)
  
  # Check if the message is in the message dictionary
  if message in message_dict.keys():
    return message_dict[message]

  return 0