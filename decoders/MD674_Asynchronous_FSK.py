"""
"""
# TODO: Further test and modify code to make sure it will plug into the framework as needed

# Defining Decoder for MD-674 Asynchronous FSK
def MD674 Decoder(data): 
  # Establishing shifting MSB first
  shift_MSB_first = data
  
  # Establishing no of bits in each symbol
  symbol_bits = 7 
  
  # Establishing parities
  even_parity = 0
  odd_parity = 1

  # Establishing bit order = MSB First
  bit_order = 'MSB'

  # Establishing number of bits per word 
  word_bits = 8

  # Establishing sync word
  sync_word = 0x7F
  
  # Establishing list of possible frequencies  
  freqs = [400,2120]  

  # Establishing decoding table 
  DecoderTable = {
     '00000': '0000',
     '00001': '0001',
     '00010': '0010', 
     '00011': '0011',
     '00100': '0100',
     '00101': '0101',
     '00110': '0110',
     '00111': '0111',
     '01000': '1000',
     '01001': '1001',
     '01010': '1010',
     '01011': '1011',
     '01100': '1100',
     '01101': '1101',
     '01110': '1110',
     '01111': '1111',
     '10000': ' [SP]',
     '10001': ' [DL]',
     '10010': ' [ST]',
     '10011': ' [SK]',
     '10100': ' [ETX] ',
     '10101': ' [ETB] ',
     '10110': ' [ENQ] ',
     '10111': ' [ACK] ',
     '11000': ' [SYN] ',
     '11001': ' [LF] ',
     '11010': ' [VT] ',
     '11011':