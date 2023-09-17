"""
Decoder for Necode 322ARX Selcall

TODO:
  - add code to account for multiple necodes being transmitted
  - figure out how to decode Necode 322ARX and get data from it
  - fill in the decode() function with instructions for decoding the selcall

"""

import sigint_framework

def decode(data):
  """Decodes the Necode 322ARX Selcall Data

  Parameters:
        data (array): Array of stream data which contains the Selcall data

  Returns:
        decoded_selcall (array): Array containing decoded Selcall data
  
  """
  # Initialize decoded_selcall array
  decoded_selcall = []

  # Iterate through the array and extract each character
  for element in data:
    # Necode 322ARX Selcall uses 4-bit data
    # Bits 0-3 = Necode character, Bits 4-7 = parity bit 
    nec_char = element & 0x0F
    parity_bit = (element & 0xF0) >> 4
    
    # TODO: check if parity bit is valid using parity check algorithm
    # TODO: if valid, add valid character to decoded_selcall array
  
  return decoded_selcall

# Register decode() function to framework
sigint_framework.register_decode_function(decode)