# SIGINT Framework Decoder
# Decoder for R-149MA1

# Inputs
raw_data = '' # Raw data to be decoded

# Outputs
decoded_data = '' # Decoded data

# TODO: Specify data format and other parameters

# Algorithm for decoder
def decode(raw_data):
    """
    Decodes R-149MA1 signal
    Args:
        raw_data (str): Raw signal data
    Returns:
        data (str): Decoded data
    """
    # Create a lookup table for data decoding
    bit_map = {
    '00' : 'A',
    '01' : 'B',
    '10' : 'C',
    '11' : 'D'
    }

    # Initialize decoded data
    decoded_data = ''
    
    # Iterate through raw data two bits at a time
    for i in range(0, len(raw_data), 2):
        # Get two-bit pair
        bit_pair = raw_data[i:i+2]
        
        # Look up bit pair in lookup table
        if bit_pair in bit_map.keys():
            # Append the corresponding decoded value
            decoded_data += bit_map[bit_pair] 
        # In case bit_pair is not present in bit_map
        else:
            # Append it as it is
            decoded_data += bit_pair   
            
    return decoded_data

# Decode raw data
decoded_data = decode(raw_data)