# TODO: Get specific details on formats that GJBs use. 
# Combo of Type 1 and 2

import signal_processing as sp # Load signal processing module

# Handle decoding of GJB 2077-94 2G ALE Format 
def decode(data):
	decoded_data = bytearray.fromhex(data)  # Hex to Bytes
	header = bytearray(decoded_data[:2])  # First two bytes are the header
	map = decoded_data[2:-1]  # 3rd to last byte are the map info
	po = decoded_data[-1]  # Last byte is the position offset
	position_offset = sp.hex_str_to_bin(po) # Convert from hex to binary
	
	decoded_data = dict() # Create Dictionary object
	decoded_data["header"] = header # Add header to dictionary
	decoded_data["map"] = map # Add map to dictionary
	decoded_data["po"] = position_offset # Add po to dictionary
	
	return decoded_data # Return decoded data
 	
# Test with sample data
sample_data = "00010000524B7FFFFFFFFF033F"
decoded_data = decode(sample_data)
print(decoded_data) # --> {'header': bytearray(b'\x00\x01'), 'map': bytearray(b'\x00\x00RK'), 'po': '11111'}