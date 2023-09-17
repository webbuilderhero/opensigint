# TODO: Plug into current sigint framework 

# Decoder for ICS Electronics v4 

def ics_decoder(data):
    # Declare output 
    output = ""
    # Iterate through each byte 
    for byte in data: 
        # Convert byte to octal 
        output += format(int(byte, 16), '04o')
    return output