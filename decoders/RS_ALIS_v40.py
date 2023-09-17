# TODO: Test / Debug

'''
This script will decode R&S ALIS v40 for radio frequency signal intelligence. 
'''

import bitstring #library to work with bit-level data
import logging #logging library for debugging

# ALIS v40 consists of 3 frames: Ch. sync, header, data 
# Each frame starts with 3 pseudo-random bits (0,1,1), followed by a 16 bit pseudorandom sequence 

#decoding process:

#Define the constants 
PREGEN_64 = [0, 1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192] #array of 16 pseudorandom values used in ALIS v40 

def GenSynchBits():
  '''
  Generates pre-syncronization bits 
  '''
  pregen = [0,1,1]
  return pregen

def decodeFrameData(frame):
  '''
  Decodes the frame data on R&S ALIS v40
  :param frame: 256 bit frame to decode
  :return: decoded data as a byte array
  '''
  bs = bitstring.BitStream(frame)
  
  # Marker bits comprised of 3 Pseudo-Random bits (0,1,1)
  marker_bits = bs.read('bin:3')
  if marker_bits != '011':
    logging.warning("Unexpected marker bits.")

  # 16 bits of Pseudo-Random sequence
  preseq_u16 = bs.read('uint: 16').uint
  
  # Strip of top 4 (MSB) bits of preseq_u16 
  preseq_seqb = preseq_u16 >> 4 
  found_seqb =  False

  # Compare Preseq_seqb with values in pregen 64 
  for seq_idx, pregen_val in enumerate(PREGEN_64):
    if preseq_seqb == pregen_val:
      data_length = 8 * (seq_idx + 1)
      found_seqb = True