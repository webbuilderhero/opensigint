import base64

#TODO: Figure out how to define constants for the different mapping from decimals to ascii characters

def bozon_2m_decoder(input_data):
  """
  A function that decodes the provided data using the bozon-2M format

  Parameters:
    input_data: A string of data to be decoded with the bozon-2M format
  
  Returns:
    A decoded string
  """

  # Create a mapping of decimal numbers to ascii characters
  decimal_to_ascii_map = {
    0 : 'a',
    1 : 'b',
    2 : 'c',
    3 : 'd',
    4 : 'e',
    5 : 'f',
    6 : 'g',
    7 : 'h',
    8 : 'i',
    9 : 'j',
    10 : 'k',
    11 : 'l',
    12 : 'm',
    13 : 'n',
    14 : 'o',
    15 : 'p',
    16 : 'q',
    17 : 'r',
    18 : 's',
    19 : 't',
    20 : 'u',
    21 : 'v',
    22 : 'w',
    23 : 'x',
    24 : 'y',
    25 : 'z'
  }

  # Decode the data using the bozon-2M format
  dec_input = base64.b64decode(input_data)
  decoded_message = ""
  for char in dec_input:
    # Convert the character to its decimal value
    decimal_value = ord(char)
    
    # Lookup the corresponding ascii character in the mapping
    ascii_letter = decimal_to_ascii_map[decimal_value%26]

    # Append the ascii character to the decoded message
    decoded_message += ascii_letter

  # Return the decoded message
  return decoded_message