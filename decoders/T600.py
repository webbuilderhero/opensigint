#TODO: Make sure the script plugs into the framework 

# Decoder for T-600

import math

def decode(signal):
  """
  Decodes an RF signal to a T-600 signal.

  Args:
    signal (float): The signal as a number.

  Returns:
    A decoded T-600 signal.
  """ 

  baud_rate = 1200
  frame_length = 20.0 / baud_rate

  bits = []
  total_time = 0

  while total_time < (len(signal) * frame_length):
    bit_val = 0
    time = 0

    while time < frame_length / 2.0:
      bit_val += signal[math.floor(total_time / frame_length)]
      time += frame_length
      total_time += frame_length

    if bit_val >= 0:
      bits.append(1)
    else:
      bits.append(0)
  
  binary_code = ''
  for bit in bits:
    binary_code += str(bit)

  return int(binary_code, 2)