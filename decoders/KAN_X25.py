#TODO: Research and implement decoding algorithm for KAN X.25 

# Python script for decoding KAN X.25 for use in RF signal intelligence

def decode_KAN_X25(rx_packet):
  """ Function to decode KAN X.25 """

  # Basic Structure of KAN X.25 packet 
  # Prefix | Format | Destination/Source Address | Data Field | Checksum 
  # 1 byte | 1 byte | 2 bytes                  | n bytes   | 1 byte

  # Get Prefix, Format, Destination/Source, and Checksum bytes from packet
  prefix = rx_packet[0]
  format = rx_packet[1]
  destination = rx_packet[2:4]
  checksum = rx_packet[-1]

  # Calculate checksum using length of packet
  checksum_calc = 0
  for i in range(len(rx_packet)-1):
    checksum_calc = checksum_calc + rx_packet[i]

  # Compare calculations to received checksum byte to ensure packet is valid
  if checksum == checksum_calc:
    data_field = rx_packet[4:-1] # Get data field, exclude Prefix, Format, Dest/Source, AND Checksum bytes
    return prefix, format, destination, data_field, checksum
  else:
    print("Checksum error. Packet is not valid.")