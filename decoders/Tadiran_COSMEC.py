# TODO: Research Takiran COSMEC to figure out what decoders need to be programmed

# Declare necessary variables for TAKIRAN COSMEC decoder

N1 = 0
N2 = 0
N3 = 0

def decrypt_message(encoded_message):
  decrypted_message = ""
  for character in encoded_message:
    if character == 'A' or character == 'B' or character == 'C': # Check if character is one of ABABCABC scheme
      if N1 < N2: # Decrypt the character according to the scheme
        decrypted_char = chr(ord(character)+N3) 
      else:
        decrypted_char = chr(ord(character)-N3)
      decrypted_message += decrypted_char
      N1 = (N1 + 1) % 2
      N2 = (N2 + 1) % 3
      N3 = (N3 + 1) % 26
    else:
      decrypted_message += character # If character is not one of ABABCABC scheme, just copy it as it is.

  return decrypted_message # Return the decrypted message

# Plugin this function to the framework
def decrypt_tadiran_cosmec(encoded_message):
   return decrypt_message(encoded_message) # Return the decrypted message