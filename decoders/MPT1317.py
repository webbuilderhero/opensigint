# TODO:
# Decode signal format

def decode(signal):
  # STEP 1: Separate Letters
  letter1, letter2, letter3 = signal[0:-4], signal[3:-1], signal[4:]

  # STEP 2: Decode by Letter 
  decoded_signal = ''
  char_table = {'M': '1', 'P': '2', 'T': '3', '1': 'M', '2': 'P', '3':'T'}

  decoded_signal += chr(int(char_table[letter1]))
  decoded_signal += chr(int(char_table[letter2]))
  decoded_signal += chr(int(char_table[letter3]))

  # STEP 3: Return decoded signal
  return decoded_signal